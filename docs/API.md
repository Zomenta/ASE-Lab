# API.md

# ASE Laboratory — Software API
## Phase 1 Support File

**Version:** 1.0  
**Status:** Phase 1 Support File

---

# Purpose

This file defines the main software interfaces for the minimal AST simulator.

The goal is to give Cursor a clear contract before implementation.

---

# Core Interfaces

## AdaptiveState

Represents the current state of the adaptive system.

### Responsibilities

- store internal variables
- store memory
- store viability-related fields
- track current time step
- support serialization if needed

### Expected methods

- `copy()`
- `update(...)`
- `reset(...)`
- `to_dict()`

---

## AdaptiveSystem

Coordinates the full adaptive process.

### Responsibilities

- observe the environment
- apply a policy
- update memory
- update state
- compute metrics

### Expected methods

- `observe()`
- `act()`
- `step()`
- `is_viable()`

---

## Environment

Represents external conditions.

### Responsibilities

- generate disturbances
- regenerate resources
- update external state

### Expected methods

- `reset()`
- `step()`
- `sample_disturbance()`
- `get_observation()`

---

## Policy

Chooses actions from observations.

### Required baseline policies

- random
- greedy
- threshold

### Expected methods

- `select_action(...)`
- `reset(...)` if needed

---

## Memory

Stores retained information that may improve future viability.

### Expected methods

- `update(...)`
- `decay(...)`
- `quality(...)`

---

## SimulationEngine

Runs the simulation loop.

### Responsibilities

- initialize state
- advance the environment and agent
- stop at terminal conditions
- record outputs
- return results

### Expected methods

- `run()`
- `step()`
- `reset()`

---

## Logger

Records simulation results in a machine-readable format.

### Responsibilities

- record step data
- write CSV
- store metadata

### Expected methods

- `log_step(...)`
- `save_csv(...)`
- `save_metadata(...)`

---

# Data Flow

The basic phase-1 data flow should be:

1. environment produces conditions
2. agent observes conditions
3. policy selects action
4. action affects system state
5. memory updates
6. metrics are computed
7. logger records the result

---

# Design Constraints

- keep interfaces small
- use type hints
- avoid circular imports
- keep public methods documented
- do not let the API drift away from the theory files

---

# Minimal Phase 1 Contract

If a module is not needed to run a reproducible toy simulation and collect metrics, it should not be added yet.
