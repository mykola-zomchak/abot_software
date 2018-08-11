from consts import *


class Game:

    def __init__(self):
        self.driver = None

    def launch(self):
        self.__enter__()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
