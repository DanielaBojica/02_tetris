import pygame

pygame.init()

screen = pygame.display.set_mode((600, 800))
rectangular = pygame.Surface((100, 200))
rectangular.fill((255, 102, 255))

#We add an image, which is a surface. We can do without convert() also.
bg = pygame.image.load("ship.bmp").convert()

while True:
    screen.fill((128, 255, 128))
    # we blit the second object we created
    screen.blit(bg, (10, 10))
    # This is the first image we create
    screen.blit(rectangular, (100, 100))
    if pygame.event.get(pygame.QUIT):
        break
    pygame.display.update()

pygame.quit()