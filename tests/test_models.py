import unittest

from dpm.models import (
    DPMMediator,
    EvaluativeDecoupling,
    GenericMetaLearning,
    PersistenceOnly,
)


class TestToyModels(unittest.TestCase):
    def test_persistence_only_fixed_gain(self):
        model = PersistenceOnly(alpha=0.5)
        self.assertAlmostEqual(model.observe(1.0), 0.5)
        self.assertAlmostEqual(model.observe(1.0), 0.75)

    def test_evaluative_bias_changes_action_not_learning_update(self):
        a = EvaluativeDecoupling(alpha=0.5)
        b = EvaluativeDecoupling(alpha=0.5)
        a.set_evaluative_bias(0.0)
        b.set_evaluative_bias(2.0)
        self.assertAlmostEqual(a.observe(1.0), b.observe(1.0))
        self.assertNotAlmostEqual(a.action_score(), b.action_score())

    def test_dpm_clamp_changes_evidence_response(self):
        low = DPMMediator(base_alpha=0.5)
        high = DPMMediator(base_alpha=0.5)
        low.set_clamp(0.2)
        high.set_clamp(1.0)
        low_delta = low.observe(1.0)
        high_delta = high.observe(1.0)
        self.assertAlmostEqual(low_delta, 0.1)
        self.assertAlmostEqual(high_delta, 0.5)
        self.assertNotAlmostEqual(low_delta, high_delta)

    def test_dpm_clamp_release(self):
        model = DPMMediator(base_alpha=0.5, mediator=0.2)
        model.set_clamp(1.0)
        self.assertAlmostEqual(model.observe(1.0), 0.5)
        model.set_clamp(None)
        self.assertAlmostEqual(model.observe(0.0), 0.45)

    def test_meta_learning_alpha_stays_bounded(self):
        model = GenericMetaLearning()
        for evidence in [1.0, -1.0, 0.5, 0.5, 0.0] * 20:
            model.observe(evidence)
        self.assertGreaterEqual(model.alpha, model.min_alpha)
        self.assertLessEqual(model.alpha, model.max_alpha)


if __name__ == "__main__":
    unittest.main()
