# import pygame
# import sys
# import random
#
# def generate_random_shape():
#     rand_shape = random.randrange(1, 3)
#     if rand_shape == 1:     # S-Shape
#         pygame.draw.rect(screen, shape_color, (50, count_offset, 50, 50))
#         pygame.draw.rect(screen, shape_color, (100, count_offset, 50, 50))
#         pygame.draw.rect(screen, shape_color, (0, count_offset + 50, 50, 50))
#         pygame.draw.rect(screen, shape_color, (50, count_offset + 50, 50, 50))
#
#     elif rand_shape == 2:   # U-Shape
#         pygame.draw.rect(screen, shape_color, (0, count_offset, 50, 50))
#         pygame.draw.rect(screen, shape_color, (100, count_offset, 50, 50))
#         pygame.draw.rect(screen, shape_color, (0, count_offset + 50, 50, 50))
#         pygame.draw.rect(screen, shape_color, (50, count_offset + 50, 50, 50))
#         pygame.draw.rect(screen, shape_color, (100, count_offset+50, 50, 50))
#
#
# pygame.init()
#
# # 1. DEFINITIONS
# screen_width = 600
# screen_height = 800
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("My Tetris Game!")
#
# # The clock sets a uniform speed
# clock = pygame.time.Clock()
#
# # We put a ball on the screen
# ball = pygame.Rect(120, 200, 50, 50)
#
# # We set the variable count_flicker for flickering
# count_flicker = 0
#
# # We set the count_offset for the movement offset
# count_offset = 0
# # 2. GAME LOOP
# while True:
#     # Establish when the game is over, to avoid infinite loops
#     for event in pygame.event.get():      # the method makes a list, and we iterate through it
#         if event.type == pygame.QUIT:
#             pygame.quit()  # quits the pygame software
#             sys.exit()  # closes the window
#
#    # The appearance of the screen
#     screen.fill('black')
#
#     rand_color = random.randrange(1, 5)
#     if rand_color == 1:
#         shape_color = 'red'
#     elif rand_color == 2:
#         shape_color = 'blue'
#     elif rand_color == 3:
#         shape_color = 'orange'
#     elif rand_color == 4:
#         shape_color = 'green'
#         rand_color = 0
#     count_flicker += 1

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
    # generate_random_shape()
    #
    # count_offset += 20
    #
    # clock.tick(2)
    #
    # pygame.display.flip()
    # pygame.display.update()
    # clock.tick(60)
    # 60 frames per second - this sets a constant speed of the objects on the screen
    # otherwise, they would move at the speed of the computer - as fast as it can
    # afford at a certain time, therefore not constant.

#------------------------------------------------
# A different approach
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 500, 600
SCREEN_SIZE = (WIDTH, HEIGHT)
BLOCK_SIZE = 50
# FPS = 6

# Colors
BLACK = (0, 0, 0)
FUCHSIA = (255, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Initialize the screen
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Simple Colored Tetris")

clock = pygame.time.Clock()

# Define the shapes
shapes = [
    {"shape": [[1, 1, 1], [0, 1, 0]], "color": RED},
    {"shape": [[1, 1, 1, 1]], "color": GREEN},
    {"shape": [[1, 0, 1], [1, 1, 1]], "color": BLUE},
    {"shape": [[0, 1, 1], [1, 1, 0]], "color": YELLOW},
    {"shape": [[1, 1], [1, 1]], "color": FUCHSIA},
]


def draw_shape(surface, shape, x, y, color):
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col] == 1:
                pygame.draw.rect(surface, color, (x + col * BLOCK_SIZE, y + row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))


def generate_shape():
    return random.choice(shapes)


def main():
    # Initial shape
    current_shape = generate_shape()
    current_x = WIDTH // 2 - (len(current_shape["shape"][0]) * BLOCK_SIZE // 2)
    current_y = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Moving the shapes
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and current_x > 0:
            current_x -= BLOCK_SIZE
        if keys[pygame.K_RIGHT] and current_x < WIDTH - len(current_shape["shape"][0]) * BLOCK_SIZE:
            current_x += BLOCK_SIZE

        # Update the position of the shape
        current_y += BLOCK_SIZE

        # Check if the shape has reached the bottom
        if current_y >= HEIGHT:
            current_shape = generate_shape()
            current_x = WIDTH // 2 - len(current_shape['shape'][0]) * BLOCK_SIZE // 2
            current_y = 0

        # Clear the screen
        screen.fill(BLACK)

        # Draw the current shape
        draw_shape(screen, current_shape['shape'], current_x, current_y, current_shape["color"])

        # Update the display
        # pygame.display.flip()

        # Cap the frame rate

        clock.tick(4)
        # Update the display
        pygame.display.flip()


if __name__ == "__main__":
    main()





