import sys

import pygame as pg

__version__ = '0.1.0'


class App:
    """Class App, it is a class which manages windows"""
    def __init__(self, window_size=(500, 500), title="Pyne", bg_color=(255, 255, 255)):
        """
        :param window_size: list or tuple of two numbers: first width and last height
        :param title: title of the window
        :param bg_color: color of background, in format RGB
        """
        pg.init()
        print("\nWelcome to the Pyne")
        print(f"Pyne {__version__} (pygame {pg.__version__}, "
              f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro})")

        self.screen = pg.display.set_mode(window_size)
        pg.display.set_caption(title)

        self.clock = pg.time.Clock()

        self.time_table = []
        self.running = False
        self.bg = bg_color
        self.fps = 30

    def quit(self):
        self.running = False
        pg.quit()

    def run(self):
        self.running = True
        while self.running:
            self.screen.fill(self.bg)

            for business in self.time_table:
                business()

            pg.display.flip()

            self.clock.tick()
