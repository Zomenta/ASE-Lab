# DESIGN.md

# ASE Laboratory — Software Design
## AST Phase 1 Architecture

**Version:** 1.0  
**Status:** Phase 1 Support File

---

# Purpose

This document defines how the Adaptive Systems Engine (ASE) should translate Adaptive State Theory (AST) into software.

It is not a theory document.

It is the architectural bridge between:

- **docs/THEORY.md**
- **docs/MATHEMATICS.md**
- **docs/DEFINITIONS.md**
- **docs/AST_GLOSSARY.md**

and the Python implementation used for simulation and experimentation.

---

# Design Goals

The software must:

- preserve the theory's terminology,
- keep concepts modular,
- support reproducible experiments,
- separate simulation from analysis,
- and remain easy to extend.

The code should never silently redefine the theory.

---

# Core Architectural Rule

Every major AST concept should map to a software concept.

| Theory concept | Software role |
|---|---|
| Adaptive state | Object representing the system's current condition |
| Environment | Source of external conditions and disturbances |
| Policy | Rule that selects actions |
| Memory | Stored state that influences future action |
| Viability | Measured survival / persistence output |
| Pressure | Environmental burden metric |
| Capacity | Adaptive response capability metric |
| Cost | Resource expenditure metric |
| Timescale ratio | Response-speed metric |
| Identity | Classification boundary, not a dynamical variable |

---

# Repository Layout

The Phase 1 implementation should be organized as follows:

```text
core/
agents/
environment/
simulation/
experiments/
tests/
examples/
docs/
```

---

# Module Responsibilities

## 1. core/

The core package contains the theory-neutral software primitives.

Recommended files:

- `state.py`
- `system.py`
- `metrics.py`
- `types.py`

### `state.py`
Stores the current adaptive state, including internal variables, resource values, memory contents, and viability-related fields.

### `system.py`
Defines the adaptive system object and coordinates observation, action, memory update, and state transition.

### `metrics.py`
Implements AST metrics as independent pure functions.

### `types.py`
Contains shared types, aliases, and dataclasses used across the codebase.

---

## 2. agents/

The agents package contains action-selection logic.

Recommended files:

- `base.py`
- `policy.py`
- `memory.py`

### `base.py`
Defines the base agent interface.

### `policy.py`
Contains simple baseline policies such as random, greedy, and threshold policies.

### `memory.py`
Contains memory implementations and memory-quality helpers.

---

## 3. environment/

The environment package models external dynamics.

Recommended files:

- `base.py`
- `toy_world.py`

### `base.py`
Defines the minimal environment interface.

### `toy_world.py`
Implements the first toy environment used for phase 1 experiments.

The first environment should be simple and deterministic enough to debug, but stochastic enough to test viability, pressure, and memory effects.

---

## 4. simulation/

The simulation package runs the time loop.

Recommended files:

- `engine.py`
- `logger.py`

### `engine.py`
Owns the simulation loop, step order, and termination conditions.

### `logger.py`
Records simulation outputs in a structured format.

The logger should support CSV output at minimum.

---

## 5. experiments/

The experiments package contains benchmark runs and ablation studies.

Recommended files:

- `baseline.py`

This package should answer scientific questions, not showcase style.

---

## 6. tests/

The tests package validates correctness and reproducibility.

Tests should cover:

- metric calculations
- state transitions
- policy behavior
- environment updates
- simulation loop execution
- deterministic seeding
- logging output

---

## 7. examples/

The examples package contains small runnable demonstrations.

Recommended file:

- `simple_run.py`

The example should run a minimal simulation and emit a CSV file.

---

# Software Data Flow

The intended flow is:

1. Environment generates the current external condition.
2. Agent observes the state.
3. Policy selects an action.
4. Action affects the system and environment.
5. Memory updates.
6. Metrics are computed.
7. Logger records the result.
8. Simulation advances to the next step.

The implementation should keep this sequence explicit.

---

# Core Object Flow

A minimal AST simulation should use these objects:

- `AdaptiveState`
- `AdaptiveSystem`
- `Environment`
- `Policy`
- `Memory`
- `SimulationEngine`
- `Logger`

The core software should not assume that the agent is biological, artificial, or social. The architecture should remain substrate-neutral.

---

# Proposed Class Roles

## AdaptiveState
Stores the current system state.

Typical fields:

- internal variables
- resource values
- memory state
- viability score
- time index
- flags for termination or failure

## AdaptiveSystem
Coordinates the system as a whole.

Responsibilities:

- observe
- act
- update memory
- update state
- evaluate viability

## Environment
Generates external conditions.

Responsibilities:

- disturbances
- resource regeneration
- pressure generation
- time evolution

## Policy
Chooses actions from observations.

Responsibilities:

- random baseline
- greedy baseline
- threshold baseline
- future custom strategies

## SimulationEngine
Advances the simulation.

Responsibilities:

- step loop
- termination checks
- state bookkeeping
- logging calls

---

# Phase 1 Simulation Scope

The first simulation should be intentionally small.

Recommended initial toy world:

- one resource system
- one agent
- stochastic disturbance
- resource regeneration
- action cost
- viability threshold

That is enough to test the first AST hypotheses.

Do not start with:

- multi-agent society
- learning networks
- evolutionary algorithms
- graphical rendering
- parallel execution
- GPU acceleration

Those belong to later phases.

---

# Logging Requirements

The logger must record:

- time
- state values
- pressure
- capacity
- cost
- viability
- memory metrics
- actions
- termination reason
- random seed

The output should be easy to inspect and easy to analyze in Python.

---

# Reproducibility Requirements

Every stochastic component must accept a seed.

The simulation should be reproducible from:

- code version
- configuration file
- random seed
- experiment parameters

The same input should produce the same output.

---

# Design Constraints

The software must be:

- readable
- modular
- deterministic when seeded
- testable
- easy to extend
- aligned with the theory documents

Avoid:

- hidden global state
- hard-coded magic numbers
- circular imports
- theory drift
- implicit behavior

---

# Implementation Sequence

Recommended order:

1. Create core datatypes.
2. Implement environment interface.
3. Implement baseline policies.
4. Implement simulation engine.
5. Implement metrics.
6. Implement logging.
7. Add tests.
8. Add example run.
9. Add experiment scripts.

---

# Acceptance Criteria for Phase 1

Phase 1 is complete when:

- the repository contains the software skeleton,
- the toy environment runs,
- baseline policies execute,
- metrics are computed,
- logs are written,
- tests pass,
- and the example simulation reproduces the same result when seeded.

---

# Final Principle

The software must never become a second theory.

Its role is to instantiate AST, test AST, and help refine AST.
