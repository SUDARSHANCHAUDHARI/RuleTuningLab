# Rule Tuning

**Goal:** Reduce false positives in detection rules.

**MVP:** Run rules against sample logs and measure noise.

## Core Features

- rule test runner
- false positive counter
- alert severity tuning
- before/after report

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
- Suggests tuning actions for noisy rules
- Writes Markdown and JSON reports

## Repository Status

This repository contains a working Rule Tuning Lab MVP with safe labeled logs, evaluation metrics, tuning suggestions, generated reports, and tests.

## Production Foundation

- Private GitHub repository linked to `main`
- Initial MVP scaffold committed
- CI repository-health workflow
- Security policy
- Contribution guide
- Pull request and issue templates
- Production readiness checklist
- Safe ignore rules for local secrets and generated files
