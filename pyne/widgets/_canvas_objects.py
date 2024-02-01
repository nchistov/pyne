import os
from typing import Sequence

import pygame as pg


class BaseCanvasObject:
    def __init__(self): ...
    def draw(self, screen: pg.Surface) -> None: ...


class Point(BaseCanvasObject):
    def __init__(self, pos: tuple[int, int], color: tuple[int, int, int]) -> None:
        super().__init__()

        self.x, self.y = pos
        self.color = color

        self.rect = pg.Rect(*pos, 1, 1)

    def draw(self, screen: pg.Surface) -> None:
        self.rect.x = self.x
        self.rect.y = self.y

        pg.draw.rect(screen, self.color, self.rect)


class Line(BaseCanvasObject):
    def __init__(self, start: tuple[int, int], end: tuple[int, int],
                 color: tuple[int, int, int], width: int) -> None:
        super().__init__()

        self.x, self.y = start
        self.end = end
        self.color = color
        self.width = width

    def draw(self, screen: pg.Surface) -> None:
        pg.draw.line(screen, self.color, (self.x, self.y), self.end, self.width)


class Rect(BaseCanvasObject):
    def __init__(self, pos: tuple[int, int], width: int, height: int,
                 color: tuple[int, int, int]) -> None:
        super().__init__()

        self.x, self.y = pos
        self.width = width
        self.height = height
        self.color = color

        self.rect = pg.Rect(*pos, self.width, self.height)

    def draw(self, screen: pg.Surface) -> None:
        self.rect.x = self.x
        self.rect.y = self.y

        pg.draw.rect(screen, self.color, self.rect)


class Circle(BaseCanvasObject):
    def __init__(self, pos: tuple[int, int], radius: int, color: tuple[int, int, int]) -> None:
        super().__init__()

        self.x, self.y = pos
        self.radius = radius
        self.color = color

    def draw(self, screen: pg.Surface) -> None:
        pg.draw.circle(screen, self.color, (self.x, self.y), self.radius)


class Polygon(BaseCanvasObject):
    def __init__(self, coordinates: Sequence[tuple[int, int]], color: tuple[int, int, int]) -> None:
        super().__init__()

        self.coordinates = coordinates
        self.color = color

    def draw(self, screen: pg.Surface) -> None:
        pg.draw.polygon(screen, self.color, self.coordinates)


class Image(BaseCanvasObject):
    def __init__(self, filename: str, pos: tuple[int, int]) -> None:
        super().__init__()

        self.filename = filename
        self.x, self.y = pos

        self.image = pg.image.load(self.filename)

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

    def draw(self, screen: pg.Surface) -> None:
        self.rect.x = self.x
        self.rect.y = self.y

        screen.blit(self.image, self.rect)


class Text(BaseCanvasObject):
    def __init__(self, pos: tuple[int, int], text: str, font_size: int,
                 color: tuple[int, int, int], font_filename: str | None = None) -> None:
        super().__init__()

        self.x, self.y = pos
        self.text = text
        self.font_size = font_size
        self.color = color
        self.font_filename = font_filename

        self.font = pg.font.Font(
            self.font_filename or os.path.join(os.path.dirname(__file__),
                                      '../fonts/font.ttf'), self.font_size)

        self.text_image = self.font.render(self.text, True, self.color)

        self.text_image_rect = self.text_image.get_rect()

        self.text_image_rect.x = self.x
        self.text_image_rect.y = self.y

    def draw(self, screen: pg.Surface) -> None:
        self.text_image_rect.x = self.x
        self.text_image_rect.y = self.y

        screen.blit(self.text_image, self.text_image_rect)
