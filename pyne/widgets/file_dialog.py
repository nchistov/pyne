import os
import sys
from enum import Enum

import pygame as pg

from . import Button, Entry, Canvas
from ._canvas_objects import Text
from .base_widget import Widget


class State(Enum):
    waiting = 0
    opening = 1
    saving = 2


class FileDialog(Widget):
    def __init__(self, files: list[str] | None = None, name: str = ''):
        super().__init__(name=name)

        self.files = files or []

        self.state = State.waiting

        self.result = ''

        self._speed = 15
        self._min_y = 5
        self._max_y = 0
        self._top_y = 5
        self._bottom_y = 5

        self.path = os.getcwd()

        self.save_or_open_btn = Button(text='Open', font_size=25, command=self.save_or_open)
        self.cancel_btn = Button(text='Cancel', font_size=25, command=self.cancel)

        self.back_btn = Button(text='^', font_size=25, command=self.back)

        self.filename_entry = Entry()

        self.canvas = Canvas(outline_color=(100, 100, 100))

        self.widgets = (self.save_or_open_btn, self.cancel_btn, self.filename_entry, self.canvas, self.back_btn)

        self.canvas_objects: list[int] = []  # Идентификаторы объектов на холсте.

    def askopenfile(self):
        self.state = State.opening
        self.save_or_open_btn.set_text('Open')

    def asksavefile(self):
        self.state = State.saving
        self.save_or_open_btn.set_text('Save')

    def save_or_open(self):
        self.result = os.path.join(self.path, self.filename_entry.text)
        self.state = State.waiting

    def cancel(self):
        self.state = State.waiting

    def back(self):
        """Возвращается назад по дереву каталогов."""
        if sys.platform == 'win32':
            if self.path.count('\\') > 1:
                new_end = self.path.rfind('\\')
                self.path = self.path[:new_end]
        else:
            if self.path.count('/') > 1:
                new_end = self.path.rfind('/')
                self.path = self.path[:new_end]

        for item in self.canvas_objects[::-1]:
            self.canvas.delete(item)
        self.canvas_objects.clear()

        self.draw_items()

    def _read_ls(self, path: str):
        """Возвращает отсортированные списки папок и файлов."""
        ls_out = os.listdir(path)

        directories = []
        files = []

        for item in ls_out:
            if os.path.isdir(os.path.join(path, item)):
                directories.append(item)
            else:
                if not self.files:
                    files.append(item)
                else:
                    for file in self.files:
                        if not item.startswith('.') and item.endswith(file):
                            files.append(item)

        return sorted(directories), sorted(files)

    def set_rect(self, x, y, width, height):
        super().set_rect(x, y, width, height)
        self.save_or_open_btn.set_rect(x + (width - 80),  y + (height - 90), 80, 40)
        self.cancel_btn.set_rect(x + (width - 80),  y + (height - 40), 80, 40)

        self.back_btn.set_rect(x + (width - 80),  y + 5, 80, 40)

        self.filename_entry.set_rect(x + 10, y + (height - 90), width - 100, 40)

        self.canvas.set_rect(x + 5, y + 50, width - 10, height - 150)

        self.draw_items()

    def draw_items(self):
        result = self._read_ls(self.path)
        y = 5

        for folder in result[0]:
            self.canvas_objects.append(self.canvas.draw_text(folder, 25, y, 25))
            self.canvas_objects.append(self.canvas.draw_image(os.path.join(os.path.dirname(__file__),
                                                                           'images/folder.gif'),
                                                              5, y + 10))
            y += 40
            self._max_y = y
            self._bottom_y = y

        for file in result[1]:
            self.canvas_objects.append(self.canvas.draw_text(file, 25, y, 25))
            self.canvas_objects.append(self.canvas.draw_image(os.path.join(os.path.dirname(__file__),
                                                                           'images/file.gif'),
                                                              5, y + 10))
            y += 40
            self._max_y = y
            self._bottom_y = y

    def update(self, event: pg.event.Event):
        if self.state != State.waiting:
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if self.canvas.hit(mouse_x, mouse_y):
                    if event.button == 5:  # Вверх
                        if self._bottom_y > self.canvas.height:
                            for obj in self.canvas_objects:
                                self.canvas.move(obj, 0, -self._speed)
                            self._top_y -= self._speed
                            self._bottom_y -= self._speed
                    elif event.button == 4:  # Вниз
                        if self._top_y < 0:
                            for obj in self.canvas_objects:
                                self.canvas.move(obj, 0, self._speed)
                            self._top_y += self._speed
                            self._bottom_y += self._speed
                    elif event.button == 1:
                        for c_obj in self.canvas.objects:
                            if isinstance(c_obj, Text):
                                if self.canvas.hit(mouse_x, mouse_y):
                                    if c_obj.text_image_rect.collidepoint(mouse_x - self.canvas.rect.x, mouse_y - self.canvas.rect.y):
                                        if os.path.isdir(os.path.join(self.path, c_obj.text)):
                                            self.path = os.path.join(self.path, c_obj.text)

                                            for item in self.canvas_objects[::-1]:
                                                self.canvas.delete(item)
                                            self.canvas_objects.clear()

                                            self.draw_items()
                                        else:
                                            self.filename_entry.set_text(c_obj.text)

            for widget in self.widgets:
                widget.update(event)

    def draw(self, screen: pg.Surface):
        if self.state != State.waiting:
            for obj in self.widgets:
                obj.draw(screen)
