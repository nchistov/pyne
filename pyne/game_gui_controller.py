import pygame as pg

from ._base_controller import BaseController
from pyne.widgets.base_widget import Widget


class GameGUIController(BaseController):
    def __init__(self, screen: pg.Surface):
        super().__init__()

        self.screen = screen

        self.widgets: list[Widget] = []

    def add_widget(self, widget: Widget, x: int, y: int, width: int, height: int, priority: int | None = None) -> None:
        widget.set_rect(x, y, width, height)

        super().add_widget(widget, priority)

    def update(self, event: pg.event.Event) -> None:
        for widget in self.widgets:
            widget.update(event)

    def draw(self) -> None:
        for widget in self.widgets:
            widget.draw(self.screen)
