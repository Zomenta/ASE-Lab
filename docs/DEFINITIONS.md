# DEFINITIONS.md

# Adaptive State Theory (AST) Formal Definitions

**Version:** 1.0  
**Status:** Phase 0 Support File

---

## 1. Adaptive system

An adaptive system is a system whose future behavior is modified by interaction with its environment.

Formally:

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

## 2. Internal state

The internal state \(x_t \in X\) is the set of system variables at time \(t\) relevant to future behavior.

---

## 3. Environment state

The environment state \(e_t \in E\) is the set of external variables that influence the system but are not fully controlled by it.

---

## 4. Observation

The system forms an observation:

\[
o_t = O(x_t, e_t)
\]

where \(o_t\) is the information available to the system at time \(t\).

---

## 5. Action

The system selects an action:

\[
a_t \sim \pi(o_t, m_t, \theta_t)
\]

where \(m_t\) is memory and \(\theta_t\) is the current adaptive parameter set.

---

## 6. Transition

The joint system-environment update is:

\[
x_{t+1} = T_X(x_t, a_t, e_t, \xi_t)
\]

\[
e_{t+1} = T_E(e_t, a_t, x_t, \zeta_t)
\]

where \(\xi_t\) and \(\zeta_t\) are stochastic influences.

---

## 7. Memory

Memory is any retained state that causally influences future decisions or future viability.

\[
m_{t+1} = M(m_t, o_t, a_t, r_t)
\]

where \(r_t\) is feedback or outcome.

---

## 8. Viability

Viability is the probability that the system remains a coherent functional system over a time horizon \(T\):

\[
V_T(x_0) = \Pr(\tau_{\text{exit}} > T \mid x_0)
\]

where \(\tau_{\text{exit}}\) is the first exit time from the acceptable region.

---

## 9. Viable set

The viable set is:

\[
K = \{x \in X : x \text{ is acceptable for continued operation}\}
\]

A system is viable when its trajectory remains in \(K\) for the required horizon.

---

## 10. Viability kernel

The viability kernel is the largest subset of \(K\) from which at least one admissible policy can keep the system inside \(K\) over the required horizon.

---

## 11. Adaptive pressure

Adaptive pressure is the expected future loss imposed by the environment:

\[
P_t = \mathbb{E}[L(x_t, e_t)]
\]

with:

\[
P_t \ge 0
\]

A decomposed pressure model may use:

\[
P_t = \sum_i w_i P_{i,t}, \quad w_i \ge 0, \quad \sum_i w_i = 1
\]

---

## 12. Adaptive capacity

Adaptive capacity is the system's ability to remain viable under perturbation:

\[
C_t = \sup\{\delta : \Pr(\text{system remains viable under } \delta) \ge \tau\}
\]

with:

\[
C_t \ge 0
\]

Capacity is multi-component and may arise from redundancy, flexibility, learning, repair, cooperation, computation, energy availability, and institutional organization.

---

## 13. Adaptive balance

Adaptive balance is the difference between capacity and pressure:

\[
\Delta_t = C_t - P_t
\]

If \(\Delta_t > 0\), viability is locally favored.  
If \(\Delta_t < 0\), pressure dominates capacity.

---

## 14. Cost

Cost is the expenditure required to adapt:

\[
K_t \ge 0
\]

Cost may include energy, computation, time, coordination, opportunity cost, and resources.

---

## 15. Adaptive timescale

Let \(\tau_E\) be the environmental timescale and \(\tau_A\) the adaptive timescale.

\[
\rho_t = \frac{\tau_E}{\tau_A}
\]

---

## 16. Identity

Identity is a classification rule:

\[
D_I(S_t, S_0) \le \varepsilon_I
\]

Identity is used to decide whether a later state still counts as the same adaptive system.

Identity is not a primary dynamical variable.

---

## 17. Adaptive efficiency

A simple efficiency ratio is:

\[
\eta_t = \frac{\Delta V_t}{K_t}
\]

or:

\[
\eta_t = \frac{\text{adaptive benefit}_t}{\text{adaptive cost}_t}
\]

---

## 18. Adaptation

A change counts as adaptation when it increases expected long-term viability under bounded cost:

\[
V_{t+1} > V_t
\]

subject to the system's constraint limits.

---

## 19. Notes on measurement

The following are proxies or implementations, not the core definitions:

- survival time
- exit time
- shock tolerance
- recovery margin
- predictive information
- compression score
- energy cost
- coordination burden

These measures should be matched to the domain without replacing the AST terms themselves.
