"""Minimal learning-update models for testing evidence-response mediation.

The models are deliberately small and transparent. They implement a scalar
toy problem so that intervention semantics can be unit-tested before any
larger environment or affect-related interpretation is introduced.
"""
from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class LearnerState:
    """State for a scalar significance-learning task."""

    significance: float = 0.0

    def __post_init__(self) -> None:
        if not math.isfinite(self.significance):
            raise ValueError("significance must be finite")


@dataclass(frozen=True)
class FixedRateLearner:
    """Persistence-only comparison with a fixed evidence update rate."""

    learning_rate: float = 0.25

    def __post_init__(self) -> None:
        _validate_rate(self.learning_rate, "learning_rate")

    def update(self, state: LearnerState, evidence: float) -> LearnerState:
        _validate_finite(evidence, "evidence")
        next_value = state.significance + self.learning_rate * (
            evidence - state.significance
        )
        return LearnerState(next_value)


@dataclass(frozen=True)
class MediatedLearner:
    """Toy DPM-style update where an intervention on P changes evidence gain.

    effective_rate = base_rate * (1 + mediator_sensitivity * P)

    P is clamped to [0, 1]. This is an explicit illustrative mechanism, not
    claimed to be the uniquely correct DPM equation or an emotion mechanism.
    """

    base_rate: float = 0.1
    mediator_sensitivity: float = 2.0

    def __post_init__(self) -> None:
        _validate_rate(self.base_rate, "base_rate")
        _validate_finite(self.mediator_sensitivity, "mediator_sensitivity")
        if self.mediator_sensitivity < 0:
            raise ValueError("mediator_sensitivity must be non-negative")
        if self.base_rate * (1.0 + self.mediator_sensitivity) > 1.0:
            raise ValueError("maximum effective learning rate must not exceed 1")

    def effective_rate(self, mediator: float) -> float:
        _validate_finite(mediator, "mediator")
        if not 0.0 <= mediator <= 1.0:
            raise ValueError("mediator must be in [0, 1]")
        return self.base_rate * (1.0 + self.mediator_sensitivity * mediator)

    def update(
        self, state: LearnerState, evidence: float, *, mediator: float
    ) -> LearnerState:
        _validate_finite(evidence, "evidence")
        rate = self.effective_rate(mediator)
        next_value = state.significance + rate * (evidence - state.significance)
        return LearnerState(next_value)


def _validate_rate(value: float, name: str) -> None:
    _validate_finite(value, name)
    if not 0.0 <= value <= 1.0:
        raise ValueError(f"{name} must be in [0, 1]")


def _validate_finite(value: float, name: str) -> None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be a number")
    if not math.isfinite(value):
        raise ValueError(f"{name} must be finite")
