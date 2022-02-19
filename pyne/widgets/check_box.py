import pygame as pg

from .base_widget import Widget


class CheckBox(Widget):
    def __init__(self, text, command=None, text_color=(0, 0, 0), font_size=20):
        super().__init__()

        self.text = text
        self.command = command
        self.text_color = text_color

        self.choosing_rect = pg.Rect(self.rect.x + 10, self.rect.y + 10, 10, 10)

        self.font = pg.font.SysFont('', font_size)

        self.is_choose = False

        self.prep_text(text)

    def prep_text(self, text):
        self.text_image = self.font.render(text, True, self.text_color)

        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.x = self.rect.x + 5
        self.text_image_rect.y = self.rect.y + 5

    def update(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos  # Get mouse pos
            if self.choosing_rect.collidepoint(mouse_x, mouse_y):  # If button is clicked
                if not self.is_choose:
                    self.is_choose = True  # change flag is_choose
                    if self.command is not None:
                        self.command()  # If the command is registered, called it
                elif self.is_choose:
                    self.is_choose = False

        self.text_image_rect.left = self.rect.left + 30
        self.text_image_rect.top = self.rect.top + 20

        self.choosing_rect.x = self.rect.x + 10
        self.choosing_rect.y = self.rect.y + 10
