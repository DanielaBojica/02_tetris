import pygame
from tetris_nick_colors import Colors
from tetris_nick_position import Position


class Shape:
    def __init__(self, id):
        self.id = id
        self.cell_size = 30
        self.cells_rotations = {}  # a dictionary keys=rotation position 0-3, values=list of coordinates of each rect
        self.rotation_state = 0  # which is included in self.cells_rotations as the first key
        self.colors = Colors.get_cell_colors()  # a list whose indexes will be self.id's

    def draw(self, screen):
        tiles = self.cells_rotations[self.rotation_state]
        for tile in tiles:
            tile_rect = pygame.Rect(tile.col * self.cell_size + 1, tile.row * self.cell_size + 1, self.cell_size - 1,
                                    self.cell_size - 1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)


class LShape(Shape):
    def __init__(self):
        super().__init__(id = 1)
        self.cells_rotations = {
            0: [Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 0)],
            3: [Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)]
        }


class JShape(Shape):
    def __init__(self):
        super().__init__(id=2)
        self.cells_rotations = {
            0: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 2)],
            3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)]
        }


class IShape(Shape):
    def __init__(self):
        super().__init__(id=3)
        self.cells_rotations = {
            0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],
            1: [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],
            2: [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)],
            3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)]
        }


class OShape(Shape):
    def __init__(self):
        super().__init__(id=4)
        self.cells_rotations = {
            0: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)],
        }


class SShape(Shape):
    def __init__(self):
        super().__init__(id=5)
        self.cells_rotations = {
            0: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],
            2: [Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1)],
            3: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)]
        }


class TShape(Shape):
    def __init__(self):
        super().__init__(id=6)
        self.cells_rotations = {
            0: [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 1)]
        }


class ZShape(Shape):
    def __init__(self):
        super().__init__(id=7)
        self.cells_rotations = {
            0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],
            1: [Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(2, 1), Position(2, 2)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 0)]
        }

