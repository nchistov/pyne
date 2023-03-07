import pygame as pg

from pyne.app import NoSouchItemError
from .widgets.base_widget import Widget


class GameGUIController:
    def __init__(self, screen: pg.Surface):
        self.screen = screen

        self.widgets: list[Widget] = []

    def add_widget(self, widget: Widget, x: int, y: int, width: int, height: int, priority: int | None = None):
        widget.set_rect(x, y, width, height)

        if priority is None:
            self.widgets.append(widget)
            return

        self.widgets.insert(priority, widget)

    def remove_widget(self, widget: Widget):
        if widget in self.widgets:
            self.widgets.remove(widget)
        else:
            raise NoSouchItemError(f'can not find widget {widget} in widgets.')

    def update(self, event: pg.event.Event):
        for widget in self.widgets:
            widget.update(event)

    def draw(self):
        for widget in self.widgets:
            widget.draw(self.screen)
