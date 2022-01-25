import pygame as pg

from .base_widget import Widget


class Button(Widget):
    def __init__(self, text: str, color=(150, 150, 150), active_color=(70, 200, 215),
                 text_color=(0, 0, 0), font_size=40, command: callable = None):
        super().__init__()
        self.text = text
        self.color = color
        self.active_color = active_color
        self.text_color = text_color
        self.command = command

        self.current_color = color

        self.is_pressed = False

        self.rect = pg.Rect(0, 0, len(text) * 17, 35)

        self.font = pg.font.SysFont('', font_size)

        self.prep_text(text)

    def prep_text(self, text):
        self.text_image = self.font.render(text, True, self.text_color)

        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.x = self.rect.x + 5
        self.text_image_rect.y = self.rect.y + 5

    def update(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos  # Get mouse pos
            if self.rect.collidepoint(mouse_x, mouse_y):  # If button is clicked
                self.current_color = self.active_color    # change color
                self.is_pressed = True                    # and flag is_pressed
                if self.command is not None:
                    self.command()                        # If the command is registered, called it
        elif event.type == pg.MOUSEBUTTONUP:
            self.current_color = self.color
            self.is_pressed = False

        self.text_image_rect.center = self.rect.center

    def draw(self, screen):
        pg.draw.rect(screen, self.current_color, self.rect)
        screen.blit(self.text_image, self.text_image_rect)

        if not self.is_pressed:  # If button isn't clicked draw outlines
            pg.draw.line(screen, (200, 200, 200), (self.rect.right - 1,
                                                   self.rect.bottom),
                         (self.rect.right - 1, self.rect.top))

            pg.draw.line(screen, (200, 200, 200), (self.rect.right, self.rect.top),
                         (self.rect.left, self.rect.top))