import pygame as pg

from . import Button, Entry, Canvas
from .base_widget import Widget


class FileDialog(Widget):
    def __init__(self):
        super().__init__()

        self.save_or_open_btn = Button(text='Open', font_size=30)
        self.cancel_btn = Button(text='Cancel', font_size=30)

        self.filename_entry = Entry()

        self.canvas = Canvas(outline_color=(100, 100, 100))

    def set_rect(self, x, y, width, height):
        super().set_rect(x, y, width, height)
        self.save_or_open_btn.set_rect(x + (width - 80),  y + (height - 90), 80, 40)
        self.cancel_btn.set_rect(x + (width - 80),  y + (height - 40), 80, 40)

        self.filename_entry.set_rect(x + 10, y + (height - 90), width - 100, 40)

        self.canvas.set_rect(x + 5, y + 5, width - 10, height - 100)

    def update(self, event):
        for obj in self.save_or_open_btn, self.cancel_btn, self.filename_entry, self.canvas:
            obj.update(event)

    def draw(self, screen: pg.Surface):
        for obj in self.save_or_open_btn, self.cancel_btn, self.filename_entry, self.canvas:
            obj.draw(screen)
