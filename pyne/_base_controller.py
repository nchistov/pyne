from typing import NoReturn

from .errors import NoSouchItemError
from .widgets.base_widget import Widget


class BaseController:
    def __init__(self) -> None:
        self.widgets: list[Widget] = []

    def add_widget(self, widget: Widget, priority: int | None = None) -> None:
        if priority is None:
            self.widgets.append(widget)
            return

        self.widgets.insert(priority, widget)

    def remove_widget(self, widget: Widget) -> None | NoReturn:
        if widget in self.widgets:
            self.widgets.remove(widget)
        else:
            raise NoSouchItemError(f'can not find widget {widget}.')
