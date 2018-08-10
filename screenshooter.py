import pyautogui
import numpy


class Screenshooter:

    def shot(self) -> numpy.ndarray:
        return numpy.array(pyautogui.screenshot())