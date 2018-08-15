from bots.flappy_bot import FlappyBot
from executors.flappy import Flappy
from parsers.flappy_parser import FlappyParser
from runners.simple_runner import SimpleRunner

runner = SimpleRunner()

runner.run(Flappy(), FlappyParser(), FlappyBot())