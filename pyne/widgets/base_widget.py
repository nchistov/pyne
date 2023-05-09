import pygame as pg


class Widget:
    def __init__(self, name: str = ''):
        self.priority = 0
        self.name = name

        self.rect = pg.Rect(0, 0, 1, 1)

    def set_rect(self, x: int, y: int, width: int, height: int) -> None:
        self.rect.x = x
        self.rect.y = y
        self.rect.width = width
        self.rect.height = height

    def hit(self, x: int, y: int) -> bool:
        return self.rect.collidepoint(x, y)

    def update(self, event: pg.event.Event) -> None:
        pass

    def draw(self, screen: pg.Surface) -> None:
        pass
