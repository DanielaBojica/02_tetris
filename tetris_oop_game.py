# A container for all the elements of the game
# Also contains method that manage the game's logic: update the shapes' position, checking for collisions etc.
# The code will be easier to understand, maintain, and expand later on
from tetris_oop_grid import Grid
from tetris_oop_shapes import *
import random


class Game:
    def __init__(self):
        self.grid = Grid()
        self.shapes = [IShape(), JShape(), LShape(), OShape(), SShape(), ZShape(), TShape()]
        self.current_shape = self.get_random_shape()
        self.next_shape = self.get_random_shape()

    # we create a method to get random shapes
    def get_random_shape(self):
        if len(self.shapes) == 0:
            self.shapes = [IShape(), JShape(), LShape(), OShape(), SShape(), ZShape(), TShape()]
        shape = random.choice(self.shapes)
        self.shapes.remove(shape)
        return shape

    def move_left(self):
        self.current_shape.move(0, -1)

    def move_right(self):
        self.current_shape.move(0, 1)

    def move_down(self):
        self.current_shape.move(1, 0)

    def shape_inside(self):
        tiles = self.current_shape.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.col) == False:
                return False
            return True

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_shape.draw(screen)
