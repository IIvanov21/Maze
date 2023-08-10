import random
import pygame
from typing import Tuple

class Maze:
    def __init__(self,width,height, start: Tuple[int, int], exit: Tuple[int, int]):
        # Width and Height added as retained attributes
        self.width=width
        self.height=height
        self.wall_density=0.3
        self.maze_layout=[[0 for _ in range (width)]for _ in range(height)]
        self.start_position=(start[0],start[1])
        self.exit_position = (exit[0],exit[1])
        self.screen_height=600
        self.screen_width=800
        # Screen reference added as retained attribute
        self._screen=None

    @property
    def screen(self):
        """
        Screen reference for maze rendering
        """
        return self._screen

    @screen.setter
    def screen(self, screen):
        """
        Screen reference set after Maze constructed
        """
        self._screen = screen

    def generate_maze(self):
        #Add walls randomly
        for row in range(self.height):
            for col in range (self.width):
                if random.random()< self.wall_density:
                    self.maze_layout[row][col]=1
                    
    def draw_maze(self):
        cell_width= self.screen_width/self.width
        cell_height=self.screen_height/self.height
        
        for row in range(self.height):
            for col in range(self.width):
                if self.maze_layout[row][col] == 1:
                    pygame.draw.rect(self.screen,(0,0,0),(col*cell_width,row*cell_height,cell_width,cell_height))
                else:
                    pygame.draw.rect(self.screen, (255,255,255),(col*cell_width,row *cell_height,cell_width,cell_height))
    
    def is_exit_reached(self, player_position):
        return player_position==self.exit_position
