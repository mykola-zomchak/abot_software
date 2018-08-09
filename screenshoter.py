import pyautogui
import numpy as np


class ScreenShoter:
    def __init__(self, region = None, window_name = None):
        self.region = region
        self.window_name = window_name

    def get_screen(self):
        return (np.array(pyautogui.screenshot()))


    # make exception for bad region value as non-tuple
    def get_screen_region(self, region = None):
        if region is None:
            region = self.region

        if region is None:
            raise ValueError("region value is None")

        return (np.array(pyautogui.screenshot(region = region)))


    def get_screen_window_name(self, window_name = None):
        if window_name is None:
            window_name = self.window_name

        if window_name is None:
            raise ValueError("window name value is None")
        if  not isinstance(window_name, str):
            raise ValueError("window name should be string")
        elif len(window_name) < 1:
            raise ValueError("too shoort window name")

        win = pyautogui.getWindow(self.window_name)

        if win is not None:
            # win.resize(640, 640)
            # win.restore()
            print(win.get_position())
            image = pyautogui.screenshot(region = win.get_position())
            image = np.array(image)
            return(image)
        else:
            raise NameError("window wasn't found")

    # def find_and_save_window_name(self):
    #     input("Press enter and active window")
    #     time.sleep(1.5)
    #     self.name = win32gui.GetWindowText(win32gui.GetForegroundWindow())
