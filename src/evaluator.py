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
    precision: float
    noise_grade: str
    severity_recommendation: str
    false_positive_examples: list[str]


def noise_grade(false_positive_rate: float) -> str:
    """Return a simple noise grade for portfolio reporting."""
    if false_positive_rate >= 0.5:
        return "noisy"
    if false_positive_rate > 0:
        return "needs-tuning"
    return "clean"


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
        false_positive_examples = [alert.line for alert in group if not alert.expected_alert][:3]
        fp_rate = round(false_positives / len(group), 3)
        precision = round(true_positives / len(group), 3)
        evaluations.append(
            Evaluation(
                rule_id=rule_id,
                alerts=len(group),
                true_positives=true_positives,
                false_positives=false_positives,
                false_positive_rate=fp_rate,
                precision=precision,
                noise_grade=noise_grade(fp_rate),
                severity_recommendation="lower-or-add-context" if fp_rate >= 0.5 else ("add-allowlist-context" if fp_rate > 0 else "keep"),
                false_positive_examples=false_positive_examples,
            )
        )
    return evaluations


def build_summary(evaluations: list[Evaluation], suggestions: list[Suggestion]) -> dict:
    """Return dashboard-friendly tuning summary."""
    total_alerts = sum(item.alerts for item in evaluations)
    total_false_positives = sum(item.false_positives for item in evaluations)
    return {
        "rules_with_alerts": len(evaluations),
        "total_alerts": total_alerts,
        "total_true_positives": sum(item.true_positives for item in evaluations),
        "total_false_positives": total_false_positives,
        "overall_false_positive_rate": round(total_false_positives / total_alerts, 3) if total_alerts else 0.0,
        "suggestions": len(suggestions),
        "noisy_rules": [item.rule_id for item in evaluations if item.noise_grade != "clean"],
    }


def build_tuning_plan(evaluations: list[Evaluation], suggestions: list[Suggestion]) -> list[dict]:
    """Return prioritized tuning plan rows."""
    suggestion_by_rule = {suggestion.rule_id: suggestion for suggestion in suggestions}
    order = {"noisy": 3, "needs-tuning": 2, "clean": 1}
    rows = []
    for item in sorted(evaluations, key=lambda evaluation: (-order[evaluation.noise_grade], -evaluation.false_positive_rate, evaluation.rule_id)):
        suggestion = suggestion_by_rule.get(item.rule_id)
        rows.append(
            {
                "rule_id": item.rule_id,
                "noise_grade": item.noise_grade,
                "false_positive_rate": item.false_positive_rate,
                "precision": item.precision,
                "severity_recommendation": item.severity_recommendation,
                "action": suggestion.message if suggestion else "No tuning needed.",
            }
        )
    return rows


def build_report(evaluations: list[Evaluation], suggestions: list[Suggestion]) -> str:
    summary = build_summary(evaluations, suggestions)
    tuning_plan = build_tuning_plan(evaluations, suggestions)
    lines = [
        "# Rule Tuning Report",
        "",
        f"- Rules with alerts: {summary['rules_with_alerts']}",
        f"- Total alerts: {summary['total_alerts']}",
        f"- False positives: {summary['total_false_positives']}",
        f"- Overall false positive rate: {summary['overall_false_positive_rate']}",
        "",
        "## Priority Tuning Plan",
        "",
    ]
    for row in tuning_plan:
        lines.append(
            f"- `{row['rule_id']}`: {row['noise_grade']}, fp_rate={row['false_positive_rate']}, action={row['action']}"
        )
    lines.append("")
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
                f"- Precision: {item.precision}",
                f"- Noise grade: `{item.noise_grade}`",
                f"- Severity recommendation: `{item.severity_recommendation}`",
                "",
            ]
        )
        if item.false_positive_examples:
            lines.append("False positive examples:")
            lines.extend([f"- `{example}`" for example in item.false_positive_examples])
            lines.append("")
    lines.extend(["## Suggestions", ""])
    for suggestion in suggestions or [Suggestion("none", "No tuning needed", "info")]:
        lines.append(f"- **{suggestion.severity}** `{suggestion.rule_id}`: {suggestion.message}")
    return "\n".join(lines).rstrip() + "\n"


def build_triage_report(summary: dict, tuning_plan: list[dict]) -> str:
    """Return compact tuning triage report."""
    lines = [
        "# Rule Tuning Triage",
        "",
        f"- Total alerts: {summary['total_alerts']}",
        f"- Overall false positive rate: {summary['overall_false_positive_rate']}",
        f"- Noisy rules: {', '.join(summary['noisy_rules']) if summary['noisy_rules'] else 'none'}",
        "",
        "## Analyst Queue",
        "",
    ]
    if not tuning_plan:
        lines.append("- No tuning actions generated.")
    for row in tuning_plan:
        lines.append(f"- `{row['rule_id']}`: {row['noise_grade']} - {row['action']}")
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate detection rules against labeled sample logs")
    parser.add_argument("--rules", nargs="+", type=Path, default=sorted(Path("rules").glob("*.yaml")))
    parser.add_argument("--logs", nargs="+", type=Path, default=[Path("data/noisy-alerts.log"), Path("data/clean-alerts.log")])
    parser.add_argument("--out", type=Path, default=Path("reports/tuning-report.md"))
    parser.add_argument("--json-out", type=Path, default=Path("reports/evaluation.json"))
    parser.add_argument("--summary-out", type=Path, default=Path("reports/summary.json"))
    parser.add_argument("--plan-out", type=Path, default=Path("reports/tuning-plan.json"))
    parser.add_argument("--triage-out", type=Path, default=Path("reports/triage.md"))
    args = parser.parse_args()

    alerts = run_rules(load_lines(args.logs), load_rules(args.rules))
    evaluations = evaluate_alerts(alerts)
    suggestions = build_suggestions(evaluations)
    summary = build_summary(evaluations, suggestions)
    tuning_plan = build_tuning_plan(evaluations, suggestions)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(build_report(evaluations, suggestions), encoding="utf-8")
    args.json_out.write_text(json.dumps([asdict(item) for item in evaluations], indent=2) + "\n", encoding="utf-8")
    args.summary_out.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    args.plan_out.write_text(json.dumps(tuning_plan, indent=2) + "\n", encoding="utf-8")
    args.triage_out.write_text(build_triage_report(summary, tuning_plan), encoding="utf-8")
    print(f"Evaluated {len(evaluations)} noisy rule(s)")
    print(f"Generated {len(suggestions)} tuning suggestion(s)")


if __name__ == "__main__":
    main()
