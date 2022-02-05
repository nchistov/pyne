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

        self.is_down = True

        self.base_image = pg.image.load(os.path.join(os.path.dirname(__file__), 'beatle.png'))
        self.image = self.base_image

        self.rect = self.image.get_rect()
        self.rect.x = self.screen.rect.centerx + self.x
        self.rect.y = self.screen.rect.centery + self.y

        self.speed = 5
        self.angle = 0
        self.steps = 0

        self.tasks = Queue(maxsize=10000)

        self.lines = []

        t = Thread(target=self.update)
        self._running = True
        t.start()
        self.thread = t

        self.app.add_to_schedule(self.draw)

    def forward(self, steps):
        self.tasks.put(('fd', steps))

    def backward(self, steps):
        self.forward(-steps)

    def setheading(self, angle):
        self.tasks.put(('seth', angle))

    def down(self):
        self.is_down = True

    def up(self):
        self.is_down = False

    def update(self):
        while self._running:
            if not self.tasks.empty():
                task = self.tasks.get()

                if task[0] == 'fd':
                    dx = cos(radians(self.angle))
                    dy = sin(radians(self.angle))
                    if self.is_down:
                        self.lines.append(((self.rect.centerx, self.rect.centery),
                                           (self.rect.centerx + dx, self.rect.centery - dy)))
                    for i in range(task[1]):
                        if self.is_down:
                            (start_x, start_y), _ = self.lines[-1]
                            self.lines[-1] = ((start_x, start_y),
                                              (self.rect.centerx + dx, self.rect.centery - dy))
                        self.x += dx
                        self.y -= dy

                        self.rect.x = self.screen.rect.centerx + self.x
                        self.rect.y = self.screen.rect.centery + self.y

                        sleep(0.05 / self.speed)

                elif task[0] == 'seth':
                    self.angle = task[1]

                    self.angle %= 360

                    self.image = pg.transform.rotate(self.base_image, self.angle)

            sleep(0.02)

    def stop(self):
        self._running = False

    def draw(self):
        self.app.screen.blit(self.image, self.rect)

        for line in self.lines:
            pg.draw.line(self.app.screen, (0, 0, 0), line[0], line[1])
