import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_protocol.py"
VALID_CONFIG = ROOT / "configs" / "protocol.yaml"


class ProtocolValidatorTests(unittest.TestCase):
    def run_validator(self, text=None):
        temporary = None
        try:
            if text is None:
                target = VALID_CONFIG
            else:
                temporary = tempfile.NamedTemporaryFile(
                    mode="w", encoding="utf-8", suffix=".yaml", delete=False
                )
                temporary.write(text)
                temporary.close()
                target = Path(temporary.name)
            return subprocess.run(
                [sys.executable, str(VALIDATOR), str(target)],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
        finally:
            if temporary is not None:
                Path(temporary.name).unlink(missing_ok=True)

    def test_current_draft_is_structurally_valid(self):
        result = self.run_validator()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Protocol structure valid", result.stdout)

    def test_rejects_overlapping_context_splits(self):
        invalid = """seed: 7
episodes:
  train: 10
  evaluation: 5
interventions:
  mediator_clamp:
    enabled: true
    values: [low, high]
splits:
  contexts:
    train: [shared]
    held_out: [shared]
metrics: [retention]
notes: []
"""
        result = self.run_validator(invalid)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("overlap", result.stderr)

    def test_rejects_non_positive_episode_count(self):
        invalid = """seed: 7
episodes:
  train: 0
  evaluation: 5
interventions:
  mediator_clamp:
    enabled: true
    values: [low, high]
splits:
  contexts:
    train: []
    held_out: []
metrics: [retention]
notes: []
"""
        result = self.run_validator(invalid)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("positive integer", result.stderr)


if __name__ == "__main__":
    unittest.main()
