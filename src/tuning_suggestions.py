"""Build tuning suggestions from rule evaluation metrics."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Suggestion:
    rule_id: str
    message: str
    severity: str


def build_suggestions(evaluations) -> list[Suggestion]:
    suggestions: list[Suggestion] = []
    for item in evaluations:
        if item.false_positive_rate >= 0.5:
            suggestions.append(
                Suggestion(
                    item.rule_id,
                    "Add a second condition, require stronger context, or lower severity until the behavior is confirmed.",
                    "high",
                )
            )
        elif item.false_positives:
            suggestions.append(
                Suggestion(
                    item.rule_id,
                    "Review sample false positives and add an allow-list or environment context condition.",
                    "medium",
                )
            )
    return suggestions
