from models.characters import Ghost, Pacman
from models.parsed_screen import ParsedScreen

GHOSTS = ('Blinky', 'Pinky', 'Inky', 'Clyde')


class Field(ParsedScreen):
    pacman = Pacman()
    ghosts = {g: Ghost(g) for g in GHOSTS}
    has_bonus = False
    cookies = []
    powerups = []
    round = 1
    score = 0
    lives = 2
    image = None

    def update_pacman(self, coordinates):
        self.pacman.update(*coordinates)

    def update_ghost(self, name, coordinates):
        self.ghosts[name].update(*coordinates)
