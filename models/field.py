from typing import List

from models.characters import *


class Field:
    def __init__(self):
        self.pacman = Pacman()
        self.ghosts = {g: Ghost(g) for g in GHOSTS}
        self.has_bonus = False
        self.cookies = []
        self.powerups = []
        self.round = 1
        self.score = 0
        self.lives = 2
        self.image = None

    def update_pacman(self, coordinates):
        self.pacman.update(*coordinates)

    def update_ghost(self, name,  coordinates):
        self.ghosts[name].update(*coordinates)

GHOSTS = ('Blinky', 'Pinky', 'Inky', 'Clyde')
