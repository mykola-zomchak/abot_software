import screenshooter as ss
from bots.scared_bot import ScaredBot
from game import Game
from parsers.pacman_parser import PacmanParser
import time
import cv2

how_long = 60
shooter = ss.ScreenShooter()
parser = PacmanParser()
bot = ScaredBot()
with Game() as _:
    start = time.time()
    cv2.namedWindow("pacman")
    while time.time() - start < how_long:
        screen = shooter.get_screen('pacman.html')
        field = parser.parse(screen)
        action = bot.get_action(field)
        action()
        cv2.imshow("pacman", field.image)
        cv2.waitKey(1)
