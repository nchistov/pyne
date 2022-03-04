from .base_widget import Widget

import pygame as pg


class BeatleScreen(Widget):
    def __init__(self, app,  color=(255, 255, 255), outline_color=(150, 150, 150)):
        super().__init__()

        self.app = app

        self.color = color
        self.outline_color = outline_color

        self.beatle = None

        self.rect = pg.Rect(0, 0, 10, 10)

        self.surface = pg.Surface(self.rect.size)

    def set_rect(self, x, y, width, height):
        super().set_rect(x, y, width, height)

        self.surface = pg.Surface(self.rect.size)

    def add_beatle(self, beatle):
        self.beatle = beatle

    def draw(self, screen: pg.Surface):
        self.surface.fill(self.color)

        if self.beatle is not None:
            self.beatle.draw(self.surface)

        screen.blit(self.surface, self.rect)

        # Draw outlines
        pg.draw.line(screen, self.outline_color, (self.rect.x, self.rect.y), (self.rect.right, self.rect.y))
        pg.draw.line(screen, self.outline_color, (self.rect.right, self.rect.y), (self.rect.right, self.rect.bottom))
        pg.draw.line(screen, self.outline_color, (self.rect.right, self.rect.bottom),
                     (self.rect.left, self.rect.bottom))
        pg.draw.line(screen, self.outline_color, (self.rect.left, self.rect.bottom), (self.rect.x, self.rect.y))
