"""
Графика Beatle, является упрошенной версией стандартного `turtle`.
"""

import os.path
from math import sin, cos, radians
from queue import Queue
from threading import Thread
from time import sleep
from typing import cast

import pygame as pg


class Beatle:
    """
    класс Beatle (аналог класса turtle.Pen)

    Атрибуты:
    screen: экземпляр класса pyne.widgets.BeatleScreen

    x: черепаший x
    y: черепаший y

    is_down: если True то Beatle рисует линию, иначе нет

    base_image: изображение предназначенное для поворота
    image: изображение отображаемое на экране

    rect: rect изображения

    speed: int
    angle: int

    tasks: экземпляр класса queue.Queue

    lines: список координат для рисования линий

    Методы:
    forward: двигает Beatle вперед на steps шагов
    backward: двигает Beatle назад на steps шагов

    setheading: устанавливает направление Beatle в angle углов

    down: изменяет флаг is_down в True
    up: изменяет флаг is_down в False
    stop: останавливает поток self.thread

    update: обновляет Beatle
    draw: рисует Beatle и линии
    """
    def __init__(self) -> None:
        self.x = 0
        self.y = 0

        self.base_x = 0
        self.base_y = 0

        self.is_down = False

        self.base_image = pg.image.load(os.path.join(os.path.dirname(__file__),
                                                     'images/beatle.png'))
        self.image = self.base_image

        self.rect = self.image.get_rect()
        self.rect.x = self.base_x + self.x
        self.rect.y = self.base_y + self.y

        self.speed = 5
        self.angle = 0

        self.tasks: Queue[tuple[str, int] | tuple[str]] = Queue(maxsize=10000)

        self.lines: list[tuple[tuple[float, float], tuple[float, float]]] = []

        self.thread = Thread(target=self.update)
        self._running = True
        self.thread.start()

    def forward(self, steps: int):
        self.tasks.put(('fd', steps))

    def backward(self, steps: int):
        self.forward(-steps)

    def setheading(self, angle: int):
        self.tasks.put(('seth', angle))

    def down(self):
        self.tasks.put(('down',))

    def up(self):
        self.tasks.put(('up',))

    def stop(self):
        self._running = False

    def home(self):
        self.tasks.put(('home',))

    def clear(self):
        self.tasks.put(('clear',))

    def reset(self):
        self.home()
        self.clear()

    def update(self):
        while self._running:
            if not self.tasks.empty():
                task = self.tasks.get()

                match task[0]:
                    case 'fd':
                        dx = cos(radians(cast(int, self.angle)))
                        dy = sin(radians(cast(int, self.angle)))
                        if self.is_down:
                            self.lines.append(((self.rect.centerx, self.rect.centery),
                                               (self.rect.centerx + dx, self.rect.centery - dy)))
                        for _ in range(cast(int, task[1])):
                            if self.is_down:
                                (start_x, start_y), _ = self.lines[-1]
                                self.lines[-1] = ((start_x, start_y),
                                                  (self.rect.centerx + dx, self.rect.centery - dy))
                            self.x += dx
                            self.y -= dy

                            self.rect.x = self.base_x + self.x
                            self.rect.y = self.base_y + self.y

                            sleep(0.05 / self.speed)

                    case 'seth':
                        self.angle = task[1]

                        self.angle %= 360

                        self.image = pg.transform.rotate(self.base_image, cast(int, self.angle))
                    case 'up':
                        self.is_down = False
                    case 'down':
                        self.is_down = True
                    case 'clear':
                        self.lines.clear()
                    case 'home':
                        self.setheading(0)

                        self.x = 0
                        self.y = 0

                        self.rect.x = self.base_x + self.x
                        self.rect.y = self.base_y + self.y

            sleep(0.02)

    def draw(self, screen: pg.Surface):
        screen.blit(self.image, self.rect)

        for line in self.lines:
            pg.draw.line(screen, (0, 0, 0), line[0], line[1])
