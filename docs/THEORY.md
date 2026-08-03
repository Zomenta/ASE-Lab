# THEORY.md

# Adaptive State Theory (AST)

**Version:** 1.0 (Foundational Draft)
**Status:** Theory Foundation

---

# Purpose

Adaptive State Theory (AST) is a substrate-neutral mathematical framework for understanding adaptive systems through a single central question:

> **What determines whether an adaptive system remains viable under changing constraints over time?**

Rather than treating optimization, reward, fitness, or efficiency as the primary objective, AST proposes that **long-term viability** is the universal outcome variable.

Optimization, learning, evolution, resilience, and control are interpreted as mechanisms that influence viability rather than objectives in themselves.

---

# Design Principles

AST is built around several guiding principles.

* **Substrate Neutrality** — The same theory should apply to biological, artificial, economic, institutional, and cultural systems.
* **Viability First** — Long-term persistence is the primary quantity of interest.
* **Constraint-Based** — Adaptation occurs under limited resources, uncertainty, and environmental pressure.
* **Modularity** — The theory is separated from specific mathematical models and implementation choices.
* **Falsifiability** — Every principle must generate observable predictions and possible failure conditions.

---

# Core Ontology

An adaptive system is defined as

[
S=(X,E,O,U,\pi,M,T,V,I)
]

where

| Symbol | Meaning                   |
| ------ | ------------------------- |
| **X**  | Internal state space      |
| **E**  | Environment               |
| **O**  | Observation operator      |
| **U**  | Action space              |
| **π**  | Adaptive policy           |
| **M**  | Memory operator           |
| **T**  | State-transition operator |
| **V**  | Viability functional      |
| **I**  | Identity rule             |

These concepts form the irreducible vocabulary of AST.

---

# Fundamental Concepts

## Viability

Viability is the probability that a system continues functioning as a coherent adaptive system over a specified time horizon.

Rather than treating survival as binary, AST models viability as a probabilistic quantity constrained by acceptable system states.

A system is viable when its trajectory remains inside a **viable set**.

---

## Viable Set

The viable set **K** is the collection of states that satisfy the functional requirements necessary for continued operation.

Crossing the boundary of **K** represents functional failure.

---

## Viability Kernel

The viability kernel is the largest subset of the viable set from which at least one admissible policy can keep the system viable indefinitely (or for the required time horizon).

The viability kernel defines the region where adaptation is still possible.

---

## Adaptive Capacity

Adaptive Capacity is the system's ability to maintain viability despite environmental change.

Capacity may arise from:

* redundancy
* flexibility
* learning
* repair
* cooperation
* computation
* energy availability
* institutional organization

These are sources of capacity, not capacity itself.

---

## Adaptive Pressure

Adaptive Pressure is the expected future loss imposed by environmental conditions.

Sources include:

* scarcity
* competition
* uncertainty
* conflict
* disturbances
* information degradation
* resource limitations

Pressure is external to the system but affects viability.

---

## Memory

Memory is any retained state that causally improves future viability.

Memory may be:

* genetic
* neural
* learned
* institutional
* cultural
* digital

AST intentionally avoids defining memory through one specific implementation.

Information bottleneck methods, predictive information, compression metrics, and other approaches are measurement tools—not definitions.

---

## Cost

Cost is the expenditure required to adapt.

Examples include:

* energy
* computation
* time
* coordination
* opportunity cost
* resources

Adaptation is never assumed to be free.

---

## Adaptive Timescale

AST distinguishes between:

* Environmental Timescale
* Adaptive Timescale

Their ratio determines whether adaptation can keep pace with environmental change.

When environments change faster than adaptation can occur, viability decreases.

---

## Identity

Identity is a classification rule.

It determines whether two system states should be considered the same adaptive system.

Identity is **not** a primary dynamical variable.

---

# Derived Concepts

## Adaptive Balance

Adaptive Balance represents the relationship between adaptive capacity and adaptive pressure.

Conceptually,

> Capacity exceeding pressure increases the likelihood of long-term viability.

Adaptive Balance is a diagnostic quantity rather than a governing law.

---

## Adaptive Efficiency

Adaptive Efficiency measures the increase in viability achieved per unit adaptation cost.

Efficient systems improve viability while minimizing required resources.

---

## Adaptation

Adaptation is defined as any change that increases expected long-term viability while respecting resource constraints.

Different mechanisms—including learning, evolution, cooperation, structural reorganization, and niche construction—are all special cases of adaptation.

---

# Architecture

AST is intentionally separated into three layers.

## Layer 1 — Foundation

Defines:

* ontology
* viability
* capacity
* pressure
* memory
* cost
* identity
* viable sets
* viability kernels

This layer is independent of particular mathematical models.

---

## Layer 2 — Dynamics

Contains candidate mathematical models describing viability change.

Possible model families include:

* deterministic dynamics
* stochastic dynamics
* discrete-time models
* continuous-time models
* constrained control models
* cooperative models

No single equation defines AST.

---

## Layer 3 — Empirical Science

Contains:

* operational definitions
* measurement protocols
* simulations
* experiments
* benchmarks
* statistical inference
* falsification
* counterexample search

This layer connects AST to observable systems.

---

# Operationalization

Every core concept should be specified at four levels.

| Level         | Description                                      |
| ------------- | ------------------------------------------------ |
| Conceptual    | What the variable means                          |
| Mathematical  | Formal definition                                |
| Observable    | How it can be measured                           |
| Computational | How it is implemented in simulation or inference |

This separation keeps AST independent of any particular measurement methodology.

---

# Candidate Dynamic Models

AST does not require a universal governing equation.

Instead, it defines a family of admissible models whose purpose is to estimate viability.

Different domains may require different dynamics while sharing the same ontology.

---

# Falsifiability

Every AST principle must satisfy four requirements.

1. A clear prediction.
2. Observable variables.
3. An experimental or simulation test.
4. A defined failure condition.

Examples include:

* Higher adaptive capacity should improve long-term viability under comparable pressure.
* Predictive memory should reduce future search effort or forecasting error.
* Better timescale matching should improve viability.
* Cooperation should increase viability only when its benefits exceed coordination costs.

Failure of these predictions requires revision of the associated principle.

---

# Scope

AST is intended to provide a common language for adaptive systems across domains including:

* Biology
* Artificial Intelligence
* Economics
* Organizations
* Institutions
* Cultural evolution
* Complex engineered systems

The ontology remains constant while measurements and dynamics may differ.

---

# What AST Is

AST is:

* a viability-centered theory
* a substrate-neutral ontology
* a modular mathematical framework
* a research program for adaptive systems

---

# What AST Is Not

AST is **not**:

* a single governing equation
* a replacement for control theory
* a replacement for evolutionary theory
* a replacement for reinforcement learning
* a replacement for resilience theory

Instead, AST provides a higher-level framework within which these theories can be interpreted, compared, and integrated according to their contributions to long-term viability.

---

# Open Research Questions

Current priorities include:

1. Formal derivation of candidate governing equations.
2. Mathematical analysis of viability dynamics.
3. Operational definitions for every core variable.
4. Cross-domain case studies.
5. Counterexample discovery.
6. Formal theorem proofs.
7. Benchmarking against existing adaptive-system theories.

---

# Vision

Adaptive State Theory proposes that **viability** is the most fundamental quantity shared by adaptive systems.

Rather than beginning with optimization, reward, or fitness, AST begins with a more basic question:

> **What allows an adaptive system to continue existing under changing conditions?**

By treating viability as the central organizing principle, AST aims to provide a unified theoretical foundation for studying adaptation across natural and artificial systems.
