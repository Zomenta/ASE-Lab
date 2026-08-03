# MATHEMATICS.md

# Adaptive State Theory (AST)
## Mathematical Foundations

**Version:** 1.0 (Foundational Draft)  
**Status:** Phase 0 Support File

---

## Purpose

This file collects the mathematical core of Adaptive State Theory in a compact, repository-friendly form.

AST is a substrate-neutral framework for adaptive systems. Its central object is **viability** under changing constraints over time.

---

## 1. Core Ontology

An adaptive system is represented as:

\[
S = (X, E, O, U, \pi, M, T, V, I)
\]

where:

- \(X\) = internal state space
- \(E\) = environment state space
- \(O\) = observation operator
- \(U\) = action space
- \(\pi\) = adaptive policy
- \(M\) = memory update operator
- \(T\) = state-transition operator
- \(V\) = viability functional
- \(I\) = identity rule

---

## 2. State, Observation, Action, Transition

Let:

- \(x_t \in X\) be internal state
- \(e_t \in E\) be environment state
- \(o_t\) be observation
- \(a_t\) be action
- \(m_t\) be memory state

Then:

\[
o_t = O(x_t, e_t)
\]

\[
a_t \sim \pi(o_t, m_t, \theta_t)
\]

\[
x_{t+1} = T_X(x_t, a_t, e_t, \xi_t)
\]

\[
e_{t+1} = T_E(e_t, a_t, x_t, \zeta_t)
\]

where \(\xi_t\) and \(\zeta_t\) are stochastic influences.

Memory updates as:

\[
m_{t+1} = M(m_t, o_t, a_t, r_t)
\]

where \(r_t\) is feedback or outcome.

---

## 3. Viability

Viability is the probability that a system remains a coherent functional system over a time horizon \(T\):

\[
V_T(x_0) = \Pr(\tau_{\text{exit}} > T \mid x_0)
\]

where \(\tau_{\text{exit}}\) is the first time the trajectory exits the acceptable region.

### Viable set

Let \(K\) be the domain-specific set of acceptable states.

\[
K = \{x \in X : x \text{ is acceptable for continued operation}\}
\]

A system is viable when its trajectory remains inside \(K\) for the relevant horizon.

### Viability kernel

The viability kernel is the largest subset of \(K\) from which at least one admissible policy can keep the system inside \(K\) for the target horizon.

This makes viability a constraint-based object rather than a vague survival statement.

---

## 4. Core Quantities

### Adaptive pressure

Adaptive pressure is the expected future loss imposed by the environment:

\[
P_t = \mathbb{E}[L(x_t, e_t)]
\]

with:

\[
P_t \ge 0
\]

If pressure is decomposed, then:

\[
P_t = \sum_i w_i P_{i,t}, \quad w_i \ge 0, \quad \sum_i w_i = 1
\]

### Adaptive capacity

Adaptive capacity is the system's ability to maintain viability under perturbation:

\[
C_t = \sup\{\delta : \Pr(\text{system remains viable under } \delta) \ge \tau\}
\]

with:

\[
C_t \ge 0
\]

Capacity is multi-component. Perturbation tolerance is one measurable consequence, not the whole definition.

### Adaptive balance

\[
\Delta_t = C_t - P_t
\]

If \(\Delta_t > 0\), viability is locally favored.  
If \(\Delta_t < 0\), pressure dominates capacity.

### Cost

Cost is the expenditure required to adapt:

\[
K_t \ge 0
\]

### Adaptive timescale

Let \(\tau_E\) be the environmental change timescale and \(\tau_A\) the adaptive response timescale.

\[
\rho_t = \frac{\tau_E}{\tau_A}
\]

### Identity

Identity is a classification rule:

\[
D_I(S_t, S_0) \le \varepsilon_I
\]

Identity is not a primary dynamical variable.

---

## 5. Derived Measures

### Adaptive efficiency

A simple adaptive efficiency ratio is:

\[
\eta_t = \frac{\Delta V_t}{K_t}
\]

or, in a benefit-cost formulation:

\[
\eta_t = \frac{\text{adaptive benefit}_t}{\text{adaptive cost}_t}
\]

### Adaptation

A change counts as adaptation when it increases expected long-term viability under bounded cost:

\[
V_{t+1} > V_t
\]

subject to the system's resource and constraint limits.

---

## 6. Candidate Dynamic Models

AST does not require one universal governing equation. It allows a family of model forms.

### Model family A: additive viability update

\[
\frac{dV}{dt} = \alpha_1(C_t - P_t) + \alpha_2 Q_{M,t} - \alpha_3 K_t + \alpha_4 \log(\rho_t)
\]

where \(Q_{M,t}\) is a model-specific memory-quality measure.

### Model family B: bounded score-to-viability map

\[
\mathrm{logit}(V_{t+1}) = b_0 + b_1 C_t - b_2 P_t + b_3 Q_{M,t} - b_4 K_t + b_5 \log(\rho_t)
\]

### Model family C: constrained viability dynamics

\[
\frac{dV}{dt} = F(C, P, M, K, \rho)
\quad \text{subject to} \quad x_t \in K \text{ for all admissible } t
\]

The core theory does not fix one \(F\); it defines the admissible structure that specific models must satisfy.

---

## 7. Operational Layer

Each core concept should be linked to:

1. a conceptual meaning,
2. a mathematical definition,
3. an observable proxy,
4. a computational implementation.

Example proxy mapping:

- viability → survival probability, exit time
- capacity → shock tolerance, recovery margin
- pressure → hazard, deficit, overload
- memory → predictive information, compression score
- cost → energy, compute, delay, coordination burden
- timescale → recovery lag versus drift interval

These proxies are implementation choices, not the definitions themselves.

---

## 8. Falsification Rules

AST principles should be testable.

### Balance principle

Higher \(C_t - P_t\) should predict higher viability in matched conditions.

Failure condition: no positive association after controlling for confounds.

### Memory principle

Higher memory quality should reduce search effort or forecast error at fixed capacity.

Failure condition: memory does not improve performance or only does so at prohibitive cost.

### Timescale principle

Better matching between \(\tau_A\) and \(\tau_E\) should improve viability.

Failure condition: timescale matching does not outperform simpler baseline models.

### Cooperation principle

Cooperation should be favorable only when its viability gain exceeds coordination cost.

Failure condition: cooperation remains net harmful after controls.

### Identity rule

Identity thresholds should classify functionally equivalent systems consistently.

Failure condition: the identity boundary is arbitrary or unstable across equivalent cases.

---

## 9. Research Use

This mathematical core is intended to support:

- toy simulations
- benchmark comparisons
- parameter fitting
- counterexample search
- proof attempts
- cross-domain translation

The next step is not to add more concepts. The next step is to test whether these concepts predict anything useful in a minimal environment.
