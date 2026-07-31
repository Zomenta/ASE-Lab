import time

from core.config import Config
from environment.world import World
from agents.agent import Agent
from simulation.renderer import ConsoleRenderer, NullRenderer


class Engine:

    def __init__(self, config=None, renderer=None):

        self.config = config or Config()
        self.world = World(self.config)

        if renderer is not None:
            self.renderer = renderer
        elif self.config.headless:
            self.renderer = NullRenderer()
        else:
            self.renderer = ConsoleRenderer(self.config)

        self.agents = [
            Agent(config=self.config)
        ]

        self.step = 0

    def update(self):

        self.step += 1

        for agent in self.agents:

            if agent.alive:
                agent.move(self.world)

    def render(self):
        self.renderer.render(self.world, self.agents, self.step)

    def run(self):

        while True:

            self.update()

            self.render()

            if (
                self.config.max_steps is not None
                and self.step >= self.config.max_steps
            ):
                break

            if not self.config.headless:
                time.sleep(Config.RENDER_SLEEP_SECONDS)
