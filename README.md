# Rule Tuning Lab

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](#requirements)
[![Status](https://img.shields.io/badge/status-MVP-green)](#status)
[![Security](https://img.shields.io/badge/security-defensive%20lab-purple)](#safe-use)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Detection tuning lab. Measures false-positive rate, precision, and noise grade per detection rule, then suggests tuning improvements based on labeled log samples.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Docker Demo](#docker-demo)
- [Safe Use](#safe-use)
- [Status](#status)
- [Roadmap](#roadmap)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)
- [About](#about)

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

## Documentation

Full project documentation lives in [`docs/`](docs/):

- [Architecture](docs/ARCHITECTURE.md) — component design and data flow
- [Demo](docs/DEMO.md) — step-by-step demo walkthrough
- [Security Notes](docs/SECURITY_NOTES.md) — defensive-use guidance and threat model
- [Production Readiness](docs/PRODUCTION_READINESS.md) — gaps between MVP and production
- [Roadmap](docs/ROADMAP.md) — planned features
- [Release Notes](docs/RELEASE_NOTES.md) — version history

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and the [Code of Conduct](CODE_OF_CONDUCT.md) before opening a pull request. To report a security issue, see [SECURITY.md](SECURITY.md).

## License

Released under the [MIT License](LICENSE). You are free to use, modify, and distribute this software with attribution.

---

## About

I'm Sudarshan Chaudhari, a Senior Quality Engineer, Test Automation specialist, and AI systems builder based in Bangkok, Thailand.

I have 13+ years of experience in software quality engineering, working across SaaS, fintech, gaming, web, mobile, cloud, and digital signage platforms. My background combines hands-on test automation with QA leadership, test strategy, CI/CD, release quality, production investigation, and cross-platform validation.

Alongside my professional QA career, I run [SudarshanTechLabs](https://sudarshantechlabs.com/), my independent engineering and product lab where I design, build, test, and ship software across Android, web, AI, cybersecurity, developer tooling, and cross-platform applications.

### What I work on

- ⚙️ **Quality Engineering & Test Automation** — Playwright, Selenium, Cypress, Appium, API testing, automation frameworks, end-to-end testing, CI/CD, release gates, GitHub Actions, risk-based testing, and production validation
- 🤖 **AI Systems & Automation** — AI agents, multi-agent orchestration, MCP servers, AI-assisted QA, prompt tooling, developer workflows, automation systems, and Claude Code plugins
- 📱 **Mobile & Cross-Platform Applications** — Android applications built with Kotlin and Jetpack Compose, Google Play releases, automated build and publishing pipelines, and cross-platform development spanning iOS, web, Windows, and macOS
- 🌐 **Web Applications & Platforms** — Full-stack applications using Next.js, TypeScript, Firebase, Cloudflare, REST APIs, and modern web infrastructure
- 🛠️ **Developer Tooling & CLI Engineering** — Rust, Python, TypeScript, CLI utilities, multi-repository tooling, build automation, release tooling, and engineering productivity systems
- 🛡️ **Cybersecurity & Observability** — Threat detection, log analysis, security auditing, vulnerability assessment, monitoring, and security-focused developer tools
- 📺 **Digital Signage & Device Platforms** — Content validation, playback testing, device compatibility, production investigation, monitoring, and QA across diverse hardware and operating-system environments

My work sits at the intersection of quality engineering, automation, AI, and software development. I approach products with a QA mindset from the beginning: understanding failure modes, designing for testability, automating repetitive work, and building release confidence into the engineering process.

Through SudarshanTechLabs, I also build products and tools from idea to production, covering architecture, development, testing, CI/CD, release automation, monitoring, and ongoing maintenance.

🌐 [sudarshantechlabs.com](https://sudarshantechlabs.com/) · 💼 [LinkedIn](https://linkedin.com/in/sudarshan-chaudhari) · 🐙 [GitHub](https://github.com/SUDARSHANCHAUDHARI) · ✉️ [sunny.sudarshan@gmail.com](mailto:sunny.sudarshan@gmail.com)
