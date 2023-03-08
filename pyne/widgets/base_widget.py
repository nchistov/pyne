import pygame as pg


class Widget:
    def __init__(self):
        self.priority = 0

        self.rect = pg.Rect(0, 0, 1, 1)

    def set_rect(self, x: int, y: int, width: int, height: int):
        self.rect.x = x
        self.rect.y = y
        self.rect.width = width
        self.rect.height = height

    def hit(self, x: int, y: int):
        return self.rect.collidepoint(x, y)

    def update(self, event: pg.event.Event):
        pass

    def draw(self, screen: pg.Surface):
        pass
