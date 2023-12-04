import pygame
import sys
from tetris_oop_grid import Grid
from tetris_oop_shapes import *

pygame.init()
dark_blue = (44, 44, 127)

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

game_grid = Grid()

shape = TShape()
shape.move(4, 3)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(dark_blue)
    game_grid.draw(screen)
    shape.draw(screen)

    pygame.display.flip()
    clock.tick(60)
