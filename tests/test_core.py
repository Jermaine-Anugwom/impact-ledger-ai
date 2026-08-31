import pytest

from impact_ledger.core import Event, compare, summarize


def ev(**kw):
    return Event(
        "intake",
        kw.get("automated", True),
        kw.get("accepted", True),
        kw.get("overridden", False),
        kw.get("cycle_minutes", 5),
        kw.get("error", False),
    )


def test_empty():
    assert summarize([])["events"] == 0


def test_counts():
    assert summarize([ev(), ev()])["events"] == 2


def test_adoption():
    assert summarize([ev(), ev(automated=False)])["adoption"] == 0.5


def test_acceptance():
    assert summarize([ev(), ev(accepted=False)])["acceptance"] == 0.5


def test_override():
    assert summarize([ev(), ev(overridden=True)])["override_rate"] == 0.5


def test_errors():
    assert summarize([ev(), ev(error=True)])["error_rate"] == 0.5


def test_median():
    assert (
        summarize([ev(cycle_minutes=1), ev(cycle_minutes=9), ev(cycle_minutes=5)])[
            "median_cycle_minutes"
        ]
        == 5
    )


@pytest.mark.parametrize("current,delta", [(4, -6), (10, 0), (15, 5)])
def test_cycle_delta(current, delta):
    assert (
        compare([ev(cycle_minutes=10)], [ev(cycle_minutes=current)])["cycle_minutes_delta"] == delta
    )


def test_acceptance_delta():
    assert compare([ev(accepted=False)], [ev(accepted=True)])["acceptance_delta"] == 1


def test_deterministic():
    assert summarize([ev()]) == summarize([ev()])
