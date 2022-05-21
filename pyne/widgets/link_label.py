import webbrowser

import pygame as pg

from .label import Label


class LinkLabel(Label):
    def __init__(self, text: str, url: str, bg_color: tuple[int, int, int] = (255, 255, 255),
                 outline_color: tuple[int, int, int] = (255, 255, 255), text_color: tuple[int, int, int] = (0, 0, 255),
                 font_size: int = 60, press: str = 'right'):
        super().__init__(text, bg_color, outline_color, text_color, font_size, press)

        self.url = url
        if not text:
            self.text = url
            self.set_text(self.text)

    def update(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                if self.text_image_rect.collidepoint(mouse_x, mouse_y):
                    webbrowser.open_new_tab(self.url)

    def draw(self, screen):
        super().draw(screen)
        pg.draw.line(screen, (0, 0, 255), (self.text_image_rect.left, self.text_image_rect.bottom),
                     (self.text_image_rect.right, self.text_image_rect.bottom))
