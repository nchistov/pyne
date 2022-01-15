"""
module in which one are located all widgets
in package pyne
"""

import pygame as pg


class Button:
    def __init__(self, text: str, color=(150, 150, 150), active_color=(70, 200, 215),
                 text_color=(0, 0, 0), font_size=40, command: callable = None):
        self.text = text
        self.color = color
        self.active_color = active_color
        self.text_color = text_color
        self.command = command

        self.current_color = color

        self.is_press = False

        pg.font.init()

        self.rect = pg.Rect(0, 0, len(text) * 17, 35)

        self.row = 0
        self.column = 0

        self.max_rows = 0
        self.max_columns = 0

        self.font = pg.font.SysFont('', font_size)

        self.prep_msg(text)

    def prep_msg(self, text):
        self.text_image = self.font.render(text, True, self.text_color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.x = self.rect.x + 5
        self.text_image_rect.y = self.rect.y + 5

    def update(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pg.mouse.get_pos()
            if self.rect.collidepoint(mouse_x, mouse_y):
                self.current_color = self.active_color
                self.is_press = True
                if self.command is not None:
                    self.command()
        elif event.type == pg.MOUSEBUTTONUP:
            self.current_color = self.color
            self.is_press = False

        self.text_image_rect.center = self.rect.center

    def draw(self, screen: pg.Surface):
        pg.draw.rect(screen, self.current_color, self.rect)
        screen.blit(self.text_image, self.text_image_rect)

        if not self.is_press:
            pg.draw.line(screen, (180, 180, 180), (self.rect.x + self.rect.width, self.rect.y + self.rect.height),
                         (self.rect.x + self.rect.width, self.rect.y))
            pg.draw.line(screen, (180, 180, 180), (self.rect.x + self.rect.width, self.rect.y),
                         (self.rect.x, self.rect.y))
