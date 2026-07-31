from agents.brain import Brain
from core.config import Config


class Agent:

    def __init__(self, x=None, y=None):
        self.x = x if x is not None else Config.AGENT_START_X
        self.y = y if y is not None else Config.AGENT_START_Y
        self.energy = Config.AGENT_START_ENERGY
        self.age = 0
        self.alive = True
        self.brain = Brain()

    def move(self, world):

        self.x, self.y = self.brain.decide(self, world)

        self.energy -= Config.AGENT_MOVE_COST
        self.age += 1

        cell = world.grid[self.y][self.x]

        if cell.energy > 0:
            self.energy += cell.energy
            cell.energy = 0
        if self.energy <= 0:
            self.alive = False
