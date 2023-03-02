import json
import os
from typing import Callable

import pygame as pg

from pyne.errors import NoSouchItemError
from pyne.widgets.base_widget import Widget


class App:
    """Управляет окнами"""

    def __init__(self, window_size=(500, 500), title="Pyne", bg_color=(255, 255, 255),
                 icon: str | None = None):
        """
        :param window_size: список или кортеж из двух чисел: первая ширина, а последняя высота окна.
        :param title: заголовок окна.
        :param bg_color: цвет окна, в формате RGB.
        :param icon: если это None, приложение установит значок по умолчанию, иначе значок пользователя.
        """

        pg.init()
        pg.font.init()
        pg.mixer.init()

        self.screen = pg.display.set_mode(window_size)
        print(f'[Pyne] window size -> {window_size}')

        if icon is None:
            self.icon = pg.image.load(os.path.join(os.path.dirname(__file__), 'icon.jpg'))
        else:
            self.icon = pg.image.load(icon)
        pg.display.set_icon(self.icon)

        pg.display.set_caption(title)
        print(f'[Pyne] window title -> "{title}"')

        self.clock = pg.time.Clock()

        self.tasks: list[Callable] = []
        self.widgets: list[Widget] = []
        self.handlers: dict[str, Callable] = {}
        self.used_handlers: dict[str, Callable] = {}
        self.unused_handlers: dict[str, Callable] = {}

        self.func_on_exit: Callable | None = None

        with open(os.path.join(os.path.dirname(__file__), 'events.json')) as f:
            self.events = json.load(f)

        self.running = False
        self.bg = bg_color
        self.fps = 30
        print(f'[Pyne] fps -> {self.fps}')

    def set_title(self, new_title):
        pg.display.set_caption(new_title)

    def set_window_size(self, new_size):
        self.screen = pg.display.set_mode(new_size)

    def get_mouse_pos(self):
        return pg.mouse.get_pos()

    def clear_tasks(self):
        self.tasks.clear()

    def clear_widgets(self):
        self.widgets.clear()

    def clear_handlers(self):
        self.handlers.clear()
        self.used_handlers.clear()
        self.unused_handlers.clear()

    def add_func_on_exit(self, func: Callable):
        self.func_on_exit = func

    def add_task(self, func: Callable, priority=None):
        if priority is None:
            self.tasks.append(func)
            return

        self.tasks.insert(priority, func)

    def remove_task(self, func: Callable):
        if func in self.tasks:
            self.tasks.remove(func)
        else:
            raise NoSouchItemError(f'can not find task {func}.')

    def add_widget(self, widget, priority=None):
        if priority is None:
            self.widgets.append(widget)
            return

        self.widgets.insert(priority, widget)

    def remove_widget(self, widget):
        if widget in self.widgets:
            self.widgets.remove(widget)
        else:
            raise NoSouchItemError(f'can not find widget {widget}.')

    def add_handler(self, key: str, func: Callable):
        self.handlers[key] = func
        self.used_handlers[key] = func

    def remove_handler(self, key):
        if key in self.handlers.keys() and key in self.used_handlers.keys():
            del self.handlers[key]
            del self.used_handlers[key]
        else:
            raise NoSouchItemError(f'can not find handler {key}.')

    def _is_press(self, keys, handler):
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

    def _check_events(self):
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

    def run(self):
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

    def quit(self):
        """Завершает главный цикл"""
        self.running = False
        print('[Pyne] application quit')

        if self.func_on_exit is not None:
            self.func_on_exit()
