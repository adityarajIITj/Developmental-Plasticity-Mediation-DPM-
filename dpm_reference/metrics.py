"""Small metric helpers for the DPM evidence-response criterion."""
from __future__ import annotations

from collections.abc import Callable


def evidence_response_contrast(
    update: Callable[[float], float],
    *,
    initial_significance: float,
    evidence_low: float,
    evidence_high: float,
) -> float:
    """Return outcome(update(high evidence)) - outcome(update(low evidence)).

    The callable should return the next significance for one fixed mediator
    setting. To compare mediator settings, call this function once per setting
    and compare the resulting contrasts. This helper does not itself establish
    causal identification; intervention validity is a design responsibility.
    """
    low = update(evidence_low)
    high = update(evidence_high)
    if not all(isinstance(x, (int, float)) for x in (
        initial_significance, evidence_low, evidence_high, low, high
    )):
        raise ValueError("metric inputs and outputs must be numeric")
    return float(high - low)
