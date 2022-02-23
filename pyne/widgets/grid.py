import pygame as pg

import pyne
from .base_widget import Widget


class NoSouchPositionError(Exception):
    pass


class Grid(Widget):
    def __init__(self, app: pyne.App, rows: int, columns: int):
        super().__init__()
        self.app = app

        self.rows = rows
        self.columns = columns

        self.rect = pg.Rect(0, 0, app.screen.get_width(), app.screen.get_height())

        self.widgets = []

    def add_widget(self, widget, row, column, width=1, height=1):
        if row >= self.rows:
            raise NoSouchPositionError("Row must be less then max rows")
        if column >= self.columns:
            raise NoSouchPositionError("Column must be less then max columns")

        try:
            sell_height = self.rect.height / self.rows
            sell_width = self.rect.width / self.columns

            widget.rect.x = self.rect.x + (column * sell_width)
            widget.rect.y = self.rect.y + (row * sell_height)

            widget.rect.width = sell_width * width
            widget.rect.height = sell_height * height

        except AttributeError:
            raise AttributeError("Widget must has attribute rect")
        except ZeroDivisionError:
            pass

        self.widgets.append(widget)

    def change_pos_of_widget(self, widget, new_row, new_column, new_width=0, new_height=0):
        self.widgets.remove(widget)
        self.add_widget(widget, new_row, new_column, new_width, new_height)

    def update(self, event):
        for widget in self.widgets:
            widget.update(event)

    def draw(self, screen: pg.Surface):
        for widget in self.widgets:
            widget.draw(screen)
