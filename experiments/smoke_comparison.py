"""Run a small deterministic smoke comparison; not confirmatory evidence."""
from __future__ import annotations

import csv
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from dpm.models import DPMMediator, EvaluativeDecoupling, GenericMetaLearning, PersistenceOnly


def run():
    sequence = [1.0] * 10 + [-1.0] * 10 + [0.5] * 10
    models = [
        PersistenceOnly(),
        EvaluativeDecoupling(),
        DPMMediator(mediator=1.0),
        GenericMetaLearning(),
    ]
    rows = []
    for model in models:
        for t, evidence in enumerate(sequence):
            significance = model.observe(evidence)
            rows.append({
                "model": model.name,
                "step": t,
                "evidence": evidence,
                "significance": significance,
                "action_score": model.action_score(),
            })
    out = Path("results/smoke_comparison.csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} trajectory rows to {out}")
    print("SMOKE TEST ONLY: this run is not a matched experiment or evidence for DPM.")


if __name__ == "__main__":
    run()
