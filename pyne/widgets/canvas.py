import pygame as pg

from .base_widget import Widget

from ._canvas_object import CanvasObject


class Canvas(Widget):
    def __init__(self, bg_color=(255, 255, 255)):
        super().__init__()

        self.bg_color = bg_color

        self.objects = []

    def draw_point(self, x: int, y: int, color=(0, 0, 0)) -> int:
        new_obj = CanvasObject(('point', (self.rect.x + x, self.rect.y + y), color))
        self.objects.append(new_obj)

        return len(self.objects) - 1

    def draw_line(self, x1: int, y1: int, x2: int, y2: int, color=(0, 0, 0), width=1) -> int:
        new_obj = CanvasObject(('line', (self.rect.x + x1, self.rect.y + y1), (self.rect.x + x2, self.rect.y + y2),
                                color, width))
        self.objects.append(new_obj)

        return len(self.objects) - 1

    def draw_rect(self, x: int, y: int, width: int, height: int, color=(0, 0, 0)) -> int:
        new_obj = CanvasObject(('rect', (self.rect.x + x, self.rect.y + y), width, height, color))
        self.objects.append(new_obj)

        return len(self.objects) - 1

    def draw_circle(self, x: int, y: int, R: int, color=(0, 0, 0)) -> int:
        new_obj = CanvasObject(('circle', (self.rect.x + x, self.rect.y + y), R, color))
        self.objects.append(new_obj)

        return len(self.objects) - 1

    def draw_image(self, file_name: str, x: int, y: int) -> int:
        new_obj = CanvasObject(('image', file_name, (self.rect.x + x, self.rect.y + y)))
        self.objects.append(new_obj)

        return len(self.objects) - 1

    def move(self, obj, x, y):
        self.objects[obj].x += x
        self.objects[obj].y += y

    def draw(self, screen: pg.Surface):
        pg.draw.rect(screen, self.bg_color, self.rect)

        for obj in self.objects:
            obj.draw(screen)
