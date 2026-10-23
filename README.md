# Developmental Plasticity Mediation (DPM)

**An open research scaffold for testing a causal-explanatory account of functional affect in artificial systems.**

DPM asks whether a history-conditioned internal mediator can change how later evidence updates learned significance. The repository is an early C++20 scaffold for making that question precise and testable. It is **not yet a working affect model**, and it contains no empirical results.

[Research status](#status) · [Build](#build-and-test) · [Scientific question](#research-question) · [Contributing](CONTRIBUTING.md)

---

## Research question

Can a history-conditioned mediator explain or predict how an artificial system learns from later evidence, beyond what is explained by persistent-state adaptive control or a strong generic meta-learning system?

The intended distinction is causal: the proposed mediator should alter the *evidence-to-learning relationship*, not merely persist and bias the system's current inference or action. This is a hypothesis to test, not a result established by the repository.

## Conceptual schema

The current theoretical sketch is:

```text
P[t+1] = H(P[t], J[t+1], B[t], Z[t], C[t])
Z[t+1] = F_{P[t]}(Z[t], epsilon[t+1], B[t], C[t])
A[t]   ~ pi(. | B[t], Z[t], P[t], C[t])
```

| Symbol | Intended role |
|---|---|
| `P` | History-conditioned plasticity/development mediator |
| `Z` | Learned significance |
| `B` | Explicit belief |
| `J` | Episode/history input |
| `epsilon` | Learning evidence; not assumed to be a temporal-difference error |
| `C` | Context |
| `A` | Action |

These equations are a **conceptual schema**, not a complete algorithm. They do not specify state spaces, update rules, parameterization, or intervention mechanics. Those choices must be written down before an implementation can be evaluated scientifically.

## Proposed empirical test

The planned *Plasticity Clamp and Transfer Test* is intended to compare:

1. A persistent-state adaptive controller.
2. An evaluative-decoupling variant.
3. A DPM-style mediator that modulates learning updates.
4. A strong generic meta-learning baseline.

A credible comparison needs explicit update equations, comparable information and data exposure, a defensible capacity/tuning budget, controlled mediator interventions, held-out contexts, and predeclared metrics. The proposed outcomes include evidence-response contrasts, retention/extinction, cross-context transfer, held-out interventional prediction error, and model complexity.

A generic meta-learning baseline that matches DPM at equal or lower complexity would weaken the claim that DPM adds distinct explanatory value.

## Status

**Current milestone: repository scaffold and research-planning documentation.**

- [x] Initial C++20/CMake project and CTest entry point.
- [x] Basic scaffold test and native build workflow.
- [x] Draft protocol configuration and documentation of scientific boundaries.
- [x] Planning guides for model specification, interventions, metrics, and reproducibility.
- [ ] Specify complete update rules for every model variant.
- [ ] Finalize the intervention protocol and metric estimators.
- [ ] Implement model variants and a configuration-consuming experiment runner.
- [ ] Add model-level, intervention, and reproducibility tests.
- [ ] Run matched experiments and report results.

The checked items describe repository artifacts, not validation of the theory. No empirical results are claimed. A successful build or scaffold test establishes only that the tested software path works.

## Scientific boundaries

- Functional organization is not evidence by itself of subjective feeling or phenomenal valence.
- Reward, prediction error, persistence, and action bias alone are insufficient to establish emotion.
- DPM is not claimed to introduce a new low-level computational primitive.
- Generic adaptive control and meta-learning are serious competing explanations, not straw-man baselines.
- Null results, failed runs, alternative explanations, and limitations should be reported alongside positive findings.

## Repository map

```text
src/dpm/                  Minimal native C++ scaffold
tests/                    Current test and planned test requirements
configs/protocol.yaml     Draft settings; not consumed by a runner yet
docs/                     Theory, protocol, and research-governance notes
scripts/                  Repository validation utilities
.github/workflows/        Build/test and repository checks
results/                  Reserved for generated outputs; no fabricated results
```

Useful guides:

- [Build and test](docs/build-and-test.md)
- [Repository architecture](docs/architecture.md)
- [Protocol validator](docs/protocol-validator.md): structural checks and their limits.
- [Validation matrix](docs/validation-matrix.md): accepted and rejected protocol cases covered by tests.
- [Core API contract](docs/core-api.md)
- [Theory notes](docs/theory-notes.md)
- [Notation reference](docs/notation.md)
- [Model specification template](docs/model-spec-template.md)
- [Intervention design](docs/intervention-design.md)
- [Metric definitions](docs/metric-definitions.md)
- [Baseline comparison](docs/baseline-comparison.md)
- [Reproducibility checklist](docs/reproducibility.md)
- [Threats to validity](docs/threats-to-validity.md)
- [Research roadmap](docs/roadmap.md)
- [Current limitations](docs/limitations.md)
- [Contributing](CONTRIBUTING.md): review standards for code and research changes.
- [Research claim ledger](docs/research-claim-ledger.md)

## Build and test

Requirements: CMake 3.20+, a C++20 compiler, and a supported build tool.

```sh
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build --parallel
ctest --test-dir build --output-on-failure
```

The current CTest target checks the scaffold API only. It does not exercise learning dynamics, mediator interventions, affect, or any scientific proposition. See [the testing-scope note](docs/testing-scope.md).

For the draft protocol's structural checks, install the development dependency and run:

```sh
python -m pip install -r requirements-dev.txt
make protocol-check
make protocol-test
```

These checks reject malformed configuration and common structural mistakes; they do not determine whether the proposed experimental design is scientifically adequate. See the [protocol validator guide](docs/protocol-validator.md).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Changes to model semantics should include a specification, tests, and an explanation of how previous results remain comparable.

## Citation and license

The manuscript is titled *Developmental Plasticity Mediation: A Causal-Explanatory Framework for Functional Affect in Artificial Systems*. Use the manuscript's submitted bibliographic details until a public record is available; submission does not imply acceptance or publication.

See [CITATION.cff](CITATION.cff) and [LICENSE](LICENSE) for citation metadata and repository terms.
