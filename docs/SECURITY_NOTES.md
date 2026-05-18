# Security Notes

This project is defensive and analysis-only. Use it only with detection rules and logs you own or have permission to evaluate.

## Data Handling

- Detection logs can include IP addresses, hostnames, usernames, URLs, and internal rule names.
- Redact production identifiers before sharing reports.
- Do not commit production SIEM exports or customer alert data.
- Sample data is synthetic and labeled with `expected=true` or `expected=false`.

## Detection Caveats

- False positives are context-dependent.
- A rule with no false positives in the sample can still be noisy in production.
- Tune rules with environment context, suppression audit history, and reviewer approval.
