from time import time

import pygame as pg

from .base_widget import Widget


class Entry(Widget):
    def __init__(self, prompt='', text_color=(0, 0, 0), bg_color=(225, 255, 255),
                 outline_color=(0, 0, 0), font_size=30):
        super().__init__()

        self.text_color = text_color

        self.bg_color = bg_color
        self.outline_color = outline_color

        self.text = ''

        self.active = False

        self.cursor_rect = pg.Rect(self.rect.x, self.rect.y, 2, 10)

        self.time_cursor_state_changed = time()
        self.cursor_state = 0

        self.font = pg.font.SysFont('', font_size)

        self.prep_text(prompt, (150, 150, 150))

    def prep_text(self, text, color):
        self.text_image = self.font.render(text, True, color)

        self.text_image_rect = self.text_image.get_rect()

        self.text_image_rect.left = self.rect.left

    def update(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if self.rect.collidepoint(mouse_x, mouse_y):
                self.active = True

        # Change cursor state
        if self.time_cursor_state_changed - time() >= 0.1:
            if self.cursor_state == 0:
                self.cursor_state = 1
            elif self.cursor_state == 1:
                self.cursor_state = 0
            self.time_cursor_state_changed = time()

    def draw(self, screen: pg.Surface):
        pg.draw.rect(screen, self.bg_color, self.rect)

        screen.blit(self.text_image, self.text_image_rect)

        if self.active:
            # Draw outline
            pg.draw.line(screen, self.outline_color, (self.rect.right, self.rect.bottom),
                         (self.rect.right, self.rect.top))
            pg.draw.line(screen, self.outline_color, (self.rect.right, self.rect.top), (self.rect.left, self.rect.top))
            pg.draw.line(screen, self.outline_color, (self.rect.left, self.rect.top),
                         (self.rect.left, self.rect.bottom))
            pg.draw.line(screen, self.outline_color, (self.rect.left, self.rect.bottom),
                         (self.rect.right, self.rect.bottom))

            # Draw cursor
            pg.draw.rect(screen, (0, 0, 0), self.cursor_rect)
