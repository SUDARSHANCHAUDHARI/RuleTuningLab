# Rule Tuning Report

- Rules with alerts: 3

## Evaluation

### brute-force

- Alerts: 3
- True positives: 2
- False positives: 1
- False positive rate: 0.333

### port-scan

- Alerts: 3
- True positives: 2
- False positives: 1
- False positive rate: 0.333

### web-attack

- Alerts: 2
- True positives: 2
- False positives: 0
- False positive rate: 0.0

## Suggestions

- **medium** `brute-force`: Review sample false positives and add an allow-list condition.
- **medium** `port-scan`: Review sample false positives and add an allow-list condition.
