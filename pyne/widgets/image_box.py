import pygame as pg

from .base_widget import Widget


class ImageBox(Widget):
    def __init__(self, file_name):
        super().__init__()

        self.image = pg.image.load(file_name)

    def scale(self):
        self.image = pg.transform.smoothscale(self.image, (self.rect.width, self.rect.height))

    def draw(self, screen: pg.Surface):
        screen.blit(self.image, self.rect)
