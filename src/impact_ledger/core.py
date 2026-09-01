from __future__ import annotations

from dataclasses import dataclass
from statistics import median


@dataclass(frozen=True)
class Event:
    workflow: str
    automated: bool
    accepted: bool
    overridden: bool
    cycle_minutes: float
    error: bool = False


def summarize(events: list[Event]) -> dict[str, float | int]:
    if not events:
        return {
            "events": 0,
            "adoption": 0.0,
            "acceptance": 0.0,
            "override_rate": 0.0,
            "error_rate": 0.0,
            "median_cycle_minutes": 0.0,
        }
    n = len(events)
    automated = sum(e.automated for e in events)
    return {
        "events": n,
        "adoption": round(automated / n, 3),
        "acceptance": round(sum(e.accepted for e in events) / n, 3),
        "override_rate": round(sum(e.overridden for e in events) / n, 3),
        "error_rate": round(sum(e.error for e in events) / n, 3),
        "median_cycle_minutes": median(e.cycle_minutes for e in events),
    }


def compare(baseline: list[Event], current: list[Event]) -> dict[str, float | bool | None]:
    if not baseline or not current:
        return {
            "comparable": False,
            "cycle_minutes_delta": None,
            "acceptance_delta": None,
        }
    b = summarize(baseline)
    c = summarize(current)
    return {
        "comparable": True,
        "cycle_minutes_delta": float(c["median_cycle_minutes"]) - float(b["median_cycle_minutes"]),
        "acceptance_delta": float(c["acceptance"]) - float(b["acceptance"]),
    }
