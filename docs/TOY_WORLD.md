# TOY_WORLD.md

# ASE Laboratory — Toy World
## Phase 1 Benchmark Environment

**Version:** 1.0  
**Status:** Phase 1 Support File

---

# Purpose

This file defines the first benchmark environment for Adaptive State Theory.

The toy world should be simple enough to inspect by hand, but rich enough to test viability, pressure, capacity, memory, and cost.

---

# Scientific Goal

The toy world should let us test one simple question:

> Does adaptive balance predict survival in a noisy resource environment?

---

# World Description

The environment contains:

- a single resource pool,
- stochastic disturbances,
- resource regeneration,
- one adaptive agent,
- action costs,
- and a viability threshold.

---

# State Variables

Possible state variables include:

- `resources`
- `disturbance_level`
- `agent_energy`
- `memory_state`
- `time_step`
- `viability`

---

# Environment Dynamics

At each step:

1. resources regenerate,
2. a disturbance may occur,
3. the agent selects an action,
4. the action changes resources or energy,
5. the system updates its state,
6. viability is checked.

---

# Actions

The first toy world should support a small action set.

Example actions:

- `wait`
- `gather`
- `defend`
- `adapt`

The exact meaning may vary, but the action set should remain small.

---

# Viability Condition

A simple viability condition may be:

- the agent survives if energy stays above a threshold,
- or the system survives if resources remain in an acceptable range,
- or both.

The exact threshold should be explicit and fixed for the experiment.

---

# Pressure

Pressure in the toy world comes from:

- disturbances
- scarcity
- environmental noise
- resource loss

Pressure should be measurable as a numeric value.

---

# Capacity

Capacity in the toy world comes from:

- recovery rate
- resilience
- action effectiveness
- memory-assisted adaptation

Capacity should not be treated as a single unexplained magic number.

---

# Memory

Memory should help the agent do at least one of the following:

- predict disturbances better,
- choose better actions,
- reduce search cost,
- recover faster from shocks.

If memory does none of these, the memory metric needs revision.

---

# Cost

Every action should have a cost.

The toy world should never assume free adaptation.

Example costs:

- energy loss
- time loss
- resource consumption

---

# Benchmark Use

This toy world is the first benchmark for AST.

All later environments should be compared against it, not replace it.

---

# Design Rule

The toy world should be the smallest environment that still makes the AST metrics meaningful.
