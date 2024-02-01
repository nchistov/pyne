import os

import pygame as pg

from .base_widget import Widget


class Label(Widget):
    default_values = {'bg_color': (255, 255, 255), 'outline_color': (255, 255, 255),
                      'text_color': (0, 0, 0), 'font_size': 60, 'press': 'right'}
    css_name = 'label'

    def __init__(self, text: str, bg_color: tuple[int, int, int] | None = None,
                 outline_color: tuple[int, int, int] | None = None,
                 text_color: tuple[int, int, int] | None = None, font_size: int | None = None,
                 press: str | None = None, font: str | None = None, name: str = ''):
        super().__init__(name=name)

        self.css_customizable_fields = {'bg_color', 'outline_color', 'text_color',
                                        'font_size', 'press'}

        self._update_fields(locals())

        self.text = text

        self.font = pg.font.Font(font or os.path.join(os.path.dirname(__file__),
                                                      '../fonts/font.ttf'), self.font_size)

        self.set_text(text)

    def set_text(self, text: str):
        self.text = text
        self.text_image = self.font.render(text, True, self.text_color)

        self.text_image_rect = self.text_image.get_rect()

        match self.press:  # Прижимаем текст к нужному краю
            case 'right':
                self.text_image_rect.right = self.rect.right - 3
            case 'left':
                self.text_image_rect.left = self.rect.left + 3
            case 'center':
                self.text_image_rect.centerx = self.rect.centerx

        self.text_image_rect.centery = self.rect.centery

    def set_rect(self, x: int, y: int, width: int, height: int):
        super().set_rect(x, y, width, height)

        match self.press:  # Прижимаем текст к нужному краю
            case 'right':
                self.text_image_rect.right = self.rect.right - 3
            case 'left':
                self.text_image_rect.left = self.rect.left + 3
            case 'center':
                self.text_image_rect.centerx = self.rect.centerx

        self.text_image_rect.centery = self.rect.centery

    def draw(self, screen: pg.Surface):
        pg.draw.rect(screen, self.bg_color, self.rect)
        screen.blit(self.text_image, self.text_image_rect)

        # Рисуем рамку
        pg.draw.line(screen, self.outline_color, (self.rect.right, self.rect.bottom),
                     (self.rect.right, self.rect.top))
        pg.draw.line(screen, self.outline_color, (self.rect.right, self.rect.top),
                     (self.rect.left, self.rect.top))
        pg.draw.line(screen, self.outline_color, (self.rect.left, self.rect.top),
                     (self.rect.left, self.rect.bottom))
        pg.draw.line(screen, self.outline_color, (self.rect.left, self.rect.bottom),
                     (self.rect.right, self.rect.bottom))
