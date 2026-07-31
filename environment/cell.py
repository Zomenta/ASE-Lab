import random

from core.config import Config


class Cell:

    def __init__(self):

        if random.random() < Config.CELL_ENERGY_SPAWN_CHANCE:
            self.energy = random.randint(
                Config.CELL_ENERGY_MIN, Config.CELL_ENERGY_MAX
            )
        else:
            self.energy = 0

    def symbol(self):

        if self.energy > 0:
            return "E"

        return "."
