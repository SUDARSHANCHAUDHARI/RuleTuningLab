# Demo

Run the included rules against labeled synthetic logs:

```bash
python3 -m src.evaluator
```

Expected output:

```text
Evaluated 3 noisy rule(s)
Generated 2 tuning suggestion(s)
```

Generated artifacts:

- `reports/evaluation.json`
- `reports/summary.json`
- `reports/tuning-plan.json`
- `reports/tuning-report.md`
- `reports/triage.md`

The sample demonstrates noisy brute-force and port-scan rules alongside a clean web-attack rule.
