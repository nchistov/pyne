from collections.abc import Callable
from typing import TypeAlias, Any

import pygame as pg

from .check_box import CheckBox

NoParamFunc: TypeAlias = Callable[[], Any]


class RadioButton(CheckBox):
    default_values = {'text_color': (0, 0, 0), 'font_size': 25}
    css_name = 'radio-button'

    def __init__(self, text: str, command: NoParamFunc | None = None,
                 unset_command: NoParamFunc | None = None,
                 text_color: tuple[int, int, int] | None = None, font_size: int | None = None,
                 font: str | None = None, name: str = ''):
        super().__init__(text, command, unset_command, text_color, font_size, font, name=name)

        self.css_customizable_fields = {'text_color', 'font_size'}

        self.choosing_rect = pg.Rect(self.rect.x + 10, self.rect.y + 10, 15, 15)

    def draw(self, screen: pg.Surface):
        screen.blit(self.text_image, self.text_image_rect)

        pg.draw.circle(screen, (0, 0, 0), self.choosing_rect.center,
                       self.choosing_rect.height // 2)
        pg.draw.circle(screen, (255, 255, 255), self.choosing_rect.center,
                       (self.choosing_rect.height // 2) - 1)

        if self.is_choose:
            pg.draw.circle(screen, (0, 0, 255), self.choosing_rect.center, (self.choosing_rect.height // 2) - 3)
