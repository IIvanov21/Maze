from abc import ABC, abstractmethod
import math

class GameEntity(ABC):
    def __init__(self,x,y,symbol):
        self.x = x
        self.y = y
        self.symbol = symbol
    
    @abstractmethod
    def move(self,dx,dy):
        pass

    def adjacent(self, x, y) -> bool:
        """
        Add way to check if entity is adjacent to another set of
        coordinates - note this could be a boundary.
        """
        if math.dist([self.x, self.y], [x, y]) > 1:
           return False
        return true
