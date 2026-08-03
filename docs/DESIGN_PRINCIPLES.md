# DESIGN_PRINCIPLES.md

# ASE Laboratory — Software Design Principles
## Phase 1 and Beyond

**Version:** 1.0  
**Status:** Phase 1 Support File

---

# Purpose

This document defines the engineering rules for the Adaptive Systems Engine.

The goal is to keep the codebase scientific, modular, and maintainable.

---

# Core Principles

## 1. Science before software
Implementation exists to test theory.

## 2. Theory before optimization
Do not optimize behavior before the scientific structure is stable.

## 3. Reproducibility first
Every simulation must be rerunnable from the repository.

## 4. Determinism by default
Randomness must always be controllable by seed.

## 5. Modularity
Each module should do one job.

## 6. Explicit interfaces
Functions and classes should make their dependencies obvious.

## 7. Small components
Prefer simple parts that can be tested independently.

## 8. No hidden state
Avoid global variables and implicit behavior.

## 9. Unit tests for core logic
Metrics, state updates, and simulation steps must be testable.

## 10. Documented assumptions
If a shortcut is taken, it must be written down.

---

# Design Rules

## Naming
Names should match the theory vocabulary.

Examples:

- AdaptiveState
- AdaptiveSystem
- Viability
- Pressure
- Capacity
- Memory
- Cost
- Policy
- Environment

Avoid names that obscure the scientific meaning.

---

## Module Boundaries
A module should not reach into another module's internals unless that is part of its responsibility.

Examples:

- metrics should not own environment behavior,
- policies should not own simulation loops,
- the environment should not decide experiment interpretation,
- tests should verify behavior rather than duplicate implementation logic.

---

## Dependencies
Dependencies should point inward toward core abstractions, not outward toward ad hoc scripts.

Prefer:

- core objects
- small interfaces
- explicit imports

Avoid:

- tangled circular dependencies
- deep import chains
- convenience hacks that hide responsibility

---

## Data Flow
The simulation should move data in a single readable direction:

environment → observation → policy → action → state update → metrics → logger

If data flow becomes confusing, the architecture needs simplification.

---

## Metrics
Metrics should be implemented as pure or near-pure functions when possible.

Metrics should:

- be easy to compute,
- be easy to test,
- be easy to compare,
- and be easy to reuse in experiments.

---

## Logging
Logging should record what happened, not interpret what happened.

Interpretation belongs to analysis scripts and reports.

---

## Configuration
All meaningful experiment parameters should live in configuration files or clearly defined parameter objects.

Do not bury scientific choices in code constants.

---

## Randomness
Every source of randomness must be seeded.

Random number generation should be explicitly passed where possible.

---

# Code Style

The preferred style is:

- readable,
- typed,
- small,
- and well-commented where necessary.

The code should be understandable by a future researcher who did not write it.

---

# Testing Principles

Each important behavior should have a test.

Tests should verify:

- outputs,
- invariants,
- determinism,
- edge cases,
- and failure handling.

A test suite is part of the scientific method, not a side feature.

---

# Extension Principles

When adding new features:

1. preserve existing interfaces if possible,
2. add tests first or alongside implementation,
3. keep the change small,
4. avoid changing theory accidentally,
5. update docs if behavior changes.

---

# What to Avoid

Avoid:

- feature creep,
- clever abstractions that hide meaning,
- overengineering,
- premature generalization,
- and “temporary” shortcuts that become permanent.

---

# Phase 1 Interpretation

Phase 1 is successful when the repository contains a small, clean simulator that faithfully instantiates the theory and can be used for reproducible experiments.

It is not successful merely because it looks advanced.

It is successful because it is scientifically useful.
