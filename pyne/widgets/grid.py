import pygame as pg

import pyne
from .base_widget import Widget


class NoSouchPositionError(Exception):
    pass


class Grid(Widget):
    def __init__(self, app: pyne.App, rows: int, columns: int, scrolling=False, speed=5):
        super().__init__()
        self.app = app

        self.rows = rows
        self.columns = columns

        self.scrolling = scrolling
        self.speed = speed

        self.rect = pg.Rect(0, 0, app.screen.get_width(), app.screen.get_height())

        self.screen_rect = self.app.screen.get_rect()

        self.widgets = []

    def add_widget(self, widget, row, column, width=1, height=1, priority=None):
        if row >= self.rows:
            raise NoSouchPositionError("Row must be less then max rows")
        if column >= self.columns:
            raise NoSouchPositionError("Column must be less then max columns")

        try:
            sell_height = self.rect.height / self.rows
            sell_width = self.rect.width / self.columns

            x = self.rect.x + (column * sell_width)
            y = self.rect.x + (row * sell_height)

            widget.set_rect(x, y, sell_width * width, sell_height * height)

        except AttributeError:
            raise AttributeError("Widget must has method 'set_rect'")
        except ZeroDivisionError:
            pass

        if priority is None:
            self.widgets.append(widget)

            return

        self.widgets.insert(priority, widget)

    def change_pos_of_widget(self, widget, new_row, new_column, new_width=1, new_height=1, priority=None):
        self.widgets.remove(widget)
        self.add_widget(widget, new_row, new_column, new_width, new_height, priority)

    def update(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.height > self.screen_rect.width:
                if event.button == 4:  # Up
                    if self.rect.top <= self.screen_rect.top:
                        self.rect.y -= self.speed

                        for widget in self.widgets:
                            widget.set_rect(widget.rect.x, widget.rect.y - self.speed,
                                            widget.rect.width, widget.rect.height)
                elif event.button == 5:  # Down
                    if self.rect.bottom > self.screen_rect.bottom and self.rect.top < self.screen_rect.top:
                        self.rect.y += self.speed

                        for widget in self.widgets:
                            widget.set_rect(widget.rect.x, widget.rect.y + self.speed,
                                            widget.rect.width, widget.rect.height)

        for widget in self.widgets:
            widget.update(event)

    def draw(self, screen: pg.Surface):
        for widget in self.widgets:
            widget.draw(screen)
