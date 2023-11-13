import pygame
import sys
import random

pygame.init()

# 1. DEFINITIONS
screen_width = 600
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Tetris Game!")

# The clock sets a uniform speed
clock = pygame.time.Clock()

# We put a ball on the screen
ball = pygame.Rect(120, 200, 50, 50)

# We set the variable count for flickering
count = 0


# 2. GAME LOOP
while True:
    # Establish when the game is over, to avoid infinite loops
    for event in pygame.event.get():      # the method makes a list, and we iterate through it
        if event.type == pygame.QUIT:
            pygame.quit()  # quits the pygame software
            sys.exit()  # closes the window

    # The appearance of the screen
    screen.fill('black')

    # Draw the game object(s) on the screen:
    # A BALL
    pygame.draw.ellipse(screen, 'red', ball)

    clock.tick(60)
    # 60 frames per second - this sets a constant speed of the objects on the screen
    # otherwise, they would move at the speed of the computer - as fast as it can
    # afford at a certain time, therefore not constant.
    pygame.display.flip()
    # pygame.display.update()
    # clock.tick(60)





