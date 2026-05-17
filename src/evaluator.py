"""Evaluate rule noise and false positives."""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
import json
from pathlib import Path

from src.rule_engine import Alert, load_rules, run_rules
from src.tuning_suggestions import Suggestion, build_suggestions


@dataclass(frozen=True)
class Evaluation:
    rule_id: str
    alerts: int
    true_positives: int
    false_positives: int
    false_positive_rate: float


def load_lines(paths: list[Path]) -> list[str]:
    lines: list[str] = []
    for path in paths:
        lines.extend(line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip() and not line.startswith("#"))
    return lines


def evaluate_alerts(alerts: list[Alert]) -> list[Evaluation]:
    grouped: dict[str, list[Alert]] = {}
    for alert in alerts:
        grouped.setdefault(alert.rule_id, []).append(alert)
    evaluations: list[Evaluation] = []
    for rule_id, group in sorted(grouped.items()):
        true_positives = sum(1 for alert in group if alert.expected_alert)
        false_positives = len(group) - true_positives
        evaluations.append(
            Evaluation(
                rule_id=rule_id,
                alerts=len(group),
                true_positives=true_positives,
                false_positives=false_positives,
                false_positive_rate=round(false_positives / len(group), 3),
            )
        )
    return evaluations


def build_report(evaluations: list[Evaluation], suggestions: list[Suggestion]) -> str:
    lines = ["# Rule Tuning Report", "", f"- Rules with alerts: {len(evaluations)}", ""]
    lines.extend(["## Evaluation", ""])
    for item in evaluations:
        lines.extend(
            [
                f"### {item.rule_id}",
                "",
                f"- Alerts: {item.alerts}",
                f"- True positives: {item.true_positives}",
                f"- False positives: {item.false_positives}",
                f"- False positive rate: {item.false_positive_rate}",
                "",
            ]
        )
    lines.extend(["## Suggestions", ""])
    for suggestion in suggestions or [Suggestion("none", "No tuning needed", "info")]:
        lines.append(f"- **{suggestion.severity}** `{suggestion.rule_id}`: {suggestion.message}")
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate detection rules against labeled sample logs")
    parser.add_argument("--rules", nargs="+", type=Path, default=sorted(Path("rules").glob("*.yaml")))
    parser.add_argument("--logs", nargs="+", type=Path, default=[Path("data/noisy-alerts.log"), Path("data/clean-alerts.log")])
    parser.add_argument("--out", type=Path, default=Path("reports/tuning-report.md"))
    parser.add_argument("--json-out", type=Path, default=Path("reports/evaluation.json"))
    args = parser.parse_args()

    alerts = run_rules(load_lines(args.logs), load_rules(args.rules))
    evaluations = evaluate_alerts(alerts)
    suggestions = build_suggestions(evaluations)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(build_report(evaluations, suggestions), encoding="utf-8")
    args.json_out.write_text(json.dumps([asdict(item) for item in evaluations], indent=2) + "\n", encoding="utf-8")
    print(f"Evaluated {len(evaluations)} noisy rule(s)")
    print(f"Generated {len(suggestions)} tuning suggestion(s)")


if __name__ == "__main__":
    main()
