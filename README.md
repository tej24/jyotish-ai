# JyotishAI

[![CI](https://github.com/tej24/jyotish-ai/actions/workflows/ci.yml/badge.svg)](https://github.com/tej24/jyotish-ai/actions/workflows/ci.yml)
[![CodeQL](https://github.com/tej24/jyotish-ai/actions/workflows/codeql.yml/badge.svg)](https://github.com/tej24/jyotish-ai/actions/workflows/codeql.yml)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](LICENSE)

An open-source Vedic astrology web app. Enter your birth details (or upload a kundli),
ask a question, and get a reading grounded in an exactly computed birth chart, followed
by up to 5 follow-up questions.

> **Status:** Phase 0 — project skeleton, CI and security pipeline. The chart engine
> (Phase 1) and AI readings (Phase 2) are in progress. See the [roadmap](#roadmap).

## How it works

```
Browser ──► FastAPI (Cloud Run) ──► Chart engine (pyswisseph, exact maths)
                    │                        │
                    │                        ▼
                    └──────────────► LLM (Gemini / Claude) writes the reading
                                     from the computed chart JSON only
```

The key design rule: **the LLM never calculates anything.** Planet positions, houses,
nakshatras and dashas come from the Swiss Ephemeris; the LLM only interprets them.
See [ADR 0001](docs/adr/0001-chart-engine-plus-llm.md).

## Tech stack

| Layer | Technology |
| --- | --- |
| Language | Python 3.12 |
| Web | FastAPI, Uvicorn, Jinja2, HTMX |
| Astrology | pyswisseph (sidereal, Lahiri ayanamsa) |
| AI | Gemini / Claude behind a provider interface |
| State | Firestore (sessions, 24 h TTL) |
| Packaging | uv, Docker (multi-stage, non-root) |
| Hosting | Google Cloud Run (asia-south1) |
| IaC | Terraform |
| CI/CD | GitHub Actions, Workload Identity Federation (no keys) |
| Security | Ruff, mypy, Bandit, CodeQL, pip-audit, Gitleaks, Trivy, Dependabot |

## Quickstart

Prerequisites: [uv](https://docs.astral.sh/uv/) and Python 3.12. Docker is optional.

```bash
git clone https://github.com/tej24/jyotish-ai.git
cd jyotish-ai
make install   # deps + pre-commit hooks
make dev       # http://localhost:8000  (API docs at /docs)
make test      # tests with coverage gate
```

With Docker:

```bash
make up        # app on http://localhost:8080 + Firestore emulator
```

## Project layout

```
app/          FastAPI app: routes, templates, static assets
tests/        pytest suite
docs/adr/     Architecture Decision Records
.github/      CI, CodeQL, Dependabot, CODEOWNERS
```

## Roadmap

- [x] **Phase 0** — skeleton, CI, security scanning, container
- [ ] **Phase 1** — chart engine: birth data → D1/D9 chart, dashas, golden-chart tests
- [ ] **Phase 2** — LLM readings, sessions, 5-question follow-up chat
- [ ] **Phase 3** — Terraform, staging on Cloud Run, Playwright E2E, image signing
- [ ] **Phase 4** — kundli upload (vision extraction), PDF export, public launch

## Disclaimer

JyotishAI is for entertainment and self-reflection only. It does not provide medical,
legal, financial or other professional advice.

## License

[AGPL-3.0-or-later](LICENSE). This project uses the Swiss Ephemeris via pyswisseph,
which is AGPL-licensed. If you run a modified version as a public service, you must
publish your source.
