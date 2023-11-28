import pygame
import sys
from tetris_oop_grid import Grid

pygame.init()
dark_blue = (0, 0, 102)

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

grid = Grid()
grid.print_grid()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(dark_blue)
    grid.draw(screen)
    pygame.display.flip()
    clock.tick(60)
