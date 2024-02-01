"""
Содержит ошибки вызываемые в разных случаях в этом пакете
"""


class NoSouchItemError(Exception):
    pass


class NoSouchPositionError(Exception):
    pass


class VersionError(Exception):
    pass


class CSSParseError(Exception):
    pass
