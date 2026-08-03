# EXPERIMENT_PROTOCOL.md

# ASE Laboratory — Experimental Protocol
## AST Phase 1 and Beyond

**Version:** 1.0  
**Status:** Phase 1 Support File

---

# Purpose

This document defines how AST experiments should be run, recorded, and compared.

It standardizes the experimental workflow so results are reproducible and scientifically meaningful.

---

# Experimental Principles

Every experiment should obey the following rules:

- one scientific question per experiment,
- one primary outcome variable,
- fixed random seed support,
- explicit baseline comparison,
- repeatable configuration,
- logged outputs,
- and documented interpretation.

---

# Experimental Unit

The basic experimental unit is a single simulation run.

A run consists of:

- one environment configuration,
- one policy,
- one random seed,
- one parameter set,
- one time horizon.

---

# Required Experiment Metadata

Every experiment should store:

- experiment name
- date
- repository version or commit hash
- environment type
- policy type
- seed
- horizon
- parameter values
- metrics collected
- notes on special behavior

---

# Core Metrics

At minimum, experiments should record:

- viability
- survival time
- exit time
- pressure
- capacity
- cost
- adaptive balance
- memory quality
- timescale ratio

If a metric is not collected, the experiment report should say so explicitly.

---

# Baselines

Every test of AST should include at least one baseline.

Recommended baselines:

- random policy
- greedy policy
- threshold policy
- no-memory policy
- no-timescale model
- no-cost model

The point of the baseline is not to win. The point is to make the AST claim measurable.

---

# Experimental Workflow

## Step 1 — Define the question

Example:

Does higher adaptive balance predict longer survival?

## Step 2 — Choose a toy environment

Example:

A resource world with regeneration and stochastic disturbance.

## Step 3 — Choose policies

Example:

- random
- greedy
- threshold

## Step 4 — Fix parameters

Parameters should be written down before running the experiment.

## Step 5 — Run multiple seeds

A single run is not evidence. Use a seed set.

## Step 6 — Log outputs

Record raw run data and summary metrics.

## Step 7 — Compare results

Compare AST-based models to baseline models.

## Step 8 — Interpret carefully

Do not claim a theory is confirmed by one promising run.

---

# Recommended Seed Policy

Use a fixed list of seeds for reproducibility.

Example:

```text
[1, 2, 3, 4, 5, 42, 99, 123, 256, 512]
```

The exact list may be changed, but once chosen it should be recorded in the experiment output.

---

# Logging Protocol

Each run should produce:

- per-step log records
- one summary record
- one machine-readable file

Recommended format:

- CSV for step logs
- JSON for run metadata
- optional plots for visualization

---

# Analysis Protocol

At minimum, analysis should compute:

- mean viability
- mean survival time
- distribution of exit times
- mean cost
- mean pressure
- mean capacity
- effect sizes versus baseline
- seed-to-seed variation

If the experiment uses multiple conditions, compare them consistently.

---

# Statistical Caution

Do not overclaim.

A small toy experiment can show:

- a trend,
- a failure mode,
- a plausible direction,
- or a useful null result.

It does not by itself establish a universal law.

---

# Experimental Conditions

A condition is a fixed combination of:

- environment parameters
- agent policy
- memory configuration
- cost configuration
- timescale configuration

Each condition should be clearly named.

Example names:

- baseline_random
- baseline_greedy
- baseline_threshold
- ast_memory_on
- ast_memory_off
- ast_timescale_on
- ast_timescale_off

---

# Ablation Studies

Ablation is required for AST development.

Ablations should test what happens when one AST component is removed.

Recommended ablations:

- remove memory
- remove timescale term
- remove cost term
- remove pressure term
- remove viability threshold variation

The aim is to determine which components actually matter.

---

# Failure Criteria

An experiment should be considered informative even when the result is negative.

Examples of valid negative results:

- capacity does not predict survival,
- memory adds no improvement,
- timescale matching has no effect,
- cooperation fails to outperform baseline,
- a model is less useful than a simpler alternative.

Negative results are scientifically valuable.

---

# Reporting Format

Every completed experiment should have a short report containing:

- question
- setup
- parameters
- baselines
- metrics
- main result
- limitations
- interpretation
- next experiment

---

# Reproducibility Requirements

The experiment must be reproducible from the repository alone.

That means the repo should contain:

- the code,
- the parameter configuration,
- the seed list,
- the analysis script,
- and the summary report.

If one of these is missing, the experiment is incomplete.

---

# Recommended Phase 1 Experiment

The first phase-1 experiment should test one simple claim:

> Does higher adaptive balance predict longer survival in a noisy resource world?

This experiment is small, measurable, and directly tied to the current AST core.

---

# Recommended Output Files

For each experiment, create:

- `results.csv`
- `metadata.json`
- `summary.md`
- optional plots

These files should be generated automatically when possible.

---

# Final Requirement

An experiment is not finished when code runs.

An experiment is finished when the result can be rerun, inspected, and compared against a baseline without ambiguity.
