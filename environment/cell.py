from core.config import Config


class Cell:

    def __init__(self, config):

        if config.rng.random() < Config.CELL_ENERGY_SPAWN_CHANCE:
            self.energy = config.rng.randint(
                Config.CELL_ENERGY_MIN, Config.CELL_ENERGY_MAX
            )
        else:
            self.energy = 0

    def symbol(self):

        if self.energy > 0:
            return "E"

        return "."
