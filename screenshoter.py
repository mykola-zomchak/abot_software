import pyautogui
import numpy


def shot() -> numpy.ndarray:
    return numpy.array(pyautogui.screenshot())
