import os

import pygame as pg

from . import Button, Entry, Canvas
from .base_widget import Widget


class FileDialog(Widget):
    def __init__(self):
        super().__init__()

        self._speed = 10
        self._min_y = 5
        self._max_y = 0
        self._top_y = 5
        self._bottom_y = 5

        self.save_or_open_btn = Button(text='Open', font_size=30)
        self.cancel_btn = Button(text='Cancel', font_size=30)

        self.filename_entry = Entry()

        self.canvas = Canvas(outline_color=(100, 100, 100))

        self.canvas_objects = []

    def _read_ls(self, path):
        """Returns sorted lists of folders and files."""
        ls_out = os.listdir(path)

        directories = []
        files = []

        for item in ls_out:
            if os.path.isdir(os.path.join(path, item)):
                directories.append(item)
            else:
                files.append(item)

        return sorted(directories), sorted(files)

    def set_rect(self, x, y, width, height):
        super().set_rect(x, y, width, height)
        self.save_or_open_btn.set_rect(x + (width - 80),  y + (height - 90), 80, 40)
        self.cancel_btn.set_rect(x + (width - 80),  y + (height - 40), 80, 40)

        self.filename_entry.set_rect(x + 10, y + (height - 90), width - 100, 40)

        self.canvas.set_rect(x + 5, y + 5, width - 10, height - 100)

        result = self._read_ls('/home/nick/')
        y = 5

        for folder in result[0]:
            self.canvas_objects.append(self.canvas.draw_text(folder, 25, y, 30))
            self.canvas_objects.append(self.canvas.draw_image(os.path.join(os.path.dirname(__file__), 'folder.gif'),
                                                              5, y))
            y += 40
            self._max_y = y
            self._bottom_y = y

        for file in result[1]:
            self.canvas_objects.append(self.canvas.draw_text(file, 25, y, 30))
            self.canvas_objects.append(self.canvas.draw_image(os.path.join(os.path.dirname(__file__), 'file.gif'),
                                                              5, y))
            y += 40
            self._max_y = y
            self._bottom_y = y

    def update(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if self.canvas.hit(mouse_x, mouse_y):
                if event.button == 4:  # Up
                    if self._bottom_y > self.canvas.height:
                        for obj in self.canvas_objects:
                            self.canvas.move(obj, 0, -self._speed)
                        self._top_y -= self._speed
                        self._bottom_y -= self._speed
                elif event.button == 5:  # Down
                    if self._top_y < 0:
                        for obj in self.canvas_objects:
                            self.canvas.move(obj, 0, self._speed)
                        self._top_y += self._speed
                        self._bottom_y += self._speed

        for obj in self.save_or_open_btn, self.cancel_btn, self.filename_entry, self.canvas:
            obj.update(event)

    def draw(self, screen: pg.Surface):
        for obj in self.save_or_open_btn, self.cancel_btn, self.filename_entry, self.canvas:
            obj.draw(screen)
