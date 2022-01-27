import pygame as pg


class NoSouchPositionError(Exception): pass


class Grid:
    def __init__(self, app, rows, columns):
        self.app = app

        self.rows = rows
        self.columns = columns

    def add_widget(self, widget, row, column, width=1, height=1):
        if row >= self.rows:
            raise NoSouchPositionError("Row must be less then max rows")
        if column >= self.columns:
            raise NoSouchPositionError("Column must be less then max columns")

        try:
            sell_height = self.app.screen.get_height() / self.rows
            sell_width = self.app.screen.get_width() / self.columns

            widget.rect.x = column * sell_width
            widget.rect.y = row * sell_height

            widget.rect.width = sell_width * width
            widget.rect.height = sell_height * height

        except AttributeError:
            raise AttributeError("Widget must has attribute rect")

        self.app.add_widget(widget)

    def add_image(self, image, row, column, width=1, height=1, size_correction=False):
        if row >= self.rows:
            raise NoSouchPositionError("Row must be less then max rows")
        if column >= self.columns:
            raise NoSouchPositionError("Column must be less then max columns")

        try:
            sell_height = self.app.screen.get_height() / self.rows
            sell_width = self.app.screen.get_width() / self.columns

            image.rect.x = column * sell_width
            image.rect.y = row * sell_height

            image.rect.width = sell_width * width
            image.rect.height = sell_height * height

            if size_correction:
                image.image = pg.transform.smoothscale(image.image, (sell_width, sell_height))

        except AttributeError:
            raise AttributeError("Widget must has attribute rect")

        self.app.add_to_schedule(image.draw)
