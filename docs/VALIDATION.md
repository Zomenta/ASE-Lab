# VALIDATION.md

# ASE Laboratory — Validation and Falsification
## AST Phase 1 and Beyond

**Version:** 1.0  
**Status:** Phase 1 Support File

---

# Purpose

This document defines how Adaptive State Theory can fail.

A scientific theory is only useful if it can be wrong in a clear and testable way.

---

# Validation Principle

AST should be validated against competing baselines and rejected if it does not outperform them on the claims it makes.

Validation is not a reward ceremony.

Validation is a controlled attempt to break the theory.

---

# What AST Must Demonstrate

At minimum, AST should be able to show that its core quantities are not decorative.

The theory should provide measurable value for at least some of the following:

- viability
- adaptive balance
- capacity
- pressure
- memory quality
- cost
- timescale ratio
- identity thresholding

If these quantities do not improve prediction or interpretation, AST needs revision.

---

# Core Falsifiable Claims

## Claim 1 — Balance matters

Higher adaptive balance should predict longer survival in comparable conditions.

### Failure condition
No meaningful relationship appears after controlling for confounds.

---

## Claim 2 — Memory matters

Memory should improve future viability, or reduce future search cost, in at least some environments.

### Failure condition
Memory never improves outcome, or only adds cost without benefit.

---

## Claim 3 — Timescale matters

Better matching between environmental timescale and adaptive timescale should improve viability.

### Failure condition
Timescale ratio has no measurable effect.

---

## Claim 4 — Cost matters

Adaptive action should not be free.

### Failure condition
Cost does not affect viability, survival, or behavior in any meaningful way.

---

## Claim 5 — Capacity matters

Systems with higher capacity should tolerate stronger perturbations.

### Failure condition
Capacity does not predict resilience or survivability.

---

## Claim 6 — Identity should be stable enough to classify

Identity thresholds should classify functionally equivalent systems in a consistent way.

### Failure condition
Identity becomes arbitrary or unstable across equivalent cases.

---

# Null Hypotheses

When testing AST, the following null hypotheses should be considered:

- adaptive balance does not predict survival,
- memory does not improve viability,
- timescale ratio does not matter,
- cost does not influence adaptive behavior,
- capacity does not improve robustness,
- identity classification is not reliable.

These are legitimate scientific starting points.

---

# Baseline Comparisons

AST must be compared against simpler alternatives.

Recommended baselines:

- random policy
- greedy policy
- threshold controller
- survival model without memory
- survival model without timescale
- survival model without cost
- simple resilience model
- simple control model

If AST performs no better than a simpler baseline, the simpler baseline should be preferred.

---

# Validation Levels

AST should be validated in stages.

## Level 1 — Metric validity
Do the metrics measure what they claim to measure?

## Level 2 — Predictive validity
Do the metrics predict the outcome better than chance or baseline?

## Level 3 — Structural validity
Do the metrics behave consistently across conditions?

## Level 4 — Cross-condition validity
Do the same relationships survive in multiple toy environments?

## Level 5 — Cross-domain validity
Do the relationships transfer to broader domains?

Higher levels should not be claimed before lower levels are satisfied.

---

# Failure Modes

Possible failure modes include:

- circular definitions,
- metrics that cannot be computed,
- metrics that are too noisy,
- results that depend entirely on arbitrary thresholds,
- equations that fit one toy world but fail in another,
- hidden dependence on implementation details,
- claims that survive only by changing definitions after the fact.

If any of these occur, the theory or implementation should be revised.

---

# Acceptance Criteria

AST should only be considered validated in a limited sense if:

- it predicts outcomes better than baseline models,
- its metrics are reproducible,
- its results persist across seeds,
- its claims survive ablation studies,
- and its measurements are stable enough to compare across conditions.

---

# Disconfirmation Criteria

AST should be treated as disconfirmed or at least weakened if:

- key metrics do not predict outcomes,
- memory does not matter,
- pressure and capacity are not useful distinctions,
- timescale has no effect,
- or the theory cannot be operationalized without ambiguity.

A theory that cannot be tested is not yet a scientific theory.

---

# Validation Workflow

1. Define the claim.
2. Choose the baseline.
3. Specify the metric.
4. Run the simulation.
5. Collect repeated trials.
6. Compare against baseline.
7. Check effect size and consistency.
8. Record whether the claim survives.

---

# Interpretation Rule

A result should be interpreted conservatively.

A positive result means:

- the theory may be useful,
- the metric may be meaningful,
- the model may be worth refining.

A negative result means:

- the theory is incomplete,
- the model may be wrong,
- or the metric may need redesign.

Negative results are progress if they are clear.

---

# Final Requirement

Validation is not about protecting AST.

Validation is about finding the boundary between what AST can explain and what it cannot.
