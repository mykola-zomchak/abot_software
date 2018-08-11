import screenshooter as ss
from bots.crazy_bot import CrazyBot
from game import Game
from parsers.pacman_parser import PacmanParser
import time
import cv2

how_long = 10
shooter = ss.shooter()
parser = PacmanParser()
bot = CrazyBot()
with Game() as _:
    start = time.time()
    cv2.namedWindow("pacman")
    while time.time() - start < how_long:
        field = parser.parse(shooter.shot())
        cv2.imshow("pacman", field.image)
        cv2.waitKey(1)
        action = bot.get_action()
        action()
