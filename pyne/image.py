import pygame as pg


class Image:
    def __init__(self, app, file_name):
        self.app = app

        self.image = pg.image.load(file_name)

        self.rect = self.image.get_rect()

    def draw(self):
        self.app.screen.blit(self.image, self.rect)
