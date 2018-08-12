from bots.crazy_bot import CrazyBot
from executors.pacman import Pacman
from parsers.pacman_parser import PacmanParser
from runners.simple_runner import SimpleRunner

runner = SimpleRunner()
runner.run(Pacman(), PacmanParser(), CrazyBot())
