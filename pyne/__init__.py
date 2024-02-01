import sys

from .app import App

from . import widgets

from . import beatle
from . import sound
from .game_gui_controller import GameGUIController
from . import errors
from . import constants  # Для __all__
from .constants import *  # Для использования, например pyne.RED

if sys.version_info < (3, 10):
    raise errors.VersionError('Версия Python должна быть >= 3.10')

__all__ = ['App', 'widgets', 'beatle', 'sound', 'GameGUIController', 'errors', '__version__'] +\
          [d for d in dir(constants) if not d.startswith('__')]

__version__ = '0.3.0 alpha'

print(f'\n[Pyne] version -> {__version__}')
