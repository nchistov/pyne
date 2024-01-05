"""
Содержит класс `BaseController`
"""

from typing import NoReturn

from ._css_parser import parse
from .errors import NoSouchItemError
from .widgets.base_widget import Widget
from . import widgets


class BaseController:
    """Базовый класс для классов `App` и `GameGUIController`"""
    def __init__(self, css: str = '') -> None:
        self.widgets: list[Widget] = []

        self.css = css

    def _update_widgets_style(self) -> None:
        parsed_css = parse(self.css)
        for widget_name, values in parsed_css.items():
            for widget in self.widgets:
                if widget.css_name == widget_name:
                    for k, v in values['value'].items():
                        if k.replace('-', '_') in widget.css_customizable_fields:
                            setattr(widget, k.replace('-', '_'), v)
                            if 'text' in k:
                                widget.set_text(widget.text)
                elif isinstance(widget, widgets.Grid):
                    widget.css = self.css

    def add_widget(self, widget: Widget, priority: int | None = None) -> None:
        if priority is None:
            self.widgets.append(widget)
            return

        self.widgets.insert(priority, widget)

    def remove_widget(self, widget: Widget) -> None | NoReturn:  # type: ignore[return]
        if widget in self.widgets:
            self.widgets.remove(widget)
        else:
            raise NoSouchItemError(f'can not find widget {widget}.')
