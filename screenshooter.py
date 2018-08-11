import pyautogui
import numpy as np


class ScreenShooter:
    def __init__(self, window_name = None):
        if isinstance(window_name, str) and len(window_name) > 2:
            self._window_name = window_name
        else:
            self._window_name = None


    #public setter for save setting window name
    #because of using if is None
    def set_window_name(self, window_name = None):
        if isinstance(window_name, str) and len(window_name) > 2:
            self._window_name = window_name
        else:
            self._window_name = None

    #Public method for conerting rgb to bgr
    def rgb_to_bgr(self, array_rgb):
        return array_rgb[..., ::-1]

    #If you need get screen just some window set attribute self.window_name = "window name"
    #If you want to get screen of all region set self.window_name = None value

    def get_screen(self):
        if self._window_name is not None:
            win = pyautogui.getWindow(self._window_name)
            if win is not None:
                screen = pyautogui.screenshot(region=win.get_position())
                screen = self.rgb_to_bgr(np.array(screen))
                return screen
        screen = self.rgb_to_bgr(np.array(pyautogui.screenshot()))
        return screen


