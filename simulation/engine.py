import time

from core.config import Config
from environment.world import World
from agents.agent import Agent


class Engine:

    def __init__(self):

        self.world = World()

        self.agents = [
            Agent()
        ]

        self.step = 0

    def update(self):

        self.step += 1

        for agent in self.agents:

            if agent.alive:
                agent.move(self.world)

    def render(self):
        print("Alive:", self.agents[0].alive)
        print("\n" * 2)

        print("=" * Config.RENDER_SEPARATOR_WIDTH)
        print("ASE STEP", self.step)
        print("=" * Config.RENDER_SEPARATOR_WIDTH)

        self.world.display(self.agents[0])

    def run(self):

        while True:

            self.update()

            self.render()

            time.sleep(Config.RENDER_SLEEP_SECONDS)
