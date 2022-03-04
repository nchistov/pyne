import pygame as pg

from .base_widget import Widget


class Button(Widget):
    def __init__(self, text: str, color=(150, 150, 150), active_color=(70, 200, 215),
                 text_color=(0, 0, 0), font_size=40, command: callable = None,
                 image=None, press='left', sound=None):
        super().__init__()
        self.text = text
        self.color = color
        self.active_color = active_color
        self.text_color = text_color
        self.command = command

        self.press = press

        self.current_color = color
        self.sound = sound

        self.is_pressed = False

        self.has_image = False

        if image is not None:
            self.image = pg.image.load(image)
            self.image_rect = self.image.get_rect()

            self.has_image = True

        self.rect = pg.Rect(0, 0, len(text) * 17, 35)

        self.font = pg.font.SysFont('', font_size)

        self.prep_text(text)

    def prep_text(self, text):
        self.text_image = self.font.render(text, True, self.text_color)

        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.x = self.rect.x + 5
        self.text_image_rect.y = self.rect.y + 5

    def set_rect(self, x, y, width, height):
        super().set_rect(x, y, width, height)

        self.text_image_rect.center = self.rect.center

        if self.has_image:
            match self.press:
                case 'right top':
                    self.image_rect.top = self.rect.top
                    self.image_rect.right = self.rect.right
                case 'right':
                    self.image_rect.centery = self.rect.centery
                    self.image_rect.right = self.rect.right
                case 'right bottom':
                    self.image_rect.bottom = self.rect.bottom
                    self.image_rect.right = self.rect.right
                case 'center top':
                    self.image_rect.top = self.rect.top
                    self.image_rect.centerx = self.rect.centerx
                case 'center':
                    self.image_rect.centery = self.rect.centery
                    self.image_rect.centerx = self.rect.centerx
                case 'center bottom':
                    self.image_rect.bottom = self.rect.bottom
                    self.image_rect.centerx = self.rect.centerx
                case 'left top':
                    self.image_rect.top = self.rect.top
                    self.image_rect.left = self.rect.left
                case 'left':
                    self.image_rect.centery = self.rect.centery
                    self.image_rect.left = self.rect.left
                case 'left bottom':
                    self.image_rect.bottom = self.rect.bottom
                    self.image_rect.left = self.rect.left
                case _:
                    raise ValueError('incorrect word to pressing image')

    def update(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos  # Get mouse pos
            if self.rect.collidepoint(mouse_x, mouse_y):  # If button is clicked
                self.current_color = self.active_color    # change color
                self.is_pressed = True                    # and flag is_pressed
                if self.command is not None:
                    self.command()                        # If the command is registered, called it
                if self.sound is not None:
                    self.sound.play()

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
        if self.has_image:
            screen.blit(self.image, self.image_rect)
