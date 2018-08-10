import screenshooter as ss
from bots.crazy_bot import CrazyBot
from game import Game
from parsers.pacman_parser import PacmanParser
import time

how_long = 10
shooter = ss.ScreenShooter()
parser = PacmanParser()
bot = CrazyBot()

with Game() as _:
    start = time.time()
    while time.time() - start < how_long:

        image = shooter.get_screen()
        parsed = parser.parse(image)
        action = bot.get_action()
        action()
        time.sleep(.5)
