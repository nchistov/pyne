from collections.abc import Sequence
from typing import cast

import pygame as pg

from .base_widget import Widget
from ._canvas_objects import BaseCanvasObject, Point, Line, Rect, Circle, Polygon, Image, Text


class Canvas(Widget):
    default_values = {'bg_color': (255, 255, 255), 'outline_color': (255, 255, 255)}
    css_name = 'canvas'

    def __init__(self, bg_color: tuple[int ,int, int] | None = None,
                 outline_color: tuple[int, int, int] | None = None, name: str = ''):
        super().__init__(name=name)

        self.css_customizable_fields = {'bg_color', 'outline_color'}

        self._update_fields(locals())

        self.surface = pg.Surface(self.rect.size)

        self.width = 0
        self.height = 0

        self.objects: list[BaseCanvasObject] = []

    def set_rect(self, x: int, y: int, width: int, height: int):
        super().set_rect(x, y, width, height)

        self.width, self.height = width, height

        self.surface = pg.Surface(self.rect.size)

    def draw_point(self, x: int, y: int, color: tuple[int, int, int] = (0, 0, 0)) -> int:
        new_obj = Point((x, y), color)
        self.objects.append(new_obj)

        return len(self.objects) - 1

    def draw_line(self, x1: int, y1: int, x2: int, y2: int,
                  color: tuple[int, int, int] = (0, 0, 0), width: int = 1) -> int:
        new_obj = Line((x1, y1), (x2, y2), color, width)
        self.objects.append(new_obj)

        return len(self.objects) - 1

    def draw_rect(self, x: int, y: int, width: int, height: int,
                  color: tuple[int, int, int] = (0, 0, 0)) -> int:
        new_obj = Rect((x, y), width, height, color)
        self.objects.append(new_obj)

        return len(self.objects) - 1

    def draw_circle(self, x: int, y: int, radius: int,
                    color: tuple[int, int, int] = (0, 0, 0)) -> int:
        new_obj = Circle((x, y), radius, color)
        self.objects.append(new_obj)

        return len(self.objects) - 1

    def draw_polygon(self, coordinates: Sequence[tuple[int, int]],
                     color: tuple[int, int, int] = (0, 0, 0)) -> int:
        new_obj = Polygon(coordinates, color)
        self.objects.append(new_obj)

        return len(self.objects) - 1

    def draw_image(self, file_name: str, x: int, y: int) -> int:
        new_obj = Image(file_name, (x, y))
        self.objects.append(new_obj)

        return len(self.objects) - 1

    def draw_text(self, text: str, x: int, y: int, font_size: int,
                  color: tuple[int, int, int] = (0, 0, 0), font: str | None = None) -> int:
        new_obj = Text((x, y), text, font_size, color, font)
        self.objects.append(new_obj)

        return len(self.objects) - 1

    def move(self, obj: int, x: int, y: int):
        new_coordinates = []

        c_obj = self.objects[obj]

        if isinstance(c_obj, Polygon):  # Если надо двигать многоугольник, подвинем все углы
            c_obj = cast(Polygon, c_obj)
            for pos in c_obj.coordinates:
                new_coordinates.append((pos[0] + x, pos[1] + y))

                c_obj.coordinates = new_coordinates

            return

        c_obj.x += x  # type: ignore[attr-defined]
        c_obj.y += y  # type: ignore[attr-defined]

        if isinstance(c_obj, Line):
            c_obj = cast(Line, c_obj)
            new_end_pos = c_obj.end[0] + x, c_obj.end[1] + y

            c_obj.end = new_end_pos

    def delete(self, obj: int):
        try:
            del self.objects[obj]
        except IndexError:
            pass

    def save_to_file(self, file_name: str):
        pg.image.save(self.surface, file_name)

    def draw(self, screen: pg.Surface):
        self.surface.fill(self.bg_color)

        for obj in self.objects:
            obj.draw(self.surface)

        screen.blit(self.surface, self.rect)

        # Рисуем рамку
        pg.draw.line(screen, self.outline_color, (self.rect.right, self.rect.bottom),
                     (self.rect.right, self.rect.top))
        pg.draw.line(screen, self.outline_color, (self.rect.right, self.rect.top),
                     (self.rect.left, self.rect.top))
        pg.draw.line(screen, self.outline_color, (self.rect.left, self.rect.top),
                     (self.rect.left, self.rect.bottom))
        pg.draw.line(screen, self.outline_color, (self.rect.left, self.rect.bottom),
                     (self.rect.right, self.rect.bottom))
