#!/usr/bin/python3
import pygame
from game import Game

pygame.init()

screen = pygame.display.set_mode((500, 500), 0, 32)

# Settings
bg_color = (0, 0, 0)

mainloop = True
while mainloop:
    screen.fill(bg_color)

    g = Game(screen)
    g.run()

    pygame.display.flip()