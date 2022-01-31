import os.path
from math import sin, cos, radians
from threading import Thread
from time import sleep

import pygame as pg


class Beatle:
    def __init__(self,  beatle_screen):
        self.app = beatle_screen.app

        self.screen = beatle_screen

        self.x = 0
        self.y = 0

        self.image = pg.image.load(os.path.join(os.path.dirname(__file__), 'beatle.png'))

        self.rect = self.image.get_rect()
        self.rect.center = beatle_screen.rect.center

        self.speed = 5
        self.angle = 0
        self.steps = 0

        self.end_point = None

        self.moving = False

        t = Thread(target=self.update)
        self._running = True
        t.start()
        self.thread = t

        self.app.add_to_schedule(self.draw)

    def forward(self, steps):
        self.steps = steps

        self.moving = True

    def setheading(self, angle):
        self.angle = angle

        self.image = pg.transform.rotate(self.image, self.angle)

    def update(self):
        while self._running:
            if self.moving:
                dx = self.speed * cos(radians(self.angle))
                dy = self.speed * sin(radians(self.angle))
                for i in range(self.steps // self.speed):
                    self.rect.x += dx
                    self.rect.y -= dy

                    sleep(0.02)
                self.moving = False

            sleep(0.02)

    def stop(self):
        self._running = False

    def draw(self):
        self.app.screen.blit(self.image, self.rect)
