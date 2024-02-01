import pygame as pg


class Widget:
    default_values = {}
    css_name = ''

    def __init__(self, name: str = ''):
        self.css_customizable_fields = set()

        self.priority = 0
        self.name = name

        self.rect = pg.Rect(0, 0, 1, 1)

    def _update_fields(self, local_vars: dict) -> None:
        for attr in self.css_customizable_fields.copy():
            if local_vars[attr] is not None:
                self.css_customizable_fields.remove(attr)
                setattr(self, attr, local_vars[attr])
            else:
                setattr(self, attr, self.default_values[attr])

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
