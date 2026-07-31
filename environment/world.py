from environment.cell import Cell
from core.config import Config


class World:

    def __init__(self, config=None, width=None, height=None):

        if isinstance(config, Config):
            self.config = config
        else:
            if config is not None:
                width = config
            self.config = Config()

        self.width = width if width is not None else Config.WORLD_WIDTH
        self.height = height if height is not None else Config.WORLD_HEIGHT

        self.grid = []

        for y in range(self.height):

            row = []

            for x in range(self.width):
                row.append(Cell(self.config))

            self.grid.append(row)

    def display(self, agent):

        print()

        for y in range(self.height):

            row = []

            for x in range(self.width):

                if x == agent.x and y == agent.y:
                    row.append("A")
                else:
                    row.append(self.grid[y][x].symbol())

            print(" ".join(row))

        print()
