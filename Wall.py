from GameEntity import GameEntity

class Wall(GameEntity):
    def __init__(self, x, y):
        super().__init__(x, y, "#")

    def move(self, dx, dy):
        pass