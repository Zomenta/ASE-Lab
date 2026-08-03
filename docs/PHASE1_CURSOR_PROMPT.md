# PHASE1_CURSOR_PROMPT.md

# ASE Laboratory — Phase 1
## Minimal AST Simulator Architecture

You are the Chief Software Engineer of the Adaptive Systems Laboratory (ASE).

This is **NOT** a prototype.
This is the foundation of a long-term scientific research platform.

The repository already contains the scientific theory.

Your job is **NOT** to invent new theory.

Your job is to translate the existing theory into clean, modular, testable software.

Everything should be implemented as if this project will eventually become an open-source scientific framework.

---

# Read First

Before writing any code read:

docs/THEORY.md

docs/MATHEMATICS.md

docs/DEFINITIONS.md

docs/AST_GLOSSARY.md

PROJECT.md

ROADMAP.md

TEAM.md

Do not redefine concepts.

Use the definitions exactly as documented.

---

# Design Philosophy

Follow these principles.

• Theory drives implementation.
• Every class should correspond to a scientific concept.
• No hidden assumptions.
• No unnecessary optimization.
• Code should be readable before being clever.
• Every numerical result should be reproducible.
• Every stochastic component must accept a random seed.
• Every public class requires documentation.
• Everything should be unit-testable.

---

# Phase 1 Goal

Build the smallest possible simulation framework capable of testing Adaptive State Theory.

Not an ecosystem.

Not reinforcement learning.

Not evolutionary computation.

Only the minimal infrastructure needed to test AST.

---

# Required Repository Structure

Create (or complete) the following.

core/
    __init__.py
    state.py
    system.py
    metrics.py
    types.py

agents/
    __init__.py
    base.py
    policy.py
    memory.py

environment/
    __init__.py
    base.py
    toy_world.py

simulation/
    __init__.py
    engine.py
    logger.py

experiments/
    baseline.py

tests/
    test_state.py
    test_metrics.py
    test_engine.py

examples/
    simple_run.py

---

# Core Scientific Objects

Implement only the concepts defined in THEORY.md.

AdaptiveState

Stores

- internal variables
- resources
- memory
- policy state
- viability

AdaptiveSystem

Responsible for

- observing environment
- updating state
- executing policy
- updating viability

Environment

Responsible only for

- disturbances
- resources
- environmental dynamics

SimulationEngine

Responsible only for

- advancing time
- calling update methods
- logging data

---

# Metrics

Implement AST metrics as independent functions.

At minimum include

Viability

Pressure

Capacity

Adaptive Balance

Cost

Timescale Ratio

Memory Quality

These should be modular.

No metric should depend on implementation details of another module.

---

# Toy Environment

Implement one extremely small environment.

Example:

A resource field.

Each timestep

resources regenerate

disturbance occurs

agent consumes resources

agent updates

Nothing more.

No graphics.

No GUI.

No reinforcement learning.

---

# Policies

Implement three simple baseline policies.

Random

Acts randomly.

Greedy

Always maximizes immediate resources.

Threshold

Acts conservatively using fixed thresholds.

These are benchmarks—not intelligent agents.

---

# Logging

Simulation should automatically record

time

resources

capacity

pressure

cost

viability

memory

actions

Output as CSV.

---

# Unit Tests

Every module must have tests.

Test

metric correctness

simulation loop

state updates

determinism with fixed seed

CSV generation

No feature is complete without tests.

---

# Example Script

Create

examples/simple_run.py

Running it should

create environment

create one agent

run simulation

save CSV

print summary statistics

No visualization yet.

---

# Code Quality

Use

type hints

docstrings

small functions

clear names

avoid global variables

avoid circular imports

No magic numbers.

Constants belong in one location.

---

# Explicitly Do NOT Build Yet

Do NOT implement

multi-agent systems

genetic algorithms

neural networks

reinforcement learning

graphical interface

parallel simulation

GPU acceleration

database support

plugin systems

advanced optimization

Keep Phase 1 minimal.

---

# Deliverables

The repository should compile.

All tests should pass.

The example simulation should run.

CSV output should be generated.

Architecture should make future AST extensions easy.

---

# Final Requirement

Whenever implementation details are ambiguous:

Do NOT invent scientific concepts.

Instead:

1. leave a TODO
2. reference the relevant theory document
3. implement the smallest scientifically faithful version

The software exists to test Adaptive State Theory—not to redefine it.