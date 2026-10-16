"""Minimal scalar toy models for the DPM Plasticity Clamp and Transfer Test.

These are deliberately simple reference implementations for checking the
experimental pipeline, not validated models of emotion or evidence of affect.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass
class State:
    significance: float = 0.0
    belief: float = 0.0
    mediator: float = 1.0
    action_bias: float = 0.0


class Model(Protocol):
    name: str
    def observe(self, evidence: float) -> float: ...
    def action_score(self) -> float: ...


@dataclass
class PersistenceOnly:
    """Persistent significance state; evidence update rate is fixed."""
    alpha: float = 0.2
    state: State | None = None
    name: str = "persistence_only"

    def __post_init__(self) -> None:
        self.state = self.state or State()

    def observe(self, evidence: float) -> float:
        assert self.state is not None
        self.state.significance += self.alpha * (evidence - self.state.significance)
        self.state.belief = evidence
        return self.state.significance

    def action_score(self) -> float:
        assert self.state is not None
        return self.state.significance


@dataclass
class EvaluativeDecoupling:
    """Persistent evaluative bias affects action but not evidence learning."""
    alpha: float = 0.2
    bias_decay: float = 0.9
    state: State | None = None
    name: str = "evaluative_decoupling"

    def __post_init__(self) -> None:
        self.state = self.state or State()

    def observe(self, evidence: float) -> float:
        assert self.state is not None
        self.state.significance += self.alpha * (evidence - self.state.significance)
        self.state.belief = evidence
        self.state.action_bias *= self.bias_decay
        return self.state.significance

    def set_evaluative_bias(self, value: float) -> None:
        assert self.state is not None
        self.state.action_bias = value

    def action_score(self) -> float:
        assert self.state is not None
        return self.state.significance + self.state.action_bias


@dataclass
class DPMMediator:
    """Mediator gates the rate at which new evidence updates significance."""
    base_alpha: float = 0.2
    mediator: float = 1.0
    clamp: float | None = None
    state: State | None = None
    name: str = "dpm_mediator"

    def __post_init__(self) -> None:
        self.state = self.state or State(mediator=self.mediator)

    def observe(self, evidence: float) -> float:
        assert self.state is not None
        p = self.clamp if self.clamp is not None else self.state.mediator
        gain = min(1.0, max(0.0, self.base_alpha * p))
        self.state.significance += gain * (evidence - self.state.significance)
        self.state.belief = evidence
        return self.state.significance

    def set_mediator(self, value: float) -> None:
        assert self.state is not None
        self.state.mediator = value

    def set_clamp(self, value: float | None) -> None:
        """Set an intervention value; None releases the clamp."""
        self.clamp = value

    def action_score(self) -> float:
        assert self.state is not None
        return self.state.significance


@dataclass
class GenericMetaLearning:
    """A generic adaptive learning-rate baseline based on recent prediction error.

    This is intentionally only a minimal baseline. It is not a claim to be a
    strong or exhaustive meta-learning implementation; it must be strengthened
    and capacity-matched before confirmatory conclusions.
    """
    alpha: float = 0.2
    min_alpha: float = 0.01
    max_alpha: float = 0.8
    adaptation_rate: float = 0.1
    state: State | None = None
    name: str = "generic_meta_learning"

    def __post_init__(self) -> None:
        self.state = self.state or State()

    def observe(self, evidence: float) -> float:
        assert self.state is not None
        error = evidence - self.state.significance
        self.state.significance += self.alpha * error
        # Adapt future learning rate using prediction-error magnitude.
        target = min(self.max_alpha, max(self.min_alpha, abs(error)))
        self.alpha += self.adaptation_rate * (target - self.alpha)
        self.alpha = min(self.max_alpha, max(self.min_alpha, self.alpha))
        self.state.belief = evidence
        return self.state.significance

    def action_score(self) -> float:
        assert self.state is not None
        return self.state.significance
