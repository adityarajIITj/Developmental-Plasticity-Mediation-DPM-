# Developmental Plasticity Mediation (DPM)

**A research project on history-conditioned learning and functional affect in artificial systems.**

Developmental Plasticity Mediation (DPM) is a candidate causal-organizational framework for studying functional affect. It describes a history-conditioned internal mediator whose intervention changes how later evidence is acquired, retained, extinguished, or transferred into learned significance.

DPM is a research hypothesis and explanatory framework, not a claim that a new computational primitive has been discovered. Its distinct explanatory value must be tested against strong adaptive-control and meta-learning baselines. No result in this repository, by itself, establishes subjective feeling or phenomenal valence.

## Research question

Can a history-conditioned mediator explain and predict changes in how an artificial system learns from later evidence, beyond what is explained by persistent internal state or a strong generic adaptive controller?

## Conceptual model

The paper uses the following conceptual schema:

`P_{t+1} = H(P_t, J_{t+1}, B_t, Z_t, C_t)`

`Z_{t+1} = F_{P_t}(Z_t, \epsilon_{t+1}, B_t, C_t)`

`A_t \sim \pi(\cdot \mid B_t, Z_t, P_t, C_t)`

Where:

- `P` is a history-conditioned plasticity/development mediator.
- `Z` is learned significance.
- `B` is explicit belief.
- `J` is episode/history input.
- `ε` is learning evidence; it is not assumed to be a temporal-difference error.
- `C` is context.
- `A` is action.

These equations are a conceptual schema, not an executable algorithm. A concrete implementation must define its update rules, state spaces, intervention semantics, and evaluation protocol.

## Planned discriminating study

The proposed **Plasticity Clamp and Transfer Test** compares:

1. A persistent-state adaptive controller.
2. An evaluative-decoupling variant.
3. A DPM-style mediator that gates learning updates.
4. A strong generic meta-learning controller.

The comparison should match task exposure, computational budget, model capacity where feasible, and evaluation opportunities. It should assess controlled evidence-response changes, retention and extinction, cross-context transfer, held-out interventional prediction, and model complexity.

The critical question is whether DPM provides predictive or explanatory value beyond a well-matched generic adaptive controller—not whether a system produces human-like emotional labels or expressions.

## Current status

- [x] Research framework and conceptual claims articulated in the accompanying theory paper.
- [ ] Concrete update rules specified for each baseline.
- [ ] Simulation and intervention tests implemented.
- [ ] Tests and reproducibility checks passing.
- [ ] Comparative experiments run and results reported.

Unchecked items are planned work, not completed results. No experimental outcomes are claimed here.

## Scientific boundaries

- Functional affect is not equated with subjective experience.
- Reward, prediction error, persistence, and action bias are not individually sufficient evidence of emotion.
- A successful DPM result would support only the tested causal-functional claim.
- A generic meta-learning model that matches DPM at equal or lower complexity would weaken the case for DPM's distinct explanatory value.
- Null results and counterexamples should be reported alongside positive findings.

## Repository roadmap

- `docs/`: formal definitions, assumptions, and study protocol.
- `src/`: minimal reference implementations, after the update rules are specified.
- `tests/`: unit tests and intervention-invariant checks.
- `experiments/`: reproducible baselines and planned evaluations.
- `configs/`: explicit experiment parameters.
- `results/`: generated results and analysis, never hand-entered as if experimentally obtained.

## Citation

A citation file will be added when the paper's public bibliographic record is available. Until then, cite the manuscript directly using the title and author information printed in the submitted version. Do not infer acceptance or publication status from a preprint or submission.

## License

No license has been selected yet. Until one is added, all rights are reserved by default; do not assume that the code is available for unrestricted reuse.
