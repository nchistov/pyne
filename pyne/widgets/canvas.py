import pygame as pg

from .base_widget import Widget


class Canvas(Widget):
    def __init__(self, bg_color=(255, 255, 255)):
        super().__init__()

        self.bg_color = bg_color

        self.objects  = []

    def draw(self, screen: pg.Surface):
        for obj in self.objects:
            obj.draw()
