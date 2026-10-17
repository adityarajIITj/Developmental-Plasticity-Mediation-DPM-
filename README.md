# Developmental Plasticity Mediation (DPM)

**Research scaffold for a causal-explanatory framework of functional affect in artificial systems.**

DPM proposes studying whether a history-conditioned mediator changes how later evidence updates learned significance. The repository is currently an initial project scaffold; it does not yet contain a complete implementation or experimental results.

## Research question

Can a history-conditioned mediator explain and predict changes in how an artificial system learns from later evidence, beyond persistent-state adaptive control and strong generic meta-learning baselines?

## Conceptual schema

`P_{t+1} = H(P_t, J_{t+1}, B_t, Z_t, C_t)`

`Z_{t+1} = F_{P_t}(Z_t, \epsilon_{t+1}, B_t, C_t)`

`A_t \sim \pi(\cdot \mid B_t, Z_t, P_t, C_t)`

- `P`: history-conditioned plasticity/development mediator.
- `Z`: learned significance.
- `B`: explicit belief.
- `J`: episode/history input.
- `ε`: learning evidence; not assumed to be a temporal-difference error.
- `C`: context.
- `A`: action.

These equations are a conceptual schema, not an executable algorithm. Implementation details must be specified before experiments are treated as confirmatory.

## Initial technology choices

- **C++20** for the native research core.
- **CMake** for portable builds.
- **CTest** for the initial native test target.
- Python may be added later for statistical analysis and visualization; it is not the core engine.

## Proposed study

The planned Plasticity Clamp and Transfer Test compares:
1. A persistent-state adaptive controller.
2. An evaluative-decoupling variant.
3. A DPM-style mediator that modulates learning updates.
4. A strong generic meta-learning baseline.

The study should match task exposure, computational budget, model capacity where feasible, and evaluation opportunities. It should assess controlled evidence-response changes, retention/extinction, cross-context transfer, held-out interventional prediction, and model complexity.

## Current status

- [x] Research overview and theoretical boundaries documented.
- [x] Initial C++20/CMake project scaffold added.
- [x] Basic build and scaffold-test entry points added.
- [ ] Formal model update rules specified for each baseline.
- [ ] Baselines implemented.
- [ ] Intervention and transfer tests implemented.
- [ ] Experiments run and results reported.

No experimental results are claimed at this stage. The current repository milestone is complete as an initial scaffold; it is not yet a practical model or a validated research implementation.

## Development note

The next phase is intentionally deferred. Building a practical DPM model requires careful specification of the model dynamics, intervention semantics, comparison baselines, and evaluation protocol; it is a substantial research and engineering effort, not a small extension to the paper. Until that work begins, this repository should remain a clean, honest scaffold. No extra modules, placeholder experiments, or claimed results are needed merely to make the repository look larger.

## Scientific boundaries

- Functional affect is not equated with subjective experience.
- Reward, prediction error, persistence, and action bias are not individually sufficient evidence of emotion.
- DPM is not claimed to be a new low-level computational primitive.
- A generic meta-learning model matching DPM at equal or lower complexity would weaken the case for distinct explanatory value.
- Null results and counterexamples should be reported alongside positive findings.

## Layout

- `src/dpm/`: native core API and implementation.
- `tests/`: initial C++ test target.
- `experiments/`: reserved for reproducible experiment drivers.
- `configs/`: draft protocol configuration.
- `docs/`: theory notes and limitations.
- `results/`: generated outputs only; never manually fabricate results.

## Developer documentation

- [Build and test guide](docs/build-and-test.md): local prerequisites and commands.
- [Core API contract](docs/core-api.md): what the current native interface does—and does not—promise.
- [Experiment configuration conventions](docs/experiment-config.md): rules for future reproducible runs.
- [Results and reporting policy](docs/results-policy.md): provenance and reporting requirements.
- [Current limitations](docs/limitations.md): implementation gaps and inference boundaries.
- [Theory notes](docs/theory-notes.md): operational distinction and model-comparison rationale.
- [Notation reference](docs/notation.md): symbols and their current implementation status.
- [Baseline comparison](docs/baseline-comparison.md): matching requirements for fair comparisons.
- [Intervention design](docs/intervention-design.md): mediator-clamp semantics to define before implementation.
- [Reproducibility checklist](docs/reproducibility.md): provenance requirements for future runs.
- [Testing scope](docs/testing-scope.md): software checks versus scientific evaluation.
- [Research roadmap](docs/roadmap.md): staged work and explicit current status.

## Build

```bash
cmake -S . -B build
cmake --build build
ctest --test-dir build --output-on-failure
```

## Citation and status

Cite the manuscript using the title and author details from the submitted version until a public bibliographic record is available. Submission does not imply acceptance or publication.

## License

See [LICENSE](LICENSE) for the repository's current terms.
