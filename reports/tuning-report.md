# Rule Tuning Report

- Rules with alerts: 3
- Total alerts: 8
- False positives: 2
- Overall false positive rate: 0.25

## Priority Tuning Plan

- `brute-force`: needs-tuning, fp_rate=0.333, action=Review sample false positives and add an allow-list or environment context condition.
- `port-scan`: needs-tuning, fp_rate=0.333, action=Review sample false positives and add an allow-list or environment context condition.
- `web-attack`: clean, fp_rate=0.0, action=No tuning needed.

## Evaluation

### brute-force

- Alerts: 3
- True positives: 2
- False positives: 1
- False positive rate: 0.333
- Precision: 0.667
- Noise grade: `needs-tuning`
- Severity recommendation: `add-allowlist-context`

False positive examples:
- `expected=false sshd Failed password for user deploy from 10.0.0.10`

### port-scan

- Alerts: 3
- True positives: 2
- False positives: 1
- False positive rate: 0.333
- Precision: 0.667
- Noise grade: `needs-tuning`
- Severity recommendation: `add-allowlist-context`

False positive examples:
- `expected=false firewall healthcheck ports=443`

### web-attack

- Alerts: 2
- True positives: 2
- False positives: 0
- False positive rate: 0.0
- Precision: 1.0
- Noise grade: `clean`
- Severity recommendation: `keep`

## Suggestions

- **medium** `brute-force`: Review sample false positives and add an allow-list or environment context condition.
- **medium** `port-scan`: Review sample false positives and add an allow-list or environment context condition.
