import pygame as pg

from .base_widget import Widget


class Panel(Widget):
    default_values = {'color': (255, 255, 255), 'outline_color': (255, 255, 255)}
    css_name = 'panel'

    def __init__(self, color: tuple[int, int, int] | None = None,
                 outline_color: tuple[int, int, int] | None = None, name: str = ''):
        super().__init__(name=name)

        self.css_customizable_fields = {'color', 'outline_color'}

        self._update_fields(locals())

    def draw(self, screen: pg.Surface):
        pg.draw.rect(screen, self.color, self.rect)

        # Рисуем рамку
        pg.draw.line(screen, self.outline_color, (self.rect.right, self.rect.bottom),
                     (self.rect.right, self.rect.top))
        pg.draw.line(screen, self.outline_color, (self.rect.right, self.rect.top),
                     (self.rect.left, self.rect.top))
        pg.draw.line(screen, self.outline_color, (self.rect.left, self.rect.top),
                     (self.rect.left, self.rect.bottom))
        pg.draw.line(screen, self.outline_color, (self.rect.left, self.rect.bottom),
                     (self.rect.right, self.rect.bottom))
