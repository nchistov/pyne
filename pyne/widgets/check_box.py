import pygame as pg

from .base_widget import Widget


class CheckBox(Widget):
    def __init__(self, text, command=None, unset_command=None, text_color=(0, 0, 0), font_size=25):
        super().__init__()

        self.text = text
        self.command = command
        self.unset_command = unset_command
        self.text_color = text_color

        self.color = (255, 255, 255)

        self.choosing_rect = pg.Rect(self.rect.x + 10, self.rect.y + 10, 10, 10)

        self.bg_rect = pg.Rect(self.rect.x + 9, self.rect.y + 9, 12, 12)

        self.font = pg.font.SysFont('', font_size)

        self.is_choose = False

        self.set_text(text)

    def set_rect(self, x, y, width, height):
        super().set_rect(x, y, width, height)

        self.text_image_rect.left = self.rect.left + 30
        self.text_image_rect.top = self.rect.top + 8

        self.choosing_rect.x = self.rect.x + 10
        self.choosing_rect.y = self.rect.y + 10

        self.bg_rect.x = self.rect.x + 9
        self.bg_rect.y = self.rect.y + 9

    def set_text(self, text):
        self.text_image = self.font.render(text, True, self.text_color)

        self.text_image_rect = self.text_image.get_rect()

        self.text_image_rect.left = self.rect.left + 30
        self.text_image_rect.top = self.rect.top + 8

        self.choosing_rect.x = self.rect.x + 10
        self.choosing_rect.y = self.rect.y + 10

    def set(self):
        self.is_choose = True
        self.color = (25, 155, 250)

    def unset(self):
        self.is_choose = False
        self.color = (255, 255, 255)

    def update(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos  # Get mouse pos
            if self.choosing_rect.collidepoint(mouse_x, mouse_y):  # If button is clicked
                if not self.is_choose:
                    self.is_choose = True  # change flag is_choose
                    self.color = (25, 155, 250)  # and color

                    if self.command is not None:
                        self.command()  # If the command is registered, called it
                elif self.is_choose:
                    self.is_choose = False

                    if self.unset_command is not None:
                        self.unset_command()  # If the unset_command is registered, called it

                    self.color = (255, 255, 255)

    def draw(self, screen: pg.Surface):
        screen.blit(self.text_image, self.text_image_rect)
        pg.draw.rect(screen, (0, 0, 0), self.bg_rect)
        pg.draw.rect(screen, self.color, self.choosing_rect)

        if self.is_choose:
            pg.draw.line(screen, (255, 255, 255), (self.choosing_rect.x + 1, self.choosing_rect.y + 5),
                         (self.choosing_rect.centerx - 2, self.choosing_rect.bottom - 1), width=2)
            pg.draw.line(screen, (255, 255, 255), (self.choosing_rect.centerx - 2, self.choosing_rect.bottom - 1),
                         (self.choosing_rect.right - 2, self.choosing_rect.top + 2), width=2)
