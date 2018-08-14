from time import time
from bots.bot import Bot
from executors.executor import Executor
from parsers.image_parser import ImageParser
from runners.runner import Runner
import cv2


class SimpleRunner(Runner):

    def run(self, game: Executor, parser: ImageParser, bot: Bot, how_long=100):
        with game as game:
            start = time()
            cv2.namedWindow(game.window_name + ' analysis')
            while time() - start < how_long:
                screen = self.shooter.get_screen(game.window_name)
                parsed = parser.parse(screen)
                bot.make_action(parsed)
                cv2.imshow("pacman", parsed.image)
                cv2.waitKey(1)
