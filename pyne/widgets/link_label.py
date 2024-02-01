import webbrowser

import pygame as pg

from .label import Label


class LinkLabel(Label):
    default_values = {'bg_color': (255, 255, 255), 'outline_color': (255, 255, 255),
                      'text_color': (0, 0, 255), 'font_size': 60, 'press': 'right'}
    css_name = 'link-label'

    def __init__(self, text: str, url: str, bg_color: tuple[int, int, int] | None = None,
                 outline_color: tuple[int, int, int] | None = None,
                 text_color: tuple[int, int, int] | None = None, font_size: int | None = None,
                 press: str | None = None, font: str | None = None, name: str = ''):
        super().__init__(text, bg_color, outline_color, text_color,
                         font_size, press, font, name=name)

        self.css_customizable_fields = {'bg_color', 'outline_color', 'text_color',
                                        'font_size', 'press'}

        self.url = url
        if not text:
            self.text = url
            self.set_text(self.text)

        self.active = False

    def update(self, event: pg.event.Event):
        mouse_x, mouse_y = pg.mouse.get_pos()
        if self.text_image_rect.collidepoint(mouse_x, mouse_y):
            self.active = True
        else:
            self.active = False

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.active:
                    webbrowser.open_new_tab(self.url)

    def draw(self, screen: pg.Surface):
        super().draw(screen)
        if self.active:
            pg.draw.line(screen, (0, 0, 255),
                         (self.text_image_rect.left, self.text_image_rect.bottom),
                         (self.text_image_rect.right, self.text_image_rect.bottom))
