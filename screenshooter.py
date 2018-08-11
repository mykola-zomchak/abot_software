import pyautogui
import numpy as np


class ScreenShooter:
    def __init__(self, window_name: str = None):
        self._window_name = window_name

    # public setter for save setting window name
    def set_window_name(self, window_name: str = None):
        self._window_name = window_name

    # Public method for converting rgb to bgr
    def rgb_to_bgr(self, array_rgb):
        return array_rgb[..., ::-1]

    # If you need get screen just some window set attribute self.window_name = "window name"
    # If you want to get screen of all region set self.window_name = None value

    def get_screen(self, window_name: str = None):
        if window_name:
            self._window_name = window_name
        if self._window_name is not None:
            win = pyautogui.getWindow(self._window_name)
            screen = pyautogui.screenshot(region=win.get_position())
            screen = self.rgb_to_bgr(np.array(screen))
            return screen
        else:
            screen = self.rgb_to_bgr(np.array(pyautogui.screenshot()))
            return screen
