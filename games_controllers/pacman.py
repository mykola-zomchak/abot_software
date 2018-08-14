from selenium import webdriver
from consts import *
from time import sleep
from action_executor import go_up
import os

path = os.getcwd()
project_dir = path

GAME_URL = 'file:///' + project_dir + '/games/pacman/pacman.html'
DRIVER_LOCATION = project_dir + '/resource/chromedriver.exe'

class Game:

    def __init__(self):
        self.driver = None

    def launch(self):
        self.__enter__()

    def __enter__(self):
        self.driver = webdriver.Chrome(DRIVER_LOCATION)
        self.driver.set_window_rect(GAME_X, GAME_Y, GAME_WIDTH, GAME_HEIGHT)
        self.driver.get(GAME_URL)
        sleep(1)
        go_up()
        sleep(2)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.close()
