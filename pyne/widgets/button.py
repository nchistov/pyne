import os
from typing import Callable

import pygame as pg

import pyne.sound
from .base_widget import Widget


class Button(Widget):
    def __init__(self, text: str, color=(150, 150, 150), active_color=(70, 200, 215),
                 text_color=(0, 0, 0), outline_color=(200, 200, 200), font_size=30, command: Callable | None = None,
                 image=None, press='left', sound: pyne.sound.Sound | None = None):
        super().__init__()
        self.text = text
        self.color = color
        self.active_color = active_color
        self.text_color = text_color
        self.outline_color = outline_color
        self.command = command

        self.press = press

        self.current_color = color
        self.sound = sound

        self.is_pressed = False

        self.has_image = False

        if image is not None:
            self.image = pg.image.load(image)
            self.image_rect = self.image.get_rect()

            self.has_image = True

        self.rect = pg.Rect(0, 0, len(text) * 17, 35)

        self.font = pg.font.Font(os.path.join(os.path.dirname(__file__), '../fonts/font.ttf'), font_size)

        self.set_text(text)

    def set_text(self, text: str):
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
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos  # Получаем координаты мыши
                if self.rect.collidepoint(mouse_x, mouse_y):  # Если кнопка нажата
                    self.current_color = self.active_color    # изменяем цвет
                    self.is_pressed = True                    # и флаг is_pressed
                    if self.command is not None:
                        self.command()                        # Если команда зарегистрирована, вызываем ее
                    if self.sound is not None:
                        self.sound.play()

        elif event.type == pg.MOUSEBUTTONUP:
            self.current_color = self.color
            self.is_pressed = False

    def draw(self, screen: pg.Surface):
        pg.draw.rect(screen, self.current_color, self.rect)
        screen.blit(self.text_image, self.text_image_rect)

        if not self.is_pressed:  # Если кнопка не нажата, рисуем рамку
            pg.draw.line(screen, self.outline_color, (self.rect.right - 1,
                                                      self.rect.bottom),
                         (self.rect.right - 1, self.rect.top))

            pg.draw.line(screen, self.outline_color, (self.rect.right, self.rect.top),
                         (self.rect.left, self.rect.top))
        if self.has_image:
            screen.blit(self.image, self.image_rect)
