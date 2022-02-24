import sys

import pygame as pg

from .app import App

from . import widgets

from . import beatle

__version__ = '0.1.0 alpha'

print("\nWelcome to the Pyne")
print(f"Pyne {__version__} (pygame {pg.__version__}, "
      f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro})")
