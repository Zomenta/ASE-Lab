from core.config import Config


class ConsoleRenderer:
    """ASCII console renderer for the simulation."""

    def __init__(self, config):
        self.config = config

    def render(self, world, agents, step):
        agent = agents[0]

        print("Alive:", agent.alive)
        print("\n" * 2)

        print("=" * Config.RENDER_SEPARATOR_WIDTH)
        print("ASE STEP", step)
        print("=" * Config.RENDER_SEPARATOR_WIDTH)

        print()

        for y in range(world.height):

            row = []

            for x in range(world.width):

                if x == agent.x and y == agent.y:
                    row.append("A")
                else:
                    row.append(world.grid[y][x].symbol())

            print(" ".join(row))

        print()
