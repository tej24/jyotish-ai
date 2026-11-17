# ADR 0001: Exact chart engine + LLM interpreter

- Status: Accepted
- Date: 2026-11-17

## Context

Readings must be accurate (planet positions, houses, dashas) and also feel natural,
including follow-up questions. LLMs write fluently but cannot reliably compute
astronomical positions.

## Decision

1. A deterministic engine (pyswisseph, sidereal Lahiri ayanamsa) computes the chart.
2. The LLM receives only the computed chart as structured JSON and writes the interpretation.
3. The LLM sits behind an `LLMProvider` interface (Gemini first for its free tier,
   Claude as an alternative, a fake provider for tests).

## Consequences

- Positions are testable against reference charts (golden tests); the LLM is never the source of truth.
- The provider can be swapped or failed over without touching the rest of the app.
- pyswisseph is AGPL-3.0, so this repository is licensed AGPL-3.0.
