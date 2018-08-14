from consts import *
import sys
import os

project_dir = os.getcwd()
sys.path.insert(0, project_dir + "\\games\\flappy")
print(project_dir)
from flappy import main

import threading

class Game:

    def __init__(self):
       pass

    def launch(self):
        self.__enter__()

    def __enter__(self):
      t = threading.Thread(target=main, name='Flappy Bird')
      t.daemon = True
      t.start()
      return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
