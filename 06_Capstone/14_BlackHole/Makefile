# Standardized commands across all capstone projects
.PHONY: setup test run up down

setup:
	python -m venv venv
	venv/bin/pip install -r requirements.txt

test:
	pytest tests/

up:
	docker-compose -f infrastructure/docker-compose.yml up -d

down:
	docker-compose -f infrastructure/docker-compose.yml down

run:
	python src/main.py
