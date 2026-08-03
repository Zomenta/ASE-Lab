# CONFIG.md

# ASE Laboratory — Configuration
## Phase 1 Support File

**Version:** 1.0  
**Status:** Phase 1 Support File

---

# Purpose

This file defines the configurable parameters used by AST simulations and experiments.

The goal is to keep experimental settings explicit, reproducible, and easy to compare.

---

# Core Configuration Fields

## Simulation

- `seed`: random seed
- `steps`: number of simulation steps
- `dt`: timestep size
- `terminate_on_violation`: whether simulation stops when viability fails
- `log_frequency`: how often to record outputs

## Environment

- `initial_resources`
- `resource_regen_rate`
- `disturbance_rate`
- `disturbance_strength`
- `environment_noise`
- `environment_size`

## Agent

- `initial_energy`
- `action_cost`
- `memory_size`
- `memory_decay`
- `policy_type`
- `threshold_value`
- `greedy_strength`

## AST Metrics

- `viability_threshold`
- `pressure_weight`
- `capacity_weight`
- `memory_weight`
- `cost_weight`
- `timescale_weight`

## Experiment

- `experiment_name`
- `policy_name`
- `baseline_name`
- `output_directory`
- `plot_enabled`
- `save_csv`
- `save_json`

---

# Recommended Default Values

The exact values are implementation choices, but the first prototype should keep them small and easy to inspect.

Example defaults:

- `seed = 42`
- `steps = 100`
- `dt = 1.0`
- `terminate_on_violation = True`
- `log_frequency = 1`

---

# Design Rule

All important experimental parameters must be stored in configuration objects or config files.

Do not hide scientific assumptions inside code constants.
