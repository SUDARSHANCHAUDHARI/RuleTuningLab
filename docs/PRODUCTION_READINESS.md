# Production Readiness

## Current Status

This repository has a working local MVP with deterministic rule evaluation, safe labeled sample logs, generated reports, and tests. It is not production complete yet.

## Required Before Public Release

- Add a real YAML parser before accepting broader rule syntax.
- Validate labeled log schema and reject unknown labels.
- Add structured logging without leaking secrets.
- Add before/after tuning simulation and rule-change audit history.
- Add authentication and authorization before storing multi-user logs.
- Add retention controls for uploaded logs and generated reports.
- Run dependency and secret scans before release.

## Definition of Done

- CI passes on pull requests.
- README has setup, usage, and security notes.
- Sample data is safe to publish.
- Error paths are handled clearly.
- No secrets or local machine paths are committed.
