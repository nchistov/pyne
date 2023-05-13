"""
Содержит класс `App`
"""

from collections.abc import Callable
import json
import os
from typing import TypeAlias, NoReturn, Protocol, Any

import pygame as pg

from ._base_controller import BaseController
from .errors import NoSouchItemError
from .widgets.base_widget import Widget

NoParamFunc: TypeAlias = Callable[[], Any]


class SupportsGetitem(Protocol):
    def __getitem__(self, item: int) -> bool:
        ...


class App(BaseController):
    """Управляет окнами"""

    def __init__(self, window_size: tuple[int, int] = (500, 500), title: str = "Pyne",
                 bg_color: tuple[int, int, int] = (255, 255, 255), icon: str | None = None) -> None:
        """
        :param window_size: список или кортеж из двух чисел: первая ширина, а последняя высота окна.
        :param title: заголовок окна.
        :param bg_color: цвет окна, в формате RGB.
        :param icon: если это None, приложение установит значок по умолчанию,
                     иначе значок пользователя.
        """
        super().__init__()

        pg.init()
        pg.font.init()
        pg.mixer.init()

        self.screen = pg.display.set_mode(window_size, flags=pg.RESIZABLE)
        print(f'[Pyne] window size -> {window_size}')

        if icon is None:
            self.icon = pg.image.load(os.path.join(os.path.dirname(__file__), 'images/icon.jpg'))
        else:
            self.icon = pg.image.load(icon)
        pg.display.set_icon(self.icon)

        pg.display.set_caption(title)
        print(f'[Pyne] window title -> "{title}"')

        self.clock = pg.time.Clock()

        self.tasks: list[NoParamFunc] = []
        self.widgets: list[Widget] = []
        self.handlers: dict[str, NoParamFunc] = {}
        self.used_handlers: dict[str, NoParamFunc] = {}
        self.unused_handlers: dict[str, NoParamFunc] = {}

        self.func_on_exit: NoParamFunc | None = None

        with open(os.path.join(os.path.dirname(__file__), 'events.json')) as f:
            self.events: dict[str, int] = json.load(f)

        self.running = False
        self.bg = bg_color
        self.fps = 30
        print(f'[Pyne] fps -> {self.fps}')

    def set_title(self, new_title: str) -> None:
        pg.display.set_caption(new_title)

    def set_window_size(self, new_size: tuple[int, int]) -> None:
        self.screen = pg.display.set_mode(new_size)

    def get_mouse_pos(self) -> tuple[int, int]:
        return pg.mouse.get_pos()

    def clear_tasks(self) -> None:
        self.tasks.clear()

    def clear_widgets(self) -> None:
        self.widgets.clear()

    def clear_handlers(self) -> None:
        self.handlers.clear()
        self.used_handlers.clear()
        self.unused_handlers.clear()

    def add_func_on_exit(self, func: NoParamFunc) -> None:
        self.func_on_exit = func

    def add_task(self, func: NoParamFunc, priority: int | None = None) -> None:
        if priority is None:
            self.tasks.append(func)
            return

        self.tasks.insert(priority, func)

    def remove_task(self, func: NoParamFunc) -> None | NoReturn:  # type: ignore[return]
        if func in self.tasks:
            self.tasks.remove(func)
        else:
            raise NoSouchItemError(f'can not find task {func}.')

    def add_handler(self, key: str, func: NoParamFunc) -> None:
        self.handlers[key] = func
        self.used_handlers[key] = func

    def remove_handler(self, key: str) -> None | NoReturn:  # type: ignore[return]
        if key in self.handlers.keys() and key in self.used_handlers.keys():
            del self.handlers[key]
            del self.used_handlers[key]
        else:
            raise NoSouchItemError(f'can not find handler {key}.')

    def _is_press(self, keys: SupportsGetitem, handler: str) -> bool:
        """Возвращает True, если handler нажат, иначе возвращает False"""
        for key in handler.split('-'):
            if key.startswith('Mouse'):  # Если зарегистрирован handler на мышь
                mouse_state = pg.mouse.get_pressed(5)  # Получить состояние мыши
                if key.endswith('Left'):
                    if not mouse_state[0]:
                        return False
                elif key.endswith('Right'):
                    if not mouse_state[2]:
                        return False
                elif key.endswith('Wheel'):
                    if not mouse_state[1]:
                        return False
            elif not keys[self.events[key]]:
                return False
        return True

    def _check_events(self) -> None:
        """Проверяет событие выхода и все обработчики"""
        keys = pg.key.get_pressed()

        for handler, func in self.handlers.items():
            if handler in self.used_handlers:
                if self._is_press(keys, handler):
                    func()
                    del self.used_handlers[handler]
                    self.unused_handlers[handler] = func
            else:
                if not self._is_press(keys, handler):
                    del self.unused_handlers[handler]
                    self.used_handlers[handler] = func

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()

            for widget in self.widgets:
                widget.update(event)

    def run(self) -> None:
        """Запускает главный цикл"""
        self.running = True

        print('[Pyne] application start')

        while self.running:
            self.screen.fill(self.bg)

            for widget in self.widgets:
                widget.draw(self.screen)

            for task in self.tasks:
                task()

            self._check_events()

            pg.display.flip()

            self.clock.tick()

        pg.quit()

    def quit(self) -> None:
        """Завершает главный цикл"""
        self.running = False
        print('[Pyne] application quit')

        if self.func_on_exit is not None:
            self.func_on_exit()
