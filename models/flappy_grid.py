from models.parsed_screen import ParsedScreen
import numpy as np

class FlappyGrid(ParsedScreen):
    image = None
    grid = np.zeros(shape = (50,50))


    def __init__(self):
      pass
