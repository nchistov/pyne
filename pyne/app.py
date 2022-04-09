import json
import os
from typing import Callable

import pygame as pg


class NoSouchItemError(Exception):
    pass


class App:
    """Class App, it is a class which manages windows"""

    def __init__(self, window_size=(500, 500), title="Pyne", bg_color=(255, 255, 255)):
        """
        :param window_size: list or tuple of two numbers: first width and last height
        :param title: title of the window
        :param bg_color: color of background, in format RGB
        """

        pg.init()
        pg.font.init()
        pg.mixer.init()

        self.screen = pg.display.set_mode(window_size)
        print(f'[Pyne] window size -> {window_size}')

        icon = pg.image.load(os.path.join(os.path.dirname(__file__), 'icon.jpg'))
        pg.display.set_icon(icon)

        pg.display.set_caption(title)
        print(f'[Pyne] window title -> "{title}"')

        self.clock = pg.time.Clock()

        self.tasks = []
        self.widgets = []
        self.handlers = {}
        self.used_handlers = {}
        self.unused_handlers = {}

        with open(os.path.join(os.path.dirname(__file__), 'events.json')) as f:
            self.events = json.load(f)

        self.running = False
        self.bg = bg_color
        self.fps = 30
        print(f'[Pyne] fps -> {self.fps}')

    def add_task(self, func: Callable, priority=None):
        if priority is None:
            self.tasks.append(func)
            return

        self.tasks.insert(priority, func)

    def remove_task(self, func: Callable):
        if func in self.tasks:
            self.tasks.remove(func)
        else:
            raise NoSouchItemError(f'can not find func {func} in schedule.')

    def add_widget(self, widget, priority=None):
        if priority is None:
            self.widgets.append(widget)
            return

        self.widgets.insert(priority, widget)

    def remove_widget(self, widget):
        if widget in self.widgets:
            self.widgets.remove(widget)
        else:
            raise NoSouchItemError(f'can not find widget {widget} in widgets.')

    def add_handler(self, key: str, func: Callable):
        self.handlers[key] = func
        self.used_handlers[key] = func

    def remove_handler(self, key):
        if key in self.handlers.keys() and key in self.used_handlers.keys():
            del self.handlers[key]
            del self.used_handlers[key]
        else:
            raise NoSouchItemError(f'can not find key {key} in handlers.')

    def _is_press(self, keys, handler):
        for key in handler.split('-'):
            if not keys[self.events[key]]:
                break
        else:
            return True
        return False

    def _check_events(self):
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
        """starts mainloop"""
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
        """change running to False"""
        self.running = False
        print('[Pyne] application quit')
