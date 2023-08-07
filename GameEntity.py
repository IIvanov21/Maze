from abc import ABC, abstractmethod

class GameEntity(ABC):
    def __init__(self,x,y,symbol):
        self.x = x
        self.y = y
        self.symbol = symbol
    
    @abstractmethod
    def move(self,dx,dy):
        pass