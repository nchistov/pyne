import os

import pygame as pg

from .base_widget import Widget


class Entry(Widget):
    default_values = {'text_color': (0, 0, 0), 'bg_color': (255, 255, 255),
                      'outline_color': (0, 0, 0), 'font_size': 25}
    css_name = 'entry'

    def __init__(self, prompt: str = '', text: str = '',
                 text_color: tuple[int, int, int] | None = None,
                 bg_color: tuple[int, int, int] | None = None,
                 outline_color: tuple[int, int, int] | None = None, font_size: int | None = None,
                 font: str | None = None, name: str = ''):
        super().__init__(name=name)

        self.css_customizable_fields = {'text_color', 'bg_color', 'outline_color', 'font_size'}

        self._prompt = prompt
        self.prompt_color = (150, 150, 150)

        self._update_fields(locals())

        self.current_outline_color = (200, 200, 200)

        self.insertion_pos = len(text)

        self._text = text

        self.active = False

        self.cursor_rect = pg.Rect(0, 0, 3, 20)

        self.surface = pg.Surface(self.rect.size)

        self.font = pg.font.Font(font or os.path.join(os.path.dirname(__file__),
                                                      '../fonts/font.ttf'), self.font_size)
        self.text_image = self.font.render(self._text, True, self.text_color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.left = 5
        self.text_image_rect.centery = self.rect.height // 2
        self._render_text()

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str):
        self._text = value
        self._render_text()

    @property
    def prompt(self) -> str:
        return self._prompt

    @prompt.setter
    def prompt(self, value: str):
        self._prompt = value
        self._render_text()

    def set_text(self, text: str):
        self._text = text
        self._render_text()

    def set_rect(self, x: int, y: int, width: int, height: int):
        super().set_rect(x, y, width, height)
        self._render_text()

        self.surface = pg.Surface(self.rect.size)

    def _render_text(self):
        text, color = self._text, self.text_color
        if not text:
            text = self.prompt
            color = self.prompt_color

        self.text_image = self.font.render(text, True, color)
        self.text_image_rect.centery = self.rect.height // 2

    def _render_cursor(self):
        before_cursor = self.font.render(self._text[:self.insertion_pos],
                                         True, self.text_color).get_rect()
        before_cursor.left = self.text_image_rect.left
        self.cursor_rect.left = before_cursor.right
        d = self.cursor_rect.right - self.rect.width
        if d > 0:
            self.text_image_rect.right -= d
            self.cursor_rect.right -= d
        if self.cursor_rect.left < 0:
            self.text_image_rect.right -= self.cursor_rect.left
            self.cursor_rect.left = 0

    def _check_mouse_click(self, mouse_x: float, mouse_y: float):
        if self.rect.collidepoint(mouse_x, mouse_y):
            self.active = True

            self.current_outline_color = self.outline_color
        else:
            self.active = False

            self.current_outline_color = (200, 200, 200)

    def _delete_letter(self):
        if self._text and self.insertion_pos != 0:
            new_text = self._text[:self.insertion_pos - 1]
            new_text += self._text[self.insertion_pos:]

            self.insertion_pos -= 1

            self.text = new_text

    def _add_letter(self, letter: str):
        new_text = self._text[:self.insertion_pos]
        new_text += letter
        new_text += self._text[self.insertion_pos:]

        self.insertion_pos += 1

        self.text = new_text

    def update(self, event: pg.event.Event):
        self.cursor_rect.centery = self.rect.height // 2

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                self._check_mouse_click(mouse_x, mouse_y)

        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_BACKSPACE:
                    self._delete_letter()
                elif event.key == pg.K_ESCAPE:
                    self.active = False
                    self.current_outline_color = (200, 200, 200)

                elif event.key not in (9, 13, 127, 1073742052, 1073742048, 1073742054,
                                       1073742050, 1073741904, 1073741903):  # Непечатаемые клавиши
                    self._add_letter(event.unicode)

                if event.key == pg.K_LEFT:
                    if self.insertion_pos != 0:
                        self.insertion_pos -= 1
                elif event.key == pg.K_RIGHT:
                    if self.insertion_pos != len(self._text):
                        self.insertion_pos += 1

        self._render_cursor()

    def draw(self, screen: pg.Surface):
        pg.draw.rect(screen, self.bg_color, self.rect)

        self.surface.fill(self.bg_color)
        self.surface.blit(self.text_image, self.text_image_rect)
        if self.active:
            # Рисуем курсор
            pg.draw.rect(self.surface, (0, 0, 0), self.cursor_rect)
        screen.blit(self.surface, self.rect)

        # Рисуем рамку
        pg.draw.line(screen, self.current_outline_color, (self.rect.right, self.rect.bottom),
                     (self.rect.right, self.rect.top))
        pg.draw.line(screen, self.current_outline_color, (self.rect.right, self.rect.top),
                     (self.rect.left, self.rect.top))
        pg.draw.line(screen, self.current_outline_color, (self.rect.left, self.rect.top),
                     (self.rect.left, self.rect.bottom))
        pg.draw.line(screen, self.current_outline_color, (self.rect.left, self.rect.bottom),
                     (self.rect.right, self.rect.bottom))
