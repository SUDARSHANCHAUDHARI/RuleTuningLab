from pathlib import Path
import unittest

from src.evaluator import build_report, build_summary, build_triage_report, build_tuning_plan, evaluate_alerts, load_lines
from src.rule_engine import load_rules, run_rules
from src.tuning_suggestions import build_suggestions


ROOT = Path(__file__).resolve().parents[1]


class RuleTuningTests(unittest.TestCase):
    def test_evaluates_false_positive_rate(self) -> None:
        rules = load_rules(sorted((ROOT / "rules").glob("*.yaml")))
        alerts = run_rules(load_lines([ROOT / "data/noisy-alerts.log"]), rules)
        evaluations = {item.rule_id: item for item in evaluate_alerts(alerts)}

        self.assertGreater(evaluations["brute-force"].false_positive_rate, 0)
        self.assertEqual("noisy", evaluations["brute-force"].noise_grade)
        self.assertGreater(evaluations["brute-force"].precision, 0)
        self.assertGreater(evaluations["port-scan"].false_positive_rate, 0)

    def test_suggests_tuning_for_noisy_rules(self) -> None:
        rules = load_rules(sorted((ROOT / "rules").glob("*.yaml")))
        evaluations = evaluate_alerts(run_rules(load_lines([ROOT / "data/noisy-alerts.log"]), rules))
        suggestions = build_suggestions(evaluations)

        self.assertTrue(any(item.rule_id == "brute-force" for item in suggestions))

    def test_report_is_markdown(self) -> None:
        self.assertIn("Rule Tuning Report", build_report([], []))

    def test_builds_summary_plan_and_triage(self) -> None:
        rules = load_rules(sorted((ROOT / "rules").glob("*.yaml")))
        evaluations = evaluate_alerts(run_rules(load_lines([ROOT / "data/noisy-alerts.log", ROOT / "data/clean-alerts.log"]), rules))
        suggestions = build_suggestions(evaluations)
        summary = build_summary(evaluations, suggestions)
        plan = build_tuning_plan(evaluations, suggestions)
        triage = build_triage_report(summary, plan)

        self.assertEqual(3, summary["rules_with_alerts"])
        self.assertTrue(any(row["rule_id"] == "brute-force" for row in plan))
        self.assertIn("Rule Tuning Triage", triage)


if __name__ == "__main__":
    unittest.main()
