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

## Roadmap

- Polish sample output screenshots or terminal demos
- Add architecture diagram and deeper implementation notes
- Expand test coverage around edge cases
- Add Docker or local demo workflow where useful
- Prepare `v0.1.0-mvp` release notes
