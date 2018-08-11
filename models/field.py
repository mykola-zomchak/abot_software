from typing import List

from models.characters import *


class Field:
    def __init__(self, pacman: Pacman = None, enemies: List[Ghost] = None, bonus: bool = False,
                 cookies: List[Point] = None, powerups: List[Point] = None, round: int = 1, score: int = 0,
                 lives: int = 2):
        self.pacman = pacman
        self.enemies = enemies
        self.has_bonus = bonus
        self.cookies = cookies
        self.powerups = powerups
        self.round = round
        self.score = score
        self.lives = lives
        self.image = None
