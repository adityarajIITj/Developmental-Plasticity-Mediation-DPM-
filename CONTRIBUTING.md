# Contributing

Thank you for helping make DPM more precise, reproducible, and easier to evaluate.

## Before opening a change

- Keep the distinction between implemented behavior, planned work, and empirical findings explicit.
- For model changes, describe the equations and assumptions before or alongside the implementation.
- Prefer a small, reviewable change with a clear purpose over added code that only increases repository size.
- Do not commit fabricated measurements, expected outputs presented as measurements, or results without run provenance.

## Code changes

1. Explain the intended behavior and its research relevance.
2. Add or update tests for changed behavior.
3. Run the CMake build and CTest suite when the native code changes.
4. Keep compiler warnings enabled and address new warnings.
5. Update documentation when the API, protocol, or scientific interpretation changes.

## Protocol and experiment changes

- Record configuration, seed, task/model version, and source commit for every run.
- Keep held-out evaluation data separate from tuning.
- Document intervention timing and possible off-target effects.
- Report failed runs and null results; do not silently omit inconvenient outcomes.
- Distinguish exploratory analyses from confirmatory tests.

## Pull requests

Use the pull-request template. CI success demonstrates only the checks that actually ran; it is not evidence that the DPM theory is correct or that a system has subjective experience.
