import pygame
from Maze import Maze
from Wall import Wall
from Player import Player
from Exit import Exit
import sys
import random

class GameEngine:
    def __init__(self):
        self.maze_width = 20
        self.maze_height = 20
        self.maze = Maze(self.maze_width,self.maze_height, [0, 0], [self.maze_width-1, self.maze_height+-1]) #Change the maze dimensions as needed
        self.numOfWalls=120
        self.player = Player(self.maze.start_position[0],self.maze.start_position[1])
        self.entities = [self.player, Wall(2, 1), Wall(3, 1), Wall(4, 1), Exit(self.maze.exit_position[0], self.maze.exit_position[1])]
        # Screen now Game Engine attribute
        self._screen = None
        # Create a specific dicitionary for obstacles
        self._obstacles = dict()
    
    def add_walls(self):
        """
        This adds the random walls to the game engine
        """

        # Create an easy local reference for the already initialised entities
        it = self.entities

        # Create a dictionary for the entities using their coordinates as a key
        # this allows a lazy check of coordinate collisions against all entities
        entity_dict = { (itr.x, itr.y) : itr for itr in it }

        # This creates a dictionary specifically for wall instances that will now
        # be added as random entries in this function
        wall_dict = dict()

        # Create a dictionary of obstacles - make list of walls all ready preset
        # as a base.
        list_obstacles = [elm for elm in self.entities if isinstance(elm, Wall)]

        # Iterate the number of new walls that need to be created
        for random_wall_count in range(0, self.numOfWalls):

            # Create a counter for the number of attempts at placing a wall, note
            # if a wall overlaps then a new position should be contemplated.
            _iter_count = 0

            # Create random coordinates for wall
            _x = random.randint(1, self.maze_width)
            _y = random.randint(1, self.maze_height)

            # Iterate random coordinates if coordinates are already taken in entity
            # dictionary
            while (_x, _y) in entity_dict and _iter_count < 100:
                _x = random.randint(1, self.maze_width)
                _y = random.randint(1, self.maze_height)

            # If the iteration count is 100 then assume that no placement is actually
            # avaialable
            if _iter_count == 100:
               # Raise an exception and break the wall placement loop since it won't
               # be possible to place any more
               raise Exception("Couldn't place the wall in a reasonable time!")
               break

            # Append a new dictionary item for a new Wall instance
            wall_dict[(_x, _y)] = Wall(_x,_y)

        # Iterate the wall dictionary and add the items to both the entities and the
        # list of obstacles for incorporation later
        for (key_x, key_y), value in wall_dict.items():
            self.entities.append(value)
            list_obstacles.append(value)

        # Create a master dictionary of obstacles
        self._obstacles = { (itr.x, itr.y) : itr for itr in list_obstacles }
    
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.move_player(0, -1)
                elif event.key == pygame.K_DOWN:
                    self.move_player(0, 1)
                elif event.key == pygame.K_LEFT:
                    self.move_player(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    self.move_player(1, 0)
                    
    def move_player(self, dx, dy):
        new_x, new_y = self.player.x + dx, self.player.y + dy

        # Check if new poisiton would be in obstacle - if so don't bother
        if (new_x, new_y) in self._obstacles:
            return

        if 0 <= new_x < self.maze.width and 0 <= new_y < self.maze.height and self.maze.maze_layout[new_y][new_x] == 0:
            self.player.move(dx, dy)

    def check_win_condition(self):
        if self.maze.is_exit_reached((self.player.x, self.player.y)):
            print("Congratulations! You've reached the exit.")
            pygame.quit()
            sys.exit()

    def run_game(self):
        pygame.init()
        # set the screen attribute
        self._screen = pygame.display.set_mode((self.maze.width * 30, self.maze.height * 30))
        # Set the screen attribute in the maze
        self.maze.screen = self._screen
        pygame.display.set_caption("Maze Game")
        self.add_walls()
        while True:
            self.handle_input()
            self.check_win_condition()

            self._screen.fill((255, 255, 255))

            for entity in self.entities:
                pygame.draw.rect(self._screen, (0, 0, 0), (entity.x * 30, entity.y * 30, 30, 30))

            pygame.draw.rect(self._screen, (0, 255, 0), (self.player.x * 30, self.player.y * 30, 30, 30))

            pygame.display.flip()

if __name__ == "__main__":
    game_engine = GameEngine()
    game_engine.run_game()
