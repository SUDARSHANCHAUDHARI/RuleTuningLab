"""Simple rule engine for tuning detection rules."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Rule:
    rule_id: str
    description: str
    severity: str
    contains: list[str]


@dataclass(frozen=True)
class Alert:
    rule_id: str
    severity: str
    line: str
    expected_alert: bool


def load_rules(paths: list[Path]) -> list[Rule]:
    rules: list[Rule] = []
    for path in paths:
        current: dict[str, object] | None = None
        for raw_line in path.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or line == "items:":
                continue
            if line.startswith("- id:"):
                if current:
                    rules.append(_rule_from_dict(current))
                current = {"id": line.split(":", 1)[1].strip(), "contains": []}
            elif current is not None and line.startswith("description:"):
                current["description"] = line.split(":", 1)[1].strip()
            elif current is not None and line.startswith("severity:"):
                current["severity"] = line.split(":", 1)[1].strip()
            elif current is not None and line.startswith("- "):
                patterns = current.setdefault("contains", [])
                assert isinstance(patterns, list)
                patterns.append(line[2:].strip().strip('"').lower())
        if current:
            rules.append(_rule_from_dict(current))
    return rules


def _rule_from_dict(data: dict[str, object]) -> Rule:
    return Rule(
        rule_id=str(data["id"]),
        description=str(data.get("description", data["id"])),
        severity=str(data.get("severity", "medium")),
        contains=[str(item) for item in data.get("contains", [])],
    )


def expected_alert(line: str) -> bool:
    return "expected=true" in line.lower()


def run_rules(lines: list[str], rules: list[Rule]) -> list[Alert]:
    alerts: list[Alert] = []
    for line in lines:
        lower = line.lower()
        for rule in rules:
            if all(pattern in lower for pattern in rule.contains):
                alerts.append(Alert(rule.rule_id, rule.severity, line, expected_alert(line)))
    return alerts
