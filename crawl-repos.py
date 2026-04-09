#!/usr/bin/env python3
"""
star_and_follow_top_repos.py

- Reads users.json -> {"users": [...]} and keywords.json -> {"keywords": [...]}
- Searches GitHub for repositories matching keywords (configurable MIN_STARS)
- Scores repos by:
    * repo stars (log)
    * contributions from known experts (counts weighted by contributor follower counts)
    * owner follower count (log)
    * recency (updated_at)
- Selects TOP_K repos by score, then:
    * Stars each repo
    * Follows the repo owner
    * Follows contributors who are in the users list (and optionally top contributors)
- Uses exponential backoff for rate limits and polite sleeps
- Configure thresholds at the top of the file
"""

import os
import time
import json
import math
import requests
from datetime import datetime, timezone
from pathlib import Path

# -------------------------
# CONFIGURATION (tune these)
# -------------------------
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
if not GITHUB_TOKEN:
    raise SystemExit("Set GITHUB_TOKEN environment variable before running the script.")

# Minimum stars to include a repo in initial search (adjust to be strict)
MIN_STARS = 20000        # default 20k; raise to 100000 for very strict selection

# Final number of top repositories to process
TOP_K = 25

# How many search results to fetch per keyword (max 100)
RESULTS_PER_PAGE = 30

# Sleep between GitHub API calls to avoid rate limits
SLEEP_BETWEEN_REQUESTS = 1.0

# Maximum retries on 403/429 with exponential backoff
MAX_RETRIES = 6

# How many top contributors to fetch for scoring and following
TOP_CONTRIBS_TO_FETCH = 50
TOP_CONTRIBS_TO_FOLLOW = 5

# Weights for scoring (tweak to emphasize different signals)
WEIGHT_STARS = 2.0
WEIGHT_OWNER_FOLLOWERS = 1.0
WEIGHT_CONTRIB = 3.0
WEIGHT_RECENCY = 10.0

# -------------------------
# HEADERS
# -------------------------
GITHUB_HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}

# -------------------------
# FILE LOADING
# -------------------------
def load_json_list(path: str, key: str):
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Required file not found: {path}")
    with p.open("r", encoding="utf-8") as f:
        data = json.load(f)
    items = data.get(key)
    if not isinstance(items, list):
        raise ValueError(f"File {path} must contain a top-level '{key}' array.")
    seen = set()
    cleaned = []
    for it in items:
        if not isinstance(it, str):
            continue
        s = it.strip()
        if not s:
            continue
        if s not in seen:
            seen.add(s)
            cleaned.append(s)
    return cleaned

# -------------------------
# HTTP helper with backoff
# -------------------------
def safe_request(method, url, **kwargs):
    last_resp = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = requests.request(method, url, headers=GITHUB_HEADERS, timeout=30, **kwargs)
        except requests.RequestException as e:
            last_resp = None
            wait = (2 ** (attempt - 1)) * 1.5
            print(f"[request error] {e}. Backing off {wait:.1f}s (attempt {attempt}).")
            time.sleep(wait)
            continue

        last_resp = resp
        if resp.status_code in (200, 201, 204, 304):
            return resp
        if resp.status_code in (403, 429):
            wait = (2 ** (attempt - 1)) * 1.5
            reset = resp.headers.get("X-RateLimit-Reset")
            if reset:
                try:
                    reset_ts = int(reset)
                    now_ts = int(time.time())
                    wait = max(wait, reset_ts - now_ts + 1)
                except Exception:
                    pass
            print(f"[rate limited] status {resp.status_code}. Backing off {wait:.1f}s (attempt {attempt}).")
            time.sleep(wait)
            continue
        # other errors: return response for caller to inspect
        return resp
    raise RuntimeError(f"Exceeded retries for {url} (last status {last_resp.status_code if last_resp else 'N/A'})")

# -------------------------
# GitHub helpers
# -------------------------
def search_repositories(keyword: str, min_stars: int, per_page: int = RESULTS_PER_PAGE):
    stars_qual = f"stars:>={min_stars}"
    q = f'{keyword} in:readme,description,topics {stars_qual}'
    url = "https://api.github.com/search/repositories"
    params = {"q": q, "sort": "stars", "order": "desc", "per_page": per_page}
    resp = safe_request("GET", url, params=params)
    if resp.status_code != 200:
        print(f"[search failed] '{keyword}' (stars>={min_stars}): {resp.status_code} {resp.text[:200]}")
        return []
    items = resp.json().get("items", [])
    print(f"[search] '{keyword}' → {len(items)} results (stars>={min_stars})")
    return items

def get_contributors(owner: str, repo: str, top_n: int = TOP_CONTRIBS_TO_FETCH):
    url = f"https://api.github.com/repos/{owner}/{repo}/contributors"
    resp = safe_request("GET", url, params={"per_page": top_n})
    if resp.status_code != 200:
        print(f"[contributors failed] {owner}/{repo}: {resp.status_code}")
        return []
    return resp.json()

def get_user_profile(username: str):
    url = f"https://api.github.com/users/{username}"
    resp = safe_request("GET", url)
    if resp.status_code != 200:
        # return minimal fallback
        return {"login": username, "followers": 0}
    return resp.json()

def star_repository(owner: str, repo: str):
    url = f"https://api.github.com/user/starred/{owner}/{repo}"
    resp = safe_request("PUT", url)
    if resp.status_code in (204, 304):
        print(f"⭐ Starred: {owner}/{repo}")
    else:
        print(f"❌ Failed to star {owner}/{repo}: {resp.status_code} {resp.text[:200]}")

def follow_user(username: str):
    url = f"https://api.github.com/user/following/{username}"
    resp = safe_request("PUT", url)
    if resp.status_code in (204, 304):
        print(f"👤 Followed: {username}")
    else:
        print(f"❌ Failed to follow {username}: {resp.status_code} {resp.text[:200]}")

# -------------------------
# Scoring
# -------------------------
def log1p(x):
    return math.log(x + 1)

def compute_contrib_signal(contribs: list, known_users_set: set):
    """
    contribs: list of contributor dicts from GitHub API (each has 'login')
    known_users_set: set of usernames considered experts
    Returns a numeric contribution signal:
      sum over contributors of (expert_multiplier * log(follower_count+1))
    """
    total = 0.0
    for c in contribs:
        login = c.get("login")
        if not login:
            continue
        # fetch follower count for contributor (cached externally by caller if needed)
        profile = get_user_profile(login)
        followers = profile.get("followers", 0) or 0
        multiplier = 2.0 if login in known_users_set else 1.0
        total += multiplier * log1p(followers)
        # small polite pause to avoid bursts
        time.sleep(0.05)
    return total

def score_repo(repo: dict, contrib_signal: float, owner_followers: int):
    stars = repo.get("stargazers_count", 0)
    forks = repo.get("forks_count", 0)
    updated_at = repo.get("updated_at")
    recency_score = 0.0
    if updated_at:
        try:
            dt = datetime.fromisoformat(updated_at.replace("Z", "+00:00"))
            days = (datetime.now(timezone.utc) - dt).days
            recency_score = 1.0 / (1 + math.log(days + 1 + 1e-9))
        except Exception:
            recency_score = 0.0

    score = (
        WEIGHT_STARS * log1p(stars)
        + 0.5 * log1p(forks)
        + WEIGHT_CONTRIB * contrib_signal
        + WEIGHT_OWNER_FOLLOWERS * log1p(owner_followers)
        + WEIGHT_RECENCY * recency_score
    )
    return score

# -------------------------
# Main flow
# -------------------------
def main():
    users = load_json_list("users.json", "users")
    keywords = load_json_list("keywords.json", "keywords")
    known_users_set = set(users)
    print(f"Loaded {len(users)} users and {len(keywords)} keywords.")

    repo_map = {}  # full_name -> repo object

    # Search phase
    for kw in keywords:
        try:
            items = search_repositories(kw, MIN_STARS)
        except Exception as e:
            print(f"[search error] '{kw}': {e}")
            continue

        for r in items:
            full = r.get("full_name")
            if not full:
                continue
            # enforce min stars
            if r.get("stargazers_count", 0) < MIN_STARS:
                continue
            # dedupe: keep highest-starred version
            existing = repo_map.get(full)
            if existing is None or r.get("stargazers_count", 0) > existing.get("stargazers_count", 0):
                repo_map[full] = r
        time.sleep(SLEEP_BETWEEN_REQUESTS)

    if not repo_map:
        print("No repositories found with the configured MIN_STARS. Consider lowering MIN_STARS.")
        return

    # Contributor analysis & scoring
    scored = []
    for full, repo in repo_map.items():
        owner = repo["owner"]["login"]
        name = repo["name"]
        print(f"\nAnalyzing {full} — ⭐ {repo.get('stargazers_count',0)}")

        # fetch owner profile for follower count
        owner_profile = get_user_profile(owner)
        owner_followers = owner_profile.get("followers", 0) or 0

        # fetch contributors
        contribs = get_contributors(owner, name, top_n=TOP_CONTRIBS_TO_FETCH)
        contrib_signal = compute_contrib_signal(contribs, known_users_set)

        # compute score
        s = score_repo(repo, contrib_signal, owner_followers)
        scored.append((full, s, repo, contribs))
        # polite pause
        time.sleep(0.5)

    # sort and pick top K
    scored.sort(key=lambda x: x[1], reverse=True)
    top = scored[:TOP_K]
    print(f"\nSelected top {len(top)} repositories (TOP_K={TOP_K}):\n")
    for i, (full, s, repo, contribs) in enumerate(top, start=1):
        print(f"{i}. {full} — score={s:.2f} — ⭐ {repo.get('stargazers_count',0)} — owner followers={get_user_profile(repo['owner']['login']).get('followers',0)}")

    # Action phase: star repos, follow owners, follow known contributors
    for full, s, repo, contribs in top:
        owner, name = full.split("/")
        print(f"\nProcessing actions for {full} (score={s:.2f})")
        try:
            star_repository(owner, name)
        except Exception as e:
            print(f"[star error] {full}: {e}")

        try:
            follow_user(owner)
        except Exception as e:
            print(f"[follow owner error] {owner}: {e}")

        # follow contributors who are in the known users list first
        followed = set()
        for c in contribs:
            login = c.get("login")
            if not login:
                continue
            if login in known_users_set:
                try:
                    follow_user(login)
                    followed.add(login)
                except Exception as e:
                    print(f"[follow contrib error] {login}: {e}")
                time.sleep(0.2)

        # then follow top contributors by follower count up to TOP_CONTRIBS_TO_FOLLOW
        remaining_to_follow = TOP_CONTRIBS_TO_FOLLOW - len(followed)
        if remaining_to_follow > 0:
            # sort contributors by follower count (fetch profiles)
            contrib_profiles = []
            for c in contribs:
                login = c.get("login")
                if not login or login in followed:
                    continue
                profile = get_user_profile(login)
                contrib_profiles.append((login, profile.get("followers", 0) or 0))
                time.sleep(0.05)
            contrib_profiles.sort(key=lambda x: x[1], reverse=True)
            for login, _ in contrib_profiles[:remaining_to_follow]:
                try:
                    follow_user(login)
                except Exception as e:
                    print(f"[follow contrib error] {login}: {e}")
                time.sleep(0.2)

        time.sleep(SLEEP_BETWEEN_REQUESTS)

    print("\n✅ Completed processing top repositories.")

if __name__ == "__main__":
    main()
