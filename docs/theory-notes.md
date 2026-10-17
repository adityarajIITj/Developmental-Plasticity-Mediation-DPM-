# DPM theory notes

This document records the central definitions needed to translate the theory into testable models. It is not a substitute for the submitted manuscript.

## Operational distinction

DPM's target is not merely a persistent state that changes current inference or action. The candidate mediator must causally change how later evidence affects learned significance.

For a selected measurable function (g), define a controlled evidence-response contrast:

[
\Delta_g(p; e_1,e_0 \mid z,b,c) =
\mathbb{E}[g(Z_{t+1}) \mid do(P_t=p), do(\epsilon_{t+1}=e_1), z,b,c]
-
\mathbb{E}[g(Z_{t+1}) \mid do(P_t=p), do(\epsilon_{t+1}=e_0), z,b,c].
]

Evidence-response mediation is present when controlled contrasts differ across mediator settings, for example (\Delta_g(p_1) \ne \Delta_g(p_0)), under a well-defined intervention and appropriate control of off-target paths.

This criterion distinguishes DPM from a restricted persistence-only model; it does not distinguish DPM from every possible meta-learning controller.

## Model comparison

Any fully specified DPM implementation can be represented as an ordinary adaptive controller whose augmented state includes (P). Therefore, a new computational primitive is not implied by introducing the DPM vocabulary.

DPM's explanatory value must be assessed empirically against strong matched baselines, including generic meta-learning. If competing models make indistinguishable predictions for every intervention in the test set, prediction alone cannot identify a uniquely correct explanatory vocabulary.

## Required protocol details before implementation

- Explicit state and action spaces.
- Exact transition and learning-update equations for every model.
- Controlled intervention definition for the mediator.
- A priori task families, random seeds, train/test splits, metrics, and compute budget.
- Matching rules for capacity and data exposure.
- Failure criteria and null-result reporting.
- Versioned configuration files and reproducible result generation.

Do not report empirical conclusions until the protocol is implemented and executed.
