from selenium import webdriver
from consts import *
from time import sleep
from action_executor import go_up

GAME_URL = 'file:///C:/Program%20Files/WindowsApps/40588MidwayStudios.PAC-MANOriginal_4.0.0.0_x64__svrvwanpjnagm' \
           '/pacman/index.html'
DRIVER_LOCATION = 'resource/chromedriver.exe'

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
