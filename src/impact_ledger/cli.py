from __future__ import annotations

import json

from .core import Event, summarize


def main() -> None:
    events = [Event("intake", True, True, False, 8.4), Event("intake", True, False, True, 11.1)]
    print(json.dumps({"synthetic": True, "summary": summarize(events)}, indent=2))
