from .base_widget import Widget

import pygame as pg


class BeatleScreen(Widget):
    def __init__(self,  color=(255, 255, 255), outline_color=(150, 150, 150)):
        super().__init__()

        self.color = color
        self.outline_color = outline_color

        self.beatles = []

        self.rect = pg.Rect(0, 0, 10, 10)

        self.surface = pg.Surface(self.rect.size)

    def set_rect(self, x, y, width, height):
        super().set_rect(x, y, width, height)

        self.surface = pg.Surface(self.rect.size)

    def add_beatle(self, beatle):
        self.beatles.append(beatle)

    def remove_beatle(self, beatle):
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
