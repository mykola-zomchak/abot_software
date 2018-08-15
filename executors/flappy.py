from executors.executor import Executor
from games.flappy.flappy import main, SCREENWIDTH, SCREENHEIGHT
import threading

class Flappy(Executor):
    window_name = "Flappy Bird"
    region = (100, 100, SCREENWIDTH, SCREENHEIGHT)

    def __init__(self):
      self.thread = threading.Thread(name="Flappy Bird", target=main)

    def __enter__(self):
      self.thread.start()
      return self

    def __exit__(self, exc_type, exc_val, exc_tb):
       # self.end_event.set()
       pass