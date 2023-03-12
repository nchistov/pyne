import pygame as pg

from . import Entry, Button
from .base_widget import Widget


class NumericUpDown(Widget):
    def __init__(self):
        super().__init__()

        self.value = 0

        self.entry = Entry(text='0')

        self.btn1 = Button('^', command=self.up, font_size=35)
        self.btn2 = Button('v', command=self.down, font_size=30)

    def up(self):
        self.value = int(self.entry.text)
        self.value += 1
        self.entry.text = str(self.value)

    def down(self):
        self.value = int(self.entry.text)
        self.value -= 1
        self.entry.text = str(self.value)

    def set_rect(self, x, y, width, height):
        super().set_rect(x, y, width, height)
        self.entry.set_rect(x, y, width - 20, height)

        self.btn1.set_rect(x + (width - 20), y, 20, height // 2)
        self.btn2.set_rect(x + (width - 20), y + (height // 2), 20, height // 2)

    def update(self, event):
        self.entry.update(event)

        self.btn1.update(event)
        self.btn2.update(event)

    def draw(self, screen: pg.Surface):
        self.entry.draw(screen)

        self.btn1.draw(screen)
        self.btn2.draw(screen)
