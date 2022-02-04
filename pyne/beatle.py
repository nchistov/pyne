import os.path
from math import sin, cos, radians
from queue import Queue
from threading import Thread
from time import sleep

import pygame as pg


class Beatle:
    def __init__(self,  beatle_screen):
        self.app = beatle_screen.app

        self.screen = beatle_screen

        self.x = 0
        self.y = 0

        self.base_image = pg.image.load(os.path.join(os.path.dirname(__file__), 'beatle.png'))
        self.image = self.base_image

        self.rect = self.image.get_rect()
        self.rect.center = beatle_screen.rect.center

        self.speed = 5
        self.angle = 0
        self.steps = 0

        self.moving = False

        self.tasks = Queue(maxsize=10000)

        t = Thread(target=self.update)
        self._running = True
        t.start()
        self.thread = t

        self.app.add_to_schedule(self.draw)

    def forward(self, steps):
        self.tasks.put(('fd', steps))

    def setheading(self, angle):
        self.tasks.put(('seth', angle))

    def update(self):
        while self._running:
            if not self.tasks.empty():
                task = self.tasks.get()

                if task[0] == 'fd':
                    dx = self.speed * cos(radians(self.angle))
                    dy = self.speed * sin(radians(self.angle))
                    for i in range(task[1] // self.speed):
                        self.rect.x += dx
                        self.rect.y -= dy

                        self.x += dx
                        self.y -= dy

                        sleep(0.02)

                elif task[0] == 'seth':
                    self.angle = task[1]

                    if self.angle != self.angle % 360:
                        self.angle %= 360
                    else:
                        self.angle %= -360

                    self.image = pg.transform.rotate(self.base_image, self.angle)

                self.moving = False

            sleep(0.02)

    def stop(self):
        self._running = False

    def draw(self):
        self.app.screen.blit(self.image, self.rect)
