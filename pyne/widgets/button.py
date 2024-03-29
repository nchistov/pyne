from collections.abc import Callable
import os
from typing import TypeAlias, Any

import pygame as pg

from pyne.sound import Sound
from .base_widget import Widget

NoParamFunc: TypeAlias = Callable[[], Any]


class Button(Widget):
    default_values = {'color': (150, 150, 150), 'active_color': (70, 200, 215),
                      'text_color': (0, 0, 0), 'outline_color': (200, 200, 200),
                      'font_size': 30, 'press': 'left'}
    css_name = 'button'

    def __init__(self, text: str, color: tuple[int, int, int] | None = None,
                 active_color: tuple[int, int, int] | None = None,
                 text_color: tuple[int, int, int] | None = None,
                 outline_color: tuple[int, int, int] | None = None,
                 font_size: int | None = None, command: NoParamFunc | None = None,
                 image: str | None = None, press: str | None = None,
                 sound: Sound | None = None, font: str | None = None, name: str = ''):
        super().__init__(name=name)

        self.css_customizable_fields = {'color', 'active_color', 'text_color',
                                        'outline_color', 'font_size', 'press'}
        self.text = text

        self.command = command

        self._update_fields(locals())

        self.current_color = self.color
        self.sound = sound

        self.is_pressed = False

        self.has_image = False

        if image is not None:
            self.image = pg.image.load(image)
            self.image_rect = self.image.get_rect()

            self.has_image = True

        self.rect = pg.Rect(0, 0, len(text) * 17, 35)

        self.font = pg.font.Font(font or os.path.join(os.path.dirname(__file__),
                                                      '../fonts/font.ttf'), self.font_size)

        self.set_text(text)

    def set_text(self, text: str):
        self.text = text
        self.text_image = self.font.render(text, True, self.text_color)

        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect.center

    def set_rect(self, x: int, y: int, width: int, height: int):
        super().set_rect(x, y, width, height)

        self.text_image_rect.center = self.rect.center

        if self.has_image:
            match self.press:
                case 'right top':
                    self.image_rect.top = self.rect.top
                    self.image_rect.right = self.rect.right
                case 'right':
                    self.image_rect.centery = self.rect.centery
                    self.image_rect.right = self.rect.right
                case 'right bottom':
                    self.image_rect.bottom = self.rect.bottom
                    self.image_rect.right = self.rect.right
                case 'center top':
                    self.image_rect.top = self.rect.top
                    self.image_rect.centerx = self.rect.centerx
                case 'center':
                    self.image_rect.centery = self.rect.centery
                    self.image_rect.centerx = self.rect.centerx
                case 'center bottom':
                    self.image_rect.bottom = self.rect.bottom
                    self.image_rect.centerx = self.rect.centerx
                case 'left top':
                    self.image_rect.top = self.rect.top
                    self.image_rect.left = self.rect.left
                case 'left':
                    self.image_rect.centery = self.rect.centery
                    self.image_rect.left = self.rect.left
                case 'left bottom':
                    self.image_rect.bottom = self.rect.bottom
                    self.image_rect.left = self.rect.left
                case _:
                    raise ValueError('incorrect word to pressing image')

    def update(self, event: pg.event.Event):
        self.current_color = self.color
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos  # Получаем координаты мыши
                if self.rect.collidepoint(mouse_x, mouse_y):  # Если кнопка нажата
                    self.current_color = self.active_color    # изменяем цвет
                    self.is_pressed = True                    # и флаг is_pressed
                    if self.command is not None:
                        self.command()                 # Если команда зарегистрирована, вызываем ее
                    if self.sound is not None:
                        self.sound.play()

        elif event.type == pg.MOUSEBUTTONUP:
            self.current_color = self.color
            self.is_pressed = False

    def draw(self, screen: pg.Surface):
        pg.draw.rect(screen, self.current_color, self.rect, border_radius=5)
        screen.blit(self.text_image, self.text_image_rect)

        if self.has_image:
            screen.blit(self.image, self.image_rect)
