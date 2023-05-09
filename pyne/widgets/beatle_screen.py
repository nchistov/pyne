from typing import NewType

import pygame as pg

from .base_widget import Widget

# Класс pyne.widgets.Beatle не получается импортировать из-за циклического импорта.
Beatle = NewType('Beatle', Widget)


class BeatleScreen(Widget):
    def __init__(self, color: tuple[int, int, int] = (255, 255, 255),
                 outline_color: tuple[int, int, int] = (150, 150, 150), name: str = ''):
        super().__init__(name=name)

        self.color = color
        self.outline_color = outline_color

        self.beatles: list[Beatle] = []

        self.rect = pg.Rect(0, 0, 10, 10)

        self.surface = pg.Surface(self.rect.size)

    def set_rect(self, x: int, y: int, width: int, height: int):
        super().set_rect(x, y, width, height)

        self.surface = pg.Surface(self.rect.size)

    def add_beatle(self, beatle: Beatle):
        self.beatles.append(beatle)

    def remove_beatle(self, beatle: Beatle):
        if beatle in self.beatles:
            self.beatles.remove(beatle)

    def draw(self, screen: pg.Surface):
        self.surface.fill(self.color)

        for beatle in self.beatles:
            beatle.draw(self.surface)

        screen.blit(self.surface, self.rect)

        # Рисуем рамку
        pg.draw.line(screen, self.outline_color, (self.rect.x, self.rect.y), (self.rect.right, self.rect.y))
        pg.draw.line(screen, self.outline_color, (self.rect.right, self.rect.y), (self.rect.right, self.rect.bottom))
        pg.draw.line(screen, self.outline_color, (self.rect.right, self.rect.bottom),
                     (self.rect.left, self.rect.bottom))
        pg.draw.line(screen, self.outline_color, (self.rect.left, self.rect.bottom), (self.rect.x, self.rect.y))
