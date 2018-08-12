from selenium import webdriver
from time import sleep
import os

from action_executor import go_up
from executors.web_executor import WebExecutor

GAME_URL = 'file:///' + os.getcwd() + '/games/pacman/pacman.html'


class Pacman(WebExecutor):
    driver = None
    window_name = 'pacman.html'
    region = 800, 0, 1100, 1000

    def launch(self):
        self.__enter__()

    def __enter__(self):
        self.driver = webdriver.Chrome(self.driver_location)
        self.driver.set_window_rect(*self.region)
        self.driver.get(GAME_URL)
        sleep(1)
        go_up()
        sleep(1)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.close()
