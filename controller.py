import screenshooter as ss
from action_executor import change_window
from bots.crazy_bot import CrazyBot
from game import Game
from parsers.pacman_parser import PacmanParser
import time
import cv2

how_long = 15
shooter = ss.shooter()
parser = PacmanParser()
bot = CrazyBot()
with Game() as _:
    start = time.time()
    while time.time() - start < how_long:
        image = shooter.shot()
        cv2.namedWindow("pacman")
        cv2.imshow("pacman", image)
        cv2.waitKey(1)
        change_window()
        parsed = parser.parse(image)
        action = bot.get_action()
        time.sleep(.03)
        action()
