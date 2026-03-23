# Data_Quality

Almost always? Missing checks. Not technical mystery.

Here are the 20 every reliable pipeline needs 👇

────────────────────
🔴 𝗦𝘁𝗿𝘂𝗰𝘁𝘂𝗿𝗮𝗹 (𝟭–𝟱)
────────────────────
01 · Null Check — critical columns, no unexpected nulls
02 · Duplicate Records — same PK twice = silent corruption
03 · Primary Key Validation — every record, valid + unique
04 · Referential Integrity — foreign keys must resolve
05 · Accepted Values — "FLYING" is not a valid order status

────────────────────
🟠 𝗙𝗼𝗿𝗺𝗮𝘁 & 𝗩𝗼𝗹𝘂𝗺𝗲 (𝟲–𝟭𝟬)
────────────────────
06 · Data Type Validation — price stored as string breaks everything
07 · Range Validation — a -£500 order total is a bug, not a refund
08 · Date Consistency — start_date > end_date never reaches Gold
09 · Freshness Check — no new data in the window = broken pipeline
10 · Volume Check — sudden record spikes are upstream failures in disguise

────────────────────
🟡 𝗖𝗼𝗻𝘀𝗶𝘀𝘁𝗲𝗻𝗰𝘆 & 𝗗𝗿𝗶𝗳𝘁 (𝟭𝟭–𝟭𝟱)
────────────────────
11 · Outlier Detection — flag abnormal values even when they pass other checks
12 · Schema Change Detection — pipeline should know before stakeholders do
13 · Format Validation — emails, phones, postcodes follow patterns. Enforce them
14 · Completeness Check — non-null isn't enough. Meaningfully filled
15 · Distribution Drift — data shifting run-to-run = something upstream changed

────────────────────
🟢 𝗕𝘂𝘀𝗶𝗻𝗲𝘀𝘀 𝗟𝗼𝗴𝗶𝗰 & 𝗛𝗶𝘀𝘁𝗼𝗿𝘆 (𝟭𝟲–𝟮𝟬)
────────────────────
16 · Business Rule Validation — order_total > 0 belongs in your pipeline, not a Slack message
17 · Cross-Field Consistency — qty=5, line_total=0 is not a discount. It's a bug
18 · Duplicate Event Detection — ingestion errors land the same event twice
19 · Aggregation Consistency — if Bronze and Gold disagree, one is wrong
20 · Historical Comparison — sudden anomalies = upstream changes nobody told you about
