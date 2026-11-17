# Security Policy

## Reporting a vulnerability

Please report security issues privately via GitHub's
[private vulnerability reporting](https://github.com/tej24/jyotish-ai/security/advisories/new).
Do not open a public issue.

You'll get an acknowledgement within 72 hours and a status update within 7 days.

## Supported versions

Only the latest release on `main` receives fixes.

## How this project handles your data

- Birth details are used only to compute your chart and are not stored beyond a 24-hour session.
- Uploaded kundli files are processed in memory and never written to disk or storage.
- Chart data (not your name) is sent to the configured LLM provider to write the reading.
