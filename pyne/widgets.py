"""
module in which one are located all widgets
in package pyne
"""

import pygame as pg


class Button:
    def __init__(self, text: str, color=(100, 100, 100), active_color=(70, 200, 215),
                 text_color=(0, 0, 0), command: callable = None):
        self.text = text
        self.color = color
        self.active_color = active_color
        self.text_color = text_color
        self.command = command

        self.rect = pg.Rect(0, 0, len(text) * 7, 20)

        self.row = 0
        self.column = 0

        self.max_rows = 0
        self.max_columns = 0

        self.font = pg.font.SysFont('', 40)

        self.prep_msg(text)

    def prep_msg(self, text):
        self.text_image = self.font.render(text, True, self.text_color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.x = self.rect.x + 5
        self.text_image_rect.y = self.rect.y + 5

    def draw(self, screen: pg.Surface):
        screen.blit(self.text_image, self.text_image_rect)
