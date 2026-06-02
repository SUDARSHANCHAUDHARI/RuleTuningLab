# Rule Tuning Lab

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](#requirements)
[![Status](https://img.shields.io/badge/status-MVP-green)](#status)
[![Security](https://img.shields.io/badge/security-defensive%20lab-purple)](#safe-use)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Detection tuning lab. Measures false-positive rate, precision, and noise grade per detection rule, then suggests tuning improvements based on labeled log samples.

---

## Overview

Rule Tuning Lab is a defensive analysis tool for detection engineers. You provide YAML rule definitions plus labeled log samples (noisy + clean), and the tool evaluates each rule's precision, false-positive rate, and noise grade. It then suggests concrete tuning improvements (narrower regex, time-window adjustments, suppression filters) prioritized by impact.

## Features

- Loads YAML detection rules
- Evaluates rules against labeled log samples
- Calculates precision, false-positive rate, and noise grade per rule
- Generates tuning suggestions ranked by impact
- Outputs tuning plan, summary, Markdown report, and triage handoff

## Requirements

- Python 3.10 or newer
- Linux, macOS, or Windows
- No third-party Python packages (standard library only)
- Optional: Docker for the demo container

## Installation

```bash
git clone https://github.com/SUDARSHANCHAUDHARI/RuleTuningLab.git
cd RuleTuningLab
pip install .
```

This registers the `rule-tuning-lab` CLI command.

To run without installing:

```bash
python3 main.py --help
```

## Usage

Evaluate the included rules against the labeled samples:

```bash
python3 main.py --rules rules/*.yaml --logs data/noisy-alerts.log data/clean-alerts.log
```

Generated outputs in `reports/`:

- `evaluations.json` — per-rule precision, FPR, noise grade
- `suggestions.json` — ranked tuning suggestions
- `tuning-plan.json` — actionable tuning plan
- `summary.json` — counts and noise overview
- `report.md` — Markdown tuning report
- `triage.md` — analyst triage checklist

## Project Structure

```
RuleTuningLab/
├── src/            Rule engine, evaluator, tuning suggestion builder
├── rules/          YAML detection rule definitions
├── data/           Labeled sample alert logs (noisy + clean)
├── reports/        Example generated output
├── docker/         Dockerfile + compose support
├── docs/           Architecture, security notes, demo
├── tests/          Unit tests
├── main.py         CLI entrypoint
├── pyproject.toml  Package metadata
└── LICENSE
```

## Testing

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

## Docker Demo

```bash
docker compose run --rm rule-tuning-demo
```

## Safe Use

This project is defensive and analysis-focused. Use only with logs and detection rules you own or have explicit written permission to evaluate. The included samples are synthetic and safe for public demo use.

## Status

Working CLI MVP with tests, sample data, and Docker support.

## Roadmap

- Sigma rule format import / export
- Live SIEM integration (Splunk, Elastic) for production tuning
- A/B comparison of tuning iterations
- Auto-generated regression test suite per rule
- GitHub release `v0.1.0-mvp`

## License

Released under the [MIT License](LICENSE). You are free to use, modify, and distribute this software with attribution.

## Author

**Sudarshan Chaudhari** — [SudarshanTechLabs](https://github.com/SUDARSHANCHAUDHARI)
Bangkok, Thailand

For inquiries: open an issue on [GitHub](https://github.com/SUDARSHANCHAUDHARI/RuleTuningLab/issues).
