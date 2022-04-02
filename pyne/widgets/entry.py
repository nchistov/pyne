import pygame as pg

from .base_widget import Widget


class Entry(Widget):
    def __init__(self, prompt='', text='', text_color=(0, 0, 0), bg_color=(255, 255, 255),
                 outline_color=(0, 0, 0), font_size=30):
        super().__init__()

        self.prompt = prompt
        self.prompt_color = (150, 150, 150)
        self.text_color = text_color

        self.bg_color = bg_color
        self.outline_color = outline_color

        self.current_outline_color = (200, 200, 200)

        self.insertion_pos = len(text)

        self._text = text

        self.active = False

        self.cursor_rect = pg.Rect(0, 0, 3, 20)

        self.surface = pg.Surface(self.rect.size)

        self.font = pg.font.SysFont('', font_size)
        self.text_image = self.font.render(self.text, True, self.text_color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.left = 5
        self.text_image_rect.centery = self.rect.height // 2
        self.render_text()

    def set_text(self, text):
        self.text = text

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
        self.render_text()

    def set_rect(self, x, y, width, height):
        super().set_rect(x, y, width, height)
        self.render_text()

        self.surface = pg.Surface(self.rect.size)

    def render_text(self):
        text, color = self.text, self.text_color
        if not text:
            text = self.prompt
            color = self.prompt_color

        self.text_image = self.font.render(text, True, color)
        self.text_image_rect.centery = self.rect.height // 2

    def render_cursor(self):
        before_cursor = self.font.render(self.text[:self.insertion_pos], True, self.text_color).get_rect()
        before_cursor.left = self.text_image_rect.left
        self.cursor_rect.left = before_cursor.right
        d = self.cursor_rect.right - self.rect.width
        if d > 0:
            self.text_image_rect.right -= d
            self.cursor_rect.right -= d
        if self.cursor_rect.left < 0:
            self.text_image_rect.right -= self.cursor_rect.left
            self.cursor_rect.left = 0

    def check_mouse_click(self, mouse_x, mouse_y):
        if self.rect.collidepoint(mouse_x, mouse_y):
            self.active = True

            self.current_outline_color = self.outline_color
        else:
            self.active = False

            self.current_outline_color = (200, 200, 200)

    def delete_text(self):
        if self.text and self.insertion_pos != 0:
            new_text = self.text[:self.insertion_pos - 1]
            new_text += self.text[self.insertion_pos:]

            self.insertion_pos -= 1

            self.text = new_text

    def add_letter(self, letter):
        new_text = self.text[:self.insertion_pos]
        new_text += letter
        new_text += self.text[self.insertion_pos:]

        self.insertion_pos += 1

        self.text = new_text

    def update(self, event):
        self.cursor_rect.centery = self.rect.height // 2

        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            self.check_mouse_click(mouse_x, mouse_y)

        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_BACKSPACE:
                    self.delete_text()
                elif event.key == pg.K_ESCAPE:
                    self.active = False
                    self.current_outline_color = (200, 200, 200)

                elif event.key not in (9, 13, 127, 1073742052, 1073742048, 1073742054,
                                       1073742050, 1073741904, 1073741903):  # Unprintable keys
                    self.add_letter(event.unicode)

                if event.key == pg.K_LEFT:
                    if self.insertion_pos != 0:
                        self.insertion_pos -= 1
                elif event.key == pg.K_RIGHT:
                    if self.insertion_pos != len(self.text):
                        self.insertion_pos += 1

        self.render_cursor()

    def draw(self, screen: pg.Surface):
        pg.draw.rect(screen, self.bg_color, self.rect)

        self.surface.fill(self.bg_color)
        self.surface.blit(self.text_image, self.text_image_rect)
        if self.active:
            # Draw cursor
            pg.draw.rect(self.surface, (0, 0, 0), self.cursor_rect)
        screen.blit(self.surface, self.rect)

        # Draw outline
        pg.draw.line(screen, self.current_outline_color, (self.rect.right, self.rect.bottom),
                     (self.rect.right, self.rect.top))
        pg.draw.line(screen, self.current_outline_color, (self.rect.right, self.rect.top), (self.rect.left, self.rect.top))
        pg.draw.line(screen, self.current_outline_color, (self.rect.left, self.rect.top),
                     (self.rect.left, self.rect.bottom))
        pg.draw.line(screen, self.current_outline_color, (self.rect.left, self.rect.bottom),
                     (self.rect.right, self.rect.bottom))

