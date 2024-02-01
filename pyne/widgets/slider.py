import pygame as pg

from .base_widget import Widget


class Slider(Widget):
    def __init__(self, min_value: int, max_value: int, color: tuple[int, int, int] = (0, 0, 0),
                 circle_color: tuple[int, int ,int] = (150, 150, 150), name: str = ''):
        super().__init__(name=name)

        self.slider_rect = pg.Rect(0, 0, 15, 15)

        self.min_value = min_value
        self.max_value = max_value
        self.color = color
        self.circle_color = circle_color

        self.is_mouse_pressed = False

        self.value = min_value

        self.value_per_pixel = 0.0

    def set_rect(self, x: int, y: int, width: int, height: int):
        super().set_rect(x, y, width, height)
        self.slider_rect.centery = y + 7
        self.slider_rect.x = self.rect.x

        self.value_per_pixel = (self.max_value - self.min_value) /\
                               (self.rect.right - self.rect.left)

    def update(self, event: pg.event.Event):
        if self.is_mouse_pressed:
            self.slider_rect.x = pg.mouse.get_pos()[0]
            if self.slider_rect.right > self.rect.right:
                self.slider_rect.right = self.rect.right
            elif self.slider_rect.x < self.rect.x:
                self.slider_rect.x = self.rect.x

            self.value = self.min_value + round(
                (self.slider_rect.x - self.rect.left) * self.value_per_pixel
            )

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                if self.slider_rect.collidepoint(mouse_x, mouse_y):
                    self.is_mouse_pressed = True
        elif event.type == pg.MOUSEBUTTONUP:
            self.is_mouse_pressed = False

    def draw(self, screen: pg.Surface):
        pg.draw.line(screen, self.color, (self.rect.left, self.rect.y),
                     (self.rect.left, self.rect.y + 15))
        pg.draw.line(screen, self.color, (self.rect.right, self.rect.y),
                     (self.rect.right, self.rect.y + 15))
        pg.draw.line(screen, self.color, (self.rect.left, self.rect.y + 7),
                     (self.rect.right, self.rect.y + 7))

        pg.draw.circle(screen, self.circle_color, self.slider_rect.center,
                       self.slider_rect.height / 2)
