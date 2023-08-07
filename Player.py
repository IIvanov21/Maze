from GameEntity import GameEntity


class Player(GameEntity):
    def __init__(self, x, y):
        super().__init__(x, y, "P")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy