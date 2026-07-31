import argparse

from core.config import Config
from simulation.engine import Engine


def main():
    parser = argparse.ArgumentParser(description="Adaptive Systems Engine")
    parser.add_argument(
        "--headless",
        action="store_true",
        help="Run without rendering or frame delay",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Random seed for reproducible runs",
    )
    parser.add_argument(
        "--steps",
        type=int,
        default=None,
        help="Maximum number of simulation steps",
    )
    args = parser.parse_args()

    config = Config(
        seed=args.seed,
        headless=args.headless,
        max_steps=args.steps,
    )
    engine = Engine(config)
    engine.run()


if __name__ == "__main__":
    main()
