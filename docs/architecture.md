# Repository architecture

## Current execution path

The current native build is intentionally small:

1. CMake builds `src/dpm/core.cpp` into the `dpm_core` library.
2. The public header `src/dpm/core.hpp` exposes `dpm::CoreScaffold::project_name()`.
3. `tests/test_scaffold.cpp` checks that this identifier matches the expected project name.
4. CTest registers and runs that executable.
5. GitHub Actions configures, builds, and tests the project on an Ubuntu runner.

This path validates basic project wiring only. There is no model state, learning update, policy, environment, intervention implementation, or experiment runner in the current core.

## Intended future separation

The eventual research implementation should keep distinct responsibilities separate:

- **Model:** state representation and update equations for each comparison model.
- **Environment/task:** observations, transitions, evidence, and actions.
- **Intervention:** explicit, logged manipulation of the proposed mediator.
- **Protocol:** configuration validation, split definitions, seeds, and resource limits.
- **Evaluation:** metric estimators, aggregation, uncertainty, and baseline comparisons.
- **Artifacts:** raw run records and analysis outputs linked to a source revision.

These are design boundaries, not claims that those modules already exist. Their interfaces should be chosen only after the model semantics and protocol have been specified.
