import screenshoter as ss
from bots.crazy_bot import CrazyBot
from game import Game
from image_parser import field
import time

how_long = 10
shooter = ss.ScreenShooter()
bot = CrazyBot()
with Game() as game:
    start = time.time()
    while time.time() - start < how_long:
        image = shooter.get_screen()
        parsed = field(image)
        action = bot.get_action(parsed)
        action()
