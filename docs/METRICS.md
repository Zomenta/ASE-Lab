# METRICS.md

# ASE Laboratory — Metrics
## AST Phase 1 Support File

**Version:** 1.0  
**Status:** Phase 1 Support File

---

# Purpose

This document defines the main AST metrics used in simulation and analysis.

Each metric should be implemented in code as clearly as possible and should match the theory documents.

---

# Metric Catalog

## 1. Viability

### Definition
Viability is the probability or observed measure of remaining within an acceptable state over time.

### Mathematical form
\[
V_T(x_0) = \Pr(\tau_{\text{exit}} > T \mid x_0)
\]

### Interpretation
Higher viability means the system remains functional for longer.

### Implementation note
A simulation may estimate viability using survival over repeated runs.

---

## 2. Adaptive Pressure

### Definition
Adaptive pressure is the expected future loss imposed by the environment.

### Mathematical form
\[
P_t = \mathbb{E}[L(x_t, e_t)]
\]

### Interpretation
Higher pressure means more environmental difficulty.

### Implementation note
Pressure can be a scalar score built from disturbances, scarcity, or hazard.

---

## 3. Adaptive Capacity

### Definition
Adaptive capacity is the system's ability to remain viable under perturbation.

### Mathematical form
\[
C_t = \sup\{\delta : \Pr(\text{viable under } \delta) \ge \tau\}
\]

### Interpretation
Higher capacity means stronger tolerance to change.

### Implementation note
A toy model may estimate capacity from recovery margin or shock tolerance.

---

## 4. Adaptive Balance

### Definition
Adaptive balance is the difference between adaptive capacity and adaptive pressure.

### Mathematical form
\[
\Delta_t = C_t - P_t
\]

### Interpretation
Positive balance favors viability. Negative balance implies risk.

### Implementation note
This should be easy to compute and easy to compare across runs.

---

## 5. Cost

### Definition
Cost is the resource expenditure required to adapt.

### Mathematical form
\[
K_t \ge 0
\]

### Interpretation
Higher cost means greater resource burden.

### Implementation note
Cost may include energy, delay, or coordination burden.

---

## 6. Timescale Ratio

### Definition
Timescale ratio compares environmental change speed to adaptive response speed.

### Mathematical form
\[
\rho_t = \frac{\tau_E}{\tau_A}
\]

### Interpretation
A higher ratio means the system can respond more quickly relative to environmental drift.

### Implementation note
This can be estimated from drift intervals and recovery times.

---

## 7. Memory Quality

### Definition
Memory quality measures how much stored state improves future viability.

### Possible proxy
\[
Q_M = I(M_t ; X_{t+1:t+H}) - \beta I(M_t ; H_t)
\]

### Interpretation
Higher memory quality means memory is actually useful, not merely present.

### Implementation note
In the simplest toy world, memory quality can be approximated by prediction accuracy or reduced search cost.

---

# Metric Design Rules

- Metrics should be testable.
- Metrics should be reproducible.
- Metrics should be comparable across runs.
- Metrics should not silently redefine theory terms.
- Proxies are allowed, but they must be labeled as proxies.

---

# Minimal Phase 1 Metric Set

The first implementation should include at least:

- viability
- pressure
- capacity
- balance
- cost
- timescale ratio
- memory quality

That is enough to start scientific testing.
