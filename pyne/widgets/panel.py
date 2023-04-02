import pygame as pg

from .base_widget import Widget


class Panel(Widget):
    def __init__(self, color=(255, 255, 255), outline_color=(255, 255, 255), name: str = ''):
        super().__init__(name=name)

        self.color = color
        self.outline_color = outline_color

    def draw(self, screen: pg.Surface):
        pg.draw.rect(screen, self.color, self.rect)

        # Рисуем рамку
        pg.draw.line(screen, self.outline_color, (self.rect.right, self.rect.bottom), (self.rect.right, self.rect.top))
        pg.draw.line(screen, self.outline_color, (self.rect.right, self.rect.top), (self.rect.left, self.rect.top))
        pg.draw.line(screen, self.outline_color, (self.rect.left, self.rect.top), (self.rect.left, self.rect.bottom))
        pg.draw.line(screen, self.outline_color, (self.rect.left, self.rect.bottom),
                     (self.rect.right, self.rect.bottom))
