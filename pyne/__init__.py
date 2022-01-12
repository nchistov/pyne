import sys

import pygame as pg

__version__ = '0.1.0'


class App:
    """Class App, it is a class which manages windows"""
    def __init__(self, window_size=(500, 500), title="Pyne"):
        """
        :param window_size: it is a list or a tuple of two numbers: first width and last height
        :param title: it is a title of the window
        """
        pg.init()
        print("\nWelcome to the Pyne")
        print(f"Pyne {__version__} (pygame {pg.__version__}, "
              f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro})")

        self.screen = pg.display.set_mode(window_size)
        pg.display.set_caption(title)

        self.time_table = []
