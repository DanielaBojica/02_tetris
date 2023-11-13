import pygame
import sys
import random

def generate_random_shape():
    rand_shape = random.randrange(1, 3)
    if rand_shape == 1:     # S-Shape
        pygame.draw.rect(screen, shape_color, (50, count_offset, 50, 50))
        pygame.draw.rect(screen, shape_color, (100, count_offset, 50, 50))
        pygame.draw.rect(screen, shape_color, (0, count_offset + 50, 50, 50))
        pygame.draw.rect(screen, shape_color, (50, count_offset + 50, 50, 50))

    elif rand_shape == 2:   # U-Shape
        pygame.draw.rect(screen, shape_color, (0, count_offset, 50, 50))
        pygame.draw.rect(screen, shape_color, (100, count_offset, 50, 50))
        pygame.draw.rect(screen, shape_color, (0, count_offset + 50, 50, 50))
        pygame.draw.rect(screen, shape_color, (50, count_offset + 50, 50, 50))
        pygame.draw.rect(screen, shape_color, (100, count_offset+50, 50, 50))

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

# We set the variable count_flicker for flickering
count_flicker = 0

# We set the count_offset for the movement offset
count_offset = 0
# 2. GAME LOOP
while True:
    # Establish when the game is over, to avoid infinite loops
    for event in pygame.event.get():      # the method makes a list, and we iterate through it
        if event.type == pygame.QUIT:
            pygame.quit()  # quits the pygame software
            sys.exit()  # closes the window

    # The appearance of the screen
    screen.fill('black')

    rand_color = random.randrange(1, 5)
    if rand_color == 1:
        shape_color = 'red'
    elif rand_color == 2:
        shape_color = 'blue'
    elif rand_color == 3:
        shape_color = 'orange'
    elif rand_color == 4:
        shape_color = 'green'
        rand_color = 0
    count_flicker += 1

    # Draw the game object(s) on the screen:
    # A BALL
    # pygame.draw.ellipse(screen, shape_color, ball)

    # A red S-SHAPE
    # pygame.draw.rect(screen, shape_color, (50, 0, 50, 50))
    # pygame.draw.rect(screen, shape_color, (100, 0, 50, 50))
    # pygame.draw.rect(screen, shape_color, (0, 50, 50, 50))
    # pygame.draw.rect(screen, shape_color, (50, 50, 50, 50))

    # A moving downwards red S_SHAPE
    # pygame.draw.rect(screen, 'red', (50, count_offset, 50, 50))
    # pygame.draw.rect(screen, 'red', (100, count_offset, 50, 50))
    # pygame.draw.rect(screen, 'red', (0, count_offset+50, 50, 50))
    # pygame.draw.rect(screen, 'red', (50, count_offset+50, 50, 50))
    generate_random_shape()
    count_offset += 20

    clock.tick(2)

    pygame.display.flip()
    # pygame.display.update()
    # clock.tick(60)
    # 60 frames per second - this sets a constant speed of the objects on the screen
    # otherwise, they would move at the speed of the computer - as fast as it can
    # afford at a certain time, therefore not constant.




