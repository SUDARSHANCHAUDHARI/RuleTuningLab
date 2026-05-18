# Rule Tuning Triage

- Total alerts: 8
- Overall false positive rate: 0.25
- Noisy rules: brute-force, port-scan

## Analyst Queue

- `brute-force`: needs-tuning - Review sample false positives and add an allow-list or environment context condition.
- `port-scan`: needs-tuning - Review sample false positives and add an allow-list or environment context condition.
- `web-attack`: clean - No tuning needed.
