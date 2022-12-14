import pygame as pg


class Sound:
    def __init__(self, file_name):
        self.sound = pg.mixer.Sound(file_name)

        self._volume = self.sound.get_volume()

        self.length = self.sound.get_length()

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        self._volume = value
        self.sound.set_volume(self._volume)

    def stop(self):
        self.sound.stop()

    def play(self):
        self.sound.play()
