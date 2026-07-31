import random


class Config:
    """Central configuration for ASE simulation parameters."""

    # World
    WORLD_WIDTH = 10
    WORLD_HEIGHT = 10

    # Agent
    AGENT_START_X = 5
    AGENT_START_Y = 5
    AGENT_START_ENERGY = 100
    AGENT_MOVE_COST = 1

    # Cell
    CELL_ENERGY_SPAWN_CHANCE = 0.15
    CELL_ENERGY_MIN = 20
    CELL_ENERGY_MAX = 50

    # Simulation display
    RENDER_SLEEP_SECONDS = 0.4
    RENDER_SEPARATOR_WIDTH = 40

    def __init__(self, seed=None, headless=False, max_steps=None):
        self.seed = seed
        self.headless = headless
        self.max_steps = max_steps
        self.rng = random.Random(seed)
