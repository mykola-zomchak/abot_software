import pyautogui
import numpy as np

from consts import *


class Screenshooter:
    border = 25

    def shot(self) -> np.ndarray:
        return np.array(pyautogui.screenshot(region=(
            GAME_X + self.border, GAME_Y + BROWSER_HEADER, GAME_WIDTH - self.border * 2,
            GAME_HEIGHT - BROWSER_HEADER - self.border)))[..., ::-1]


def shooter() -> Screenshooter:
    return Screenshooter()
