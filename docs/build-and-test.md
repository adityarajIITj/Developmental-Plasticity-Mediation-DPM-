# Build and test

## Requirements

- CMake 3.20 or newer.
- A C++ compiler with C++20 support.
- A build tool supported by CMake.

The continuous-integration workflow uses Ubuntu and a hosted runner. Local compiler versions may differ, so record the compiler and CMake versions when reporting reproducibility issues.

## Configure, build, and test

```sh
cmake -S . -B build -DCMAKE_BUILD_TYPE=Debug
cmake --build build --parallel
ctest --test-dir build --output-on-failure
```

For a clean reconfiguration, remove the generated `build/` directory and repeat the commands. Do not commit build products.

## Scope of the current test

The current test checks only that the scaffold API is available and returns its expected project-name string. It does not test DPM dynamics, interventions, learning, affect, or the theory's propositions.

A passing build establishes basic compilation and test execution only.


## Repository validation

Install the development dependency before running the protocol checks:

```sh
python -m pip install -r requirements-dev.txt
make protocol-check
make protocol-test
```

The `Makefile` provides shortcuts for the same protocol checks and the CMake/CTest path. If Make is unavailable, run the underlying Python and CMake commands directly. Protocol validation checks structural invariants only; it does not certify scientific readiness.
