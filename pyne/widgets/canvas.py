import pygame as pg

from .base_widget import Widget

from ._canvas_object import CanvasObject


class Canvas(Widget):
    def __init__(self, bg_color=(255, 255, 255)):
        super().__init__()

        self.bg_color = bg_color

        self.objects = []

    def point(self, x: int, y: int, color=(0, 0, 0)):
        new_obj = CanvasObject(('point', (self.rect.x + x, self.rect.y + y), color))
        self.objects.append(new_obj)

    def draw(self, screen: pg.Surface):
        pg.draw.rect(screen, self.bg_color, self.rect)

        for obj in self.objects:
            obj.draw(screen)
