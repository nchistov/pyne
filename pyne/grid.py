import pygame as pg


class NoSouchPositionError(Exception):
    pass


class Grid:
    def __init__(self, app, rows, columns, x=0, y=0, width=None, height=None):
        self.app = app

        self.rows = rows
        self.columns = columns

        self.x = x
        self.y = y

        self.width = width or app.screen.get_width()
        self.height = height or app.screen.get_height()

    def add_widget(self, widget, row, column, width=1, height=1):
        if row >= self.rows:
            raise NoSouchPositionError("Row must be less then max rows")
        if column >= self.columns:
            raise NoSouchPositionError("Column must be less then max columns")

        try:
            sell_height = self.height / self.rows
            sell_width = self.width / self.columns

            widget.rect.x = self.x + (column * sell_width)
            widget.rect.y = self.y + (row * sell_height)

            widget.rect.width = sell_width * width
            widget.rect.height = sell_height * height

        except AttributeError:
            raise AttributeError("Widget must has attribute rect")
        except ZeroDivisionError:
            pass

        self.app.add_widget(widget)

    def change_pos_of_widget(self, widget, new_row, new_column, new_width=0, new_height=0):
        self.app.remove_widget(widget)
        self.add_widget(widget, new_row, new_column, new_width, new_height)
