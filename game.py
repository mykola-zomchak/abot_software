from selenium import webdriver
from consts import *


class Game:

    def __init__(self):
        self.driver = None

    def launch(self):
        self.__enter__()

    def __enter__(self):
        self.driver = webdriver.Chrome(DRIVER_LOCATION)
        self.driver.set_window_rect(GAME_X, GAME_Y, GAME_WIDTH, GAME_HEIGHT)
        self.driver.get(GAME_URL)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.close()
