.PHONY: install dev test lint fmt scan docker up

install:      ## Install all deps (incl. dev) and git hooks
	uv sync
	uv run pre-commit install

dev:          ## Run locally with hot reload on http://localhost:8000
	uv run uvicorn app.main:app --reload

test:         ## Unit + integration tests with coverage gate
	uv run pytest

lint:         ## Lint, format check and type check
	uv run ruff check .
	uv run ruff format --check .
	uv run mypy app

fmt:
	uv run ruff check --fix .
	uv run ruff format .

scan:         ## Local security scans (same as CI)
	uv run bandit -r app -q
	uv run pip-audit

docker:
	docker build -t jyotish-ai:local .

up:           ## App + Firestore emulator via docker compose
	docker compose up --build
