# DEVELOPMENT.md

# ASE Laboratory — Development Workflow
## Phase 1 Support File

**Version:** 1.0  
**Status:** Phase 1 Support File

---

# Purpose

This document tells Cursor and other engineers how to work on ASE.

It defines the expected workflow for implementation tasks.

---

# General Workflow

For every development task:

1. Read the relevant docs.
2. Identify the exact scientific goal.
3. Implement the smallest useful version.
4. Add tests.
5. Run the example.
6. Record limitations.
7. Stop.

---

# Task Template

Every coding task should include:

- goal
- files to edit
- acceptance criteria
- tests required
- outputs expected
- restrictions

---

# Example Task Format

```text
Goal:
Implement AdaptiveState.

Files:
core/state.py
tests/test_state.py

Acceptance criteria:
- dataclass exists
- fields match docs
- copy/reset work
- tests pass

Restrictions:
- no new theory
- no hidden global state
- no unrelated refactor
```

---

# Implementation Order

Recommended order:

1. core types
2. state object
3. policy objects
4. environment object
5. simulation engine
6. metrics
7. logger
8. experiment runner
9. tests
10. example script

---

# Restrictions

Do not:

- add neural networks,
- add evolutionary algorithms,
- add GUI code,
- add advanced optimization,
- add distributed systems,
- change theory terms,
- hide assumptions in code.

---

# Testing Workflow

For every module:

- write or update tests,
- run tests,
- fix failures,
- keep tests deterministic.

---

# Review Workflow

Before merging a task:

- check alignment with theory docs,
- check API consistency,
- check reproducibility,
- check that the change is minimal.

---

# Output Expectations

Each task should leave the repository in a state that is:

- runnable,
- testable,
- understandable,
- and ready for the next task.

---

# Final Rule

If uncertain, choose the simplest implementation that remains faithful to the theory.
