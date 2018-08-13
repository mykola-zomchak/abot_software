from models.point import Point


class Character(Point):

    def __init__(self, name: str = 'character', x: int = 0, y: int = 0):
        super().__init__(x, y)
        self.name = name

    def update(self, x: int, y: int):
        if x < 0 or y < 0:
            return
        self.x = x
        self.y = y

    def xy(self):
        return self.x, self.y

class Pacman(Character):

    def __init__(self, x: int = 0, y: int = 0):
        super().__init__('Pacman', x, y)


class Ghost(Character):

    def __init__(self, name: str = 'ghost', x: int = 0, y: int = 0):
        super().__init__(name, x, y)
        self.blue = False
