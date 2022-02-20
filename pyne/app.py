import json
import os

import pygame as pg


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

        self.screen = pg.display.set_mode(window_size)

        icon = pg.image.load(os.path.join(os.path.dirname(__file__), 'icon.jpg'))
        pg.display.set_icon(icon)

        pg.display.set_caption(title)

        self.clock = pg.time.Clock()

        self.schedule = []
        self.widgets = []
        self.handlers = {}

        with open(os.path.join(os.path.dirname(__file__), 'events.json')) as f:
            self.events = json.load(f)

        self.running = False
        self.bg = bg_color
        self.fps = 30

    def add_to_schedule(self, func: callable):
        self.schedule.append(func)

    def remove_from_schedule(self, func):
        if func in self.schedule:
            self.schedule.remove(func)

    def add_widget(self, widget):
        self.widgets.append(widget)

    def remove_widget(self, widget):
        if widget in self.widgets:
            self.widgets.remove(widget)

    def add_handler(self, key: str, func: callable):
        self.handlers[key] = func

    def remove_handler(self, key):
        if key in self.handlers.keys():
            del self.handlers[key]

    def _check_events(self):
        keys = pg.key.get_pressed()

        for handler, func in self.handlers.items():
            for key in handler.split('-'):
                if not keys[self.events[key]]:
                    break
            else:
                func()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()

            for widget in self.widgets:
                widget.update(event)

    def run(self):
        """starts mainloop"""
        self.running = True
        while self.running:
            self.screen.fill(self.bg)

            for widget in self.widgets:
                widget.draw(self.screen)

            for business in self.schedule:
                business()

            self._check_events()

            pg.display.flip()

            self.clock.tick()

        pg.quit()

    def quit(self):
        """change running to False"""
        self.running = False
