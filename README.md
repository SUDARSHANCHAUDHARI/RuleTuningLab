# Rule Tuning Lab

[![Python](https://img.shields.io/badge/Python-3.12-blue)](#) [![Status](https://img.shields.io/badge/status-MVP-green)](#) [![Security](https://img.shields.io/badge/security-defensive%20lab-purple)](#)

Detection tuning lab that measures false positives and suggests rule improvements from labeled logs.

- **Portfolio group:** Cybersecurity lab project
- **Status:** MVP implemented, tested, committed, and pushed to GitHub
- **GitHub:** https://github.com/SUDARSHANCHAUDHARI/RuleTuningLab
- **Local path:** `/Users/screencloudsudarshan/SUDARSHAN_CODE/sudarshan_repos/CyberSecurity/RuleTuningLab`

## MVP Snapshot

This repository includes a working MVP with safe sample data, deterministic detection or analysis logic, local tests, and generated output reports where relevant. It is ready for README/demo polish or deeper product work.

## Safe Use

This project is defensive and analysis-focused. Use only with logs, systems, repositories, and lab environments you own or have permission to assess.

## Core Features

- rule test runner
- false positive counter
- alert severity tuning
- before/after report


## Install

```bash
pip install .
```

This registers the `rule-tuning-lab` command. Or run directly:

```bash
python3 main.py --help
```

## Quick Start

```bash
python3 -m src.evaluator
python3 -m unittest discover -s tests -p 'test_*.py'
```

The sample logs are safe synthetic labeled events.

## MVP Capabilities

- Loads detection rules from YAML-like files
- Runs rules against labeled sample logs
- Counts true positives and false positives
- Calculates false positive rate
- Calculates precision and a noise grade per rule
- Suggests tuning actions for noisy rules
- Writes evaluation JSON, summary JSON, tuning plan JSON, Markdown report, and triage handoff

## Demo Artifacts

- [Architecture](docs/ARCHITECTURE.md)
- [Security notes](docs/SECURITY_NOTES.md)
- [Demo walkthrough](docs/DEMO.md)
- [Release notes](docs/RELEASE_NOTES.md)
- [Sample tuning report](reports/tuning-report.md)
- [Sample triage report](reports/triage.md)
- [Sample tuning plan](reports/tuning-plan.json)

## Docker Demo

```bash
docker compose run --rm rule-tuning-demo
```

## Roadmap

- Add before/after simulation using proposed rule changes.
- Add suppression and allowlist condition examples.
- Add severity downgrade impact analysis.
- Add dashboard charts for noisy rules.
- Prepare GitHub release `v0.1.0-mvp`.
