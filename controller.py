from screenshoter import shot
from bots.crazy_bot import CrazyBot
from game import Game
from image_parser import field
import time

how_long = 10
bot = CrazyBot()
with Game() as game:
    start = time.time()
    while time.time() - start < how_long:
        image = shot()
        parsed = field(image)
        action = bot.get_action(parsed)
        action()
