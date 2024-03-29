import pygame as pg


class Sound:
    def __init__(self, file_name: str):
        self.sound = pg.mixer.Sound(file_name)

        self._volume: float = self.sound.get_volume()

        self.length: float = self.sound.get_length()

    @property
    def volume(self) -> float:
        return self._volume

    @volume.setter
    def volume(self, value: float) -> None:
        self._volume = value
        self.sound.set_volume(self._volume)

    def stop(self) -> None:
        self.sound.stop()

    def play(self) -> None:
        self.sound.play()
