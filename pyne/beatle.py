import os.path
from math import sin, cos, radians

import pygame as pg


class Beatle:
    def __init__(self,  beatle_screen):
        self.app = beatle_screen.app

        self.screen = beatle_screen

        self.x = 0
        self.y = 0

        self.image = pg.image.load(os.path.join(os.path.dirname(__file__), 'beatle.png'))

        self.rect = self.image.get_rect()
        self.rect.centerx = beatle_screen.rect.centerx
        self.rect.centery = beatle_screen.rect.centery

        self.speed = 5
        self.angle = 0

        self.end_point = None

        self.moving = False

    def forward(self, steps):
        self.dx = self.speed * cos(radians(self.angle))
        self.dy = self.speed * sin(radians(self.angle))

        self.end_point = (steps * cos(radians(self.angle)), steps * sin(radians(self.angle)))

        self.moving = True

    def setheading(self, angle):
        self.angle = angle

        self.image = pg.transform.rotate(self.image, self.angle)

    def draw(self):
        if self.moving and self.rect.center != self.end_point:
            self.rect.x += self.dx
            self.rect.x += self.dy

            self.x += self.dx
            self.y += self.dy

        self.screen.blit(self.image, self.rect)
