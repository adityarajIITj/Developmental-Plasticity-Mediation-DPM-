import math
import unittest

from dpm_reference import (
    FixedRateLearner,
    LearnerState,
    MediatedLearner,
    evidence_response_contrast,
)


class ReferenceModelTests(unittest.TestCase):
    def test_fixed_rate_update_matches_equation(self):
        model = FixedRateLearner(learning_rate=0.25)
        result = model.update(LearnerState(0.0), 1.0)
        self.assertAlmostEqual(result.significance, 0.25)

    def test_mediator_changes_evidence_response_contrast(self):
        model = MediatedLearner(base_rate=0.1, mediator_sensitivity=2.0)
        state = LearnerState(0.2)

        low_contrast = evidence_response_contrast(
            lambda evidence: model.update(
                state, evidence, mediator=0.0
            ).significance,
            evidence_low=0.0,
            evidence_high=1.0,
        )
        high_contrast = evidence_response_contrast(
            lambda evidence: model.update(
                state, evidence, mediator=1.0
            ).significance,
            evidence_low=0.0,
            evidence_high=1.0,
        )

        self.assertAlmostEqual(low_contrast, 0.1)
        self.assertAlmostEqual(high_contrast, 0.3)
        self.assertNotAlmostEqual(low_contrast, high_contrast)

    def test_fixed_rate_model_does_not_depend_on_mediator(self):
        model = FixedRateLearner(learning_rate=0.2)
        state = LearnerState(0.4)
        # FixedRateLearner has no mediator argument by design.
        self.assertAlmostEqual(model.update(state, 1.0).significance, 0.52)

    def test_rejects_mediator_outside_unit_interval(self):
        model = MediatedLearner()
        with self.assertRaises(ValueError):
            model.update(LearnerState(), 1.0, mediator=1.1)

    def test_rejects_non_finite_evidence(self):
        model = MediatedLearner()
        with self.assertRaises(ValueError):
            model.update(LearnerState(), math.inf, mediator=0.5)

    def test_rejects_effective_rate_above_one(self):
        with self.assertRaises(ValueError):
            MediatedLearner(base_rate=0.6, mediator_sensitivity=1.0)


if __name__ == "__main__":
    unittest.main()
