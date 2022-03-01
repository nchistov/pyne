import pygame as pg

from .base_widget import Widget


class Entry(Widget):
    def __init__(self, prompt='', text_color=(0, 0, 0), bg_color=(255, 255, 255),
                 outline_color=(0, 0, 0), font_size=30):
        super().__init__()

        self.prompt = prompt

        self.text_color = text_color

        self.bg_color = bg_color
        self.outline_color = outline_color

        self.insertion_pos = 0

        self.text = ''

        self.active = False

        self.cursor_rect = pg.Rect(self.rect.x, self.rect.y, 3, 20)
        self.cursor_rect.left = self.rect.left
        self.cursor_rect.top = self.rect.top

        self.font = pg.font.SysFont('', font_size)

        self.prep_text(prompt, (150, 150, 150))

    def prep_text(self, text, color):
        self.text_image = self.font.render(text, True, color)

        self.text_image_rect = self.text_image.get_rect()

        self.text_image_rect.left = self.rect.left
        self.text_image_rect.centery = self.rect.centery

    def update(self, event):
        self.cursor_rect.centery = self.rect.centery

        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if self.rect.collidepoint(mouse_x, mouse_y):
                self.active = True
            else:
                self.active = False

        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]

                    self.prep_text(self.text, self.text_color)

                    self.cursor_rect.centery = self.text_image_rect.centery
                elif event.key not in (13, 1073742052, 1073742048, 1073742054,
                                       1073742050, 1073741904, 1073741903):  # Unprintable keys
                    new_text = self.text[:self.insertion_pos]
                    new_text += event.unicode
                    new_text += self.text[self.insertion_pos:]

                    self.insertion_pos += 1

                    self.text = new_text

                    self.prep_text(self.text, self.text_color)
                if event.key == pg.K_LEFT:
                    if self.insertion_pos != 0:
                        self.insertion_pos -= 1
                elif event.key == pg.K_RIGHT:
                    if self.insertion_pos != len(self.text) - 1:
                        self.insertion_pos += 1

            self.cursor_rect.left = self.text_image_rect.right + 1

        if not self.text:
            self.prep_text(self.prompt, (150, 150, 150))

            self.cursor_rect.left = self.rect.left

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
