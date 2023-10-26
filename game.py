#!/usr/bin/python3
import random

import pygame
from pygame import Rect

pygame.init()


class Game:

    def __init__(self, screen):

        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
        self.size = self.scr_width, self.scr_height

        # Background Game
        self.bg = pygame.image.load("images/starsbackground.jpg")
        self.bg = pygame.transform.scale(self.bg, (500, 500))
        self.bg_rect = self.bg.get_rect()

        # Clock
        self.clock = pygame.time.Clock()

        self.shapes = []

        # Init Shapes

        # Time Variables
        self.timecount_m = 0
        self.timecount = 0

        # Init Variables
        self.shape = None

        self.init_queue_shape = True
        self.first_shape_creation = True

        self.created_id = 0

        self.score = 0

    def draw_current_shape(self):

        for i, rect_sh in enumerate([self.shape]):
            if ((rect_sh.y + rect_sh.height) <= self.bg_rect.height):
                rect_sh.y += 5

            pygame.draw.rect(self.screen, "red", rect_sh)

    def run(self):
        mainloop = True
        while mainloop:

            self.clock.tick(40)
            self.screen.fill([0, 0, 0])
            self.screen.blit(self.bg, self.bg_rect)

            if self.shape is None:

                self.shape = Rect(0, 50, 50, 50)
                self.shape.x = 300 - self.shape.width / 2 - self.shape.x

            if self.shape is not None:

                self.draw_current_shape()

                if self.shape.y + self.shape.height == self.scr_height:
                    self.shape = None
                    break

            pygame.display.flip()
