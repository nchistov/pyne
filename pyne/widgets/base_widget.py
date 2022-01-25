import pygame as pg


class Widget:
    def __init__(self):
        self.rect = pg.Rect(0, 0, 1, 1)

    def update(self, event):
        pass

    def draw(self, screen: pg.Surface):
        pass