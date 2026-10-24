"""Small executable reference components for DPM's operational criterion.

This package is a research prototype, not a validated affect model.
"""
from .models import FixedRateLearner, MediatedLearner, LearnerState
from .metrics import evidence_response_contrast

__all__ = [
    "FixedRateLearner",
    "MediatedLearner",
    "LearnerState",
    "evidence_response_contrast",
]
