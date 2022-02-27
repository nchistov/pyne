import pygame as pg

from .base_widget import Widget


class Entry(Widget):
    def __init__(self, bg_color=(225, 255, 255), outline_color=(0, 0, 0)):
        super().__init__()

        self.bg_color = bg_color
        self.outline_color = outline_color

        self.active = False

    def update(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if self.rect.collidepoint(mouse_x, mouse_y):
                self.active = True

    def draw(self, screen: pg.Surface):
        pg.draw.rect(screen, self.bg_color, self.rect)

        if self.active:
            # Draw outline
            pg.draw.line(screen, self.outline_color, (self.rect.right, self.rect.bottom),
                         (self.rect.right, self.rect.top))
            pg.draw.line(screen, self.outline_color, (self.rect.right, self.rect.top), (self.rect.left, self.rect.top))
            pg.draw.line(screen, self.outline_color, (self.rect.left, self.rect.top),
                         (self.rect.left, self.rect.bottom))
            pg.draw.line(screen, self.outline_color, (self.rect.left, self.rect.bottom),
                         (self.rect.right, self.rect.bottom))
