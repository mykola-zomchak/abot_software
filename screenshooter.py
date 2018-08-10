import pyautogui
import numpy as np


class ScreenShooter:
    def __init__(self, region = None, window_name = None):
        self.region = region
        self.window_name = window_name

    def get_screen(self, region = None):
        if region is None:
            region = self.region
        return np.array(pyautogui.screenshot(region = region))[..., ::-1] # converts from rgb to bgr