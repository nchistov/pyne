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
        self.running = False
        self.bg = bg_color
        self.fps = 30

    def add_to_schedule(self, func: callable):
        self.schedule.append(func)

    def remove_from_schedule(self, func):
        self.schedule.remove(func)

    def add_widget(self, widget):
        self.widgets.append(widget)

    def remove_widget(self, widget):
        self.widgets.remove(widget)

    def _check_events(self):
        for event in pg.event.get():
            match event.type:
                case pg.QUIT:
                    self.quit()

            for widget in self.widgets:
                widget.update(event)

    def run(self):
        """starts mainloop"""
        self.running = True
        while self.running:
            self.screen.fill(self.bg)

            for business in self.schedule:
                business()

            for widget in self.widgets:
                widget.draw(self.screen)

            self._check_events()

            pg.display.flip()

            self.clock.tick()

        pg.quit()

    def quit(self):
        """change running to False"""
        self.running = False
