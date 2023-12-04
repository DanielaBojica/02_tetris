# A container for all the elements of the game
# Also contains method that manage the game's logic: update the shapes' position, checking for collisions etc.
# The code will be easier to understand, maintain, and expand later on
from tetris_oop_grid import Grid
from tetris_oop_shapes import *
import random

class Game:
    def __init__(self):
        self.grid = Grid()
        self.shapes = [IShape, JShape, LShape, OShape, SShape, ZShape,TShape]

    # we create a method to get random shapes
    def get_random_shape(self):
        if len(self.shapes) == 0:
            self.shapes = [IShape, JShape, LShape, OShape, SShape, ZShape, TShape]
        shape = random.choice(self.shapes)
        self.shapes.remove(shape)
        return shape

