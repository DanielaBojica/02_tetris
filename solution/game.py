#!/usr/bin/python3
import random

import pygame

from oop_5.exercise_2.factory import ShapeFactory

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

    def create_new_shape(self, new_shape_builder):

        if new_shape_builder == "normal":
            self.shape = ShapeFactory.generate_new_shape()
        else:
            shape1 = ShapeFactory.generate_new_shape()
            shape2 = ShapeFactory.generate_new_shape()
            self.shape = ShapeFactory.generate_combined_shape(
                shape1,
                shape2
            )

    def draw_current_shape(self):

        for i, rect_sh in enumerate(self.shape.shape_list):
            if ((rect_sh.y + rect_sh.height) <= self.bg_rect.height):
                rect_sh.y += 5

            pygame.draw.rect(self.screen, self.shape.color, rect_sh)

    def run(self):
        mainloop = True
        while mainloop:

            self.clock.tick(40)
            self.screen.fill([0, 0, 0])
            # pygame.display.flip()
            self.screen.blit(self.bg, self.bg_rect)

            if self.shape is None:
                new_shape_builder = random.choice(["normal", "custom"])
                self.create_new_shape(new_shape_builder)

            if self.shape is not None:

                self.draw_current_shape()

                for rect in self.shape.shape_list:

                    if rect.y + rect.height == self.scr_height:
                        self.shape = None
                        print("booooom end")
                        break
            pygame.display.flip()
