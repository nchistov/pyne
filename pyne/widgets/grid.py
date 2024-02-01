import pygame as pg

from .base_widget import Widget
from .._css_parser import parse
from ..errors import NoSouchItemError, NoSouchPositionError


class Grid(Widget):
    def __init__(self, rows: int, columns: int, padding: int = 0, scrolling: bool = False, speed: int = 5,
                 name: str = ''):
        """
        :param rows: количество рядов
        :param columns: количество столбцов
        :param scrolling: если это True, когда мышь прокручивается, сетка тоже прокручивается
        :param speed: количество пикселей, на которое прокручивается сетка
        """
        super().__init__(name=name)
        self.rows = rows
        self.columns = columns
        self.padding = padding

        self.scrolling = scrolling
        self.speed = speed

        self.rect = pg.Rect(0, 0, pg.display.get_window_size()[0], pg.display.get_window_size()[1])

        self.screen_rect = pg.display.get_surface().get_rect()

        # Этот флаг говорит на весь ли экран растянута grid
        # если да то она должна растягиваться вслед за окном.
        self.is_on_all_screen = True

        self.widgets: dict[Widget, tuple[int, int, float, float]] = {}
        self.sorted_widgets: list[Widget] = []

        self.css = ''

    def set_rect(self, x: int, y: int, width: int, height: int):
        super().set_rect(x, y, width, height)

        self.update_widgets_pos()

        self.is_on_all_screen = False

    def add_widget(self, widget: Widget, row: int, column: int, width: float = 1, height: float = 1,
                   priority: int | None = None) -> None:
        if row >= self.rows:
            raise NoSouchPositionError("Row must be less then max rows")
        if column >= self.columns:
            raise NoSouchPositionError("Column must be less then max columns")

        try:
            sell_height = self.rect.height / self.rows
            sell_width = self.rect.width / self.columns

            x = int(self.rect.x + (column * sell_width)) + self.padding // 2
            y = int(self.rect.x + (row * sell_height))

            widget.set_rect(x, y, int(sell_width * width)-self.padding, int(sell_height * height) - self.padding)

        except AttributeError as exc:
            raise AttributeError("Widget must has method 'set_rect'") from exc
        except ZeroDivisionError:
            pass

        if priority is None:
            widget.priority = 0
        else:
            widget.priority = priority

        self.widgets[widget] = (row, column, width, height)

        self.sorted_widgets = sorted(self.widgets, key=lambda w: w.priority)

    def remove_widget(self, widget: Widget):
        if widget in self.widgets:
            self.widgets.pop(widget)
            self.sorted_widgets = sorted(self.widgets, key=lambda w: w.priority)
        else:
            raise NoSouchItemError(f'can not find widget {widget} in widgets.')

    def change_pos_of_widget(self, widget: Widget, new_row: int, new_column: int,
                             new_width: int = 1, new_height: int = 1, priority: int | None = None):
        if widget in self.widgets:
            self.widgets.pop(widget)
        else:
            raise NoSouchItemError(f'can not find widget {widget} in widgets.')

        self.add_widget(widget, new_row, new_column, new_width, new_height, priority)

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
                elif isinstance(widget, self.__class__):
                    widget.css = self.css

    def update(self, event: pg.event.Event):
        self._update_widgets_style()
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if self.rect.collidepoint(mouse_x, mouse_y):
                if self.rect.height > self.screen_rect.width:
                    if event.button == 4:  # Вверх
                        # Если край сетки выходит за край окна
                        if self.rect.top <= self.screen_rect.top and \
                                self.rect.bottom > self.screen_rect.bottom + self.speed:
                            self.rect.y -= self.speed

                            for widget in self.widgets:
                                widget.set_rect(widget.rect.x, widget.rect.y - self.speed,
                                                widget.rect.width, widget.rect.height)
                    elif event.button == 5:  # Вниз
                        # Если край сетки выходит за край окна
                        if self.rect.bottom > self.screen_rect.bottom and \
                             self.rect.top < self.screen_rect.top:
                            self.rect.y += self.speed

                            for widget in self.widgets:
                                widget.set_rect(widget.rect.x, widget.rect.y + self.speed,
                                                widget.rect.width, widget.rect.height)

        for widget in self.sorted_widgets:
            widget.update(event)

        if self.is_on_all_screen:
            self.screen_rect = pg.display.get_surface().get_rect()
            if self.rect.width != self.screen_rect.width:
                self.set_rect(0, 0, self.screen_rect.width, self.rect.height)
                self.is_on_all_screen = True
            if self.rect.height != self.screen_rect.height:
                self.set_rect(0, 0, self.rect.width, self.screen_rect.height)
                self.is_on_all_screen = True

    def update_widgets_pos(self):
        for widget, info in self.widgets.copy().items():
            self.change_pos_of_widget(widget, *info)

    def draw(self, screen: pg.Surface):
        for widget in self.sorted_widgets:
            widget.draw(screen)
