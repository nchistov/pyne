import pygame as pg


class Sound:
    def __init__(self, file_name):
        self.sound = pg.mixer.Sound(file_name)

        self.volume = self.sound.get_volume()

        self.length = self.sound.get_length()

    def stop(self):
        self.sound.stop()

    def play(self):
        self.sound.set_volume(self.volume)

        self.sound.play()
