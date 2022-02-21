import pygame as pg

from .base_widget import Widget

from ._canvas_object import CanvasObject


class Canvas(Widget):
    def __init__(self, bg_color=(255, 255, 255)):
        super().__init__()

        self.bg_color = bg_color

        self.objects = []

    def draw_point(self, x: int, y: int, color=(0, 0, 0)):
        new_obj = CanvasObject(('point', (self.rect.x + x, self.rect.y + y), color))
        self.objects.append(new_obj)

    def draw_line(self, x1, y1, x2, y2, color=(0, 0, 0), width=1):
        new_obj = CanvasObject(('line', (self.rect.x + x1, self.rect.y + y1), (self.rect.x + x2, self.rect.y + y2),
                                color, width))
        self.objects.append(new_obj)

    def draw_rect(self, x, y, width, height, color=(0, 0, 0)):
        new_obj = CanvasObject(('rect', (self.rect.x + x, self.rect.y + y), width, height, color))
        self.objects.append(new_obj)

    def draw_circle(self, x, y, R, color=(0, 0, 0)):
        new_obj = CanvasObject(('circle', (self.rect.x + x, self.rect.y + y), R, color))
        self.objects.append(new_obj)

    def draw(self, screen: pg.Surface):
        pg.draw.rect(screen, self.bg_color, self.rect)

        for obj in self.objects:
            obj.draw(screen)
