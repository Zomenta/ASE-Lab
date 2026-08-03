# EXPERIMENT_001.md

# ASE Laboratory — Experiment 001
## Adaptive Balance and Survival

**Version:** 1.0  
**Status:** Phase 1 Experiment Draft

---

# Purpose

This is the first canonical AST experiment.

Its purpose is to test whether adaptive balance predicts survival in a noisy resource environment.

---

# Research Question

Does higher adaptive balance predict longer survival?

---

# Hypothesis

If AST is useful, then runs with higher average adaptive balance should survive longer on average.

---

# Null Hypothesis

Adaptive balance does not predict survival better than chance or than a simpler baseline.

---

# Environment

Use the Phase 1 toy world.

The environment should include:

- one resource pool
- stochastic disturbances
- resource regeneration
- one agent
- action costs
- viability threshold

---

# Conditions

At minimum, compare these conditions:

- random policy
- greedy policy
- threshold policy
- memory on
- memory off
- timescale term on
- timescale term off

---

# Required Metrics

Collect:

- survival time
- exit time
- viability
- adaptive balance
- pressure
- capacity
- cost
- timescale ratio
- memory quality

---

# Procedure

1. Set a fixed seed list.
2. Run multiple simulations per condition.
3. Log per-step data.
4. Save run summaries.
5. Compare mean survival and distribution of outcomes.
6. Compare against baseline policies.
7. Repeat with ablations.

---

# Output Files

The experiment should generate:

- `results.csv`
- `metadata.json`
- `summary.md`
- optional plots

---

# Success Criteria

The experiment is useful if at least one of the following occurs:

- adaptive balance predicts survival better than baseline,
- memory improves survival or forecast quality,
- timescale ratio affects viability,
- one AST component is shown to matter.

---

# Failure Criteria

The experiment is also useful if:

- adaptive balance does not predict survival,
- memory has no measurable effect,
- timescale ratio does not matter,
- AST performs no better than simpler baselines.

A clear negative result is still valuable.

---

# Interpretation Rule

Do not treat one run as evidence.

Use repeated trials and compare across conditions.

---

# Final Note

Experiment 001 is not about proving the theory.

It is about determining whether the theory is worth refining.
