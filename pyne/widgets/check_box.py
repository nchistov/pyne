from collections.abc import Callable
import os
from typing import TypeAlias, Any

import pygame as pg

from .base_widget import Widget

NoParamFunc: TypeAlias = Callable[[], Any]


class CheckBox(Widget):
    default_values = {'text_color': (0, 0, 0), 'font_size': 25}
    css_name = 'check-box'

    def __init__(self, text: str, command: NoParamFunc | None = None,
                 unset_command: NoParamFunc | None = None,
                 text_color: tuple[int, int, int] | None = None, font_size: int | None = None,
                 font: str | None = None, name: str = ''):
        super().__init__(name=name)

        self.css_customizable_fields = {'text_color', 'font_size'}

        self.text = text
        self.command = command
        self.unset_command = unset_command

        self._update_fields(locals())

        self.color = (255, 255, 255)

        self.choosing_rect = pg.Rect(self.rect.x + 10, self.rect.y + 10, 10, 10)

        self.bg_rect = pg.Rect(self.rect.x + 9, self.rect.y + 9, 12, 12)

        self.font = pg.font.Font(font or os.path.join(os.path.dirname(__file__),
                                                      '../fonts/font.ttf'), self.font_size)

        self.is_choose = False

        self.set_text(text)

    def set_rect(self, x: int, y: int, width: int, height: int):
        super().set_rect(x, y, width, height)

        self.text_image_rect.left = self.rect.left + 30
        self.text_image_rect.top = self.rect.top + 8

        self.choosing_rect.x = self.rect.x + 10
        self.choosing_rect.y = self.text_image_rect.centery

        self.bg_rect.x = self.rect.x + 9
        self.bg_rect.y = self.text_image_rect.centery - 1

    def set_text(self, text: str):
        self.text = text
        self.text_image = self.font.render(text, True, self.text_color)

        self.text_image_rect = self.text_image.get_rect()

        self.text_image_rect.left = self.rect.left + 30
        self.text_image_rect.top = self.rect.top + 8

        self.choosing_rect.x = self.rect.x + 10
        self.choosing_rect.y = self.text_image_rect.centery

    def set(self):
        self.is_choose = True
        self.color = (25, 155, 250)

    def unset(self):
        self.is_choose = False
        self.color = (255, 255, 255)

    def update(self, event: pg.event.Event):
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos  # Получаем координаты мыши
            if self.choosing_rect.collidepoint(mouse_x, mouse_y):  # Если кнопка нажата
                if not self.is_choose:
                    self.is_choose = True  # изменяем флаг is_choose
                    self.color = (25, 155, 250)  # и цвет

                    if self.command is not None:
                        self.command()  # Если команда зарегистрирована, вызываем ее
                elif self.is_choose:
                    self.is_choose = False

                    if self.unset_command is not None:
                        # Если команда на отпускание зарегистрирована, вызываем ее
                        self.unset_command()

                    self.color = (255, 255, 255)

    def draw(self, screen: pg.Surface):
        screen.blit(self.text_image, self.text_image_rect)
        pg.draw.rect(screen, (0, 0, 0), self.bg_rect)
        pg.draw.rect(screen, self.color, self.choosing_rect)

        if self.is_choose:
            pg.draw.line(screen, (255, 255, 255),
                         (self.choosing_rect.x + 1, self.choosing_rect.y + 5),
                         (self.choosing_rect.centerx - 2, self.choosing_rect.bottom - 1), width=2)
            pg.draw.line(screen, (255, 255, 255),
                         (self.choosing_rect.centerx - 2, self.choosing_rect.bottom - 1),
                         (self.choosing_rect.right - 2, self.choosing_rect.top + 2), width=2)
