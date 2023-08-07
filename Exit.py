from GameEntity import GameEntity


class Exit(GameEntity):
    def __init__(self, x, y):
        super().__init__(x, y, "E")

    def move(self, dx, dy):
        pass