import pygame as pg

from .base_widget import Widget


class Entry(Widget):
    def __init__(self, bg_color=(225, 255, 255), outline_color=(0, 0, 0)):
        super().__init__()

        self.bg_color = bg_color
        self.outline_color = outline_color

        self.active = False
