import screenshooter as ss
from bots.crazy_bot import CrazyBot
from games_controllers import flappy
import time
import cv2


pause = 1000
how_long = 60
shooter = ss.ScreenShooter()
bot = CrazyBot()
with flappy.Game() as _:
    start = time.time()
    cv2.namedWindow("Flappy Bird")
    while time.time() - start < how_long:
        screen = shooter.get_screen('Flappy Bird')
        cv2.imshow("Flappy Bird", screen)
        cv2.waitKey(pause)
        cv2.destroyAllWindows()
