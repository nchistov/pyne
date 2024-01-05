import pygame as pg

from .base_widget import Widget
from ..beatle import Beatle


class BeatleScreen(Widget):
    default_values = {'color': (255, 255, 255), 'outline_color': (150, 150, 150)}
    css_name = 'beatle-screen'

    def __init__(self, color: tuple[int, int, int] | None = None,
                 outline_color: tuple[int, int, int] | None = None, name: str = ''):
        super().__init__(name=name)

        self.css_customizable_fields = {'color', 'outline_color'}

        self._update_fields(locals())

        self.beatles: list[Beatle] = []

        self.rect = pg.Rect(0, 0, 10, 10)

        self.surface = pg.Surface(self.rect.size)

    def set_rect(self, x: int, y: int, width: int, height: int):
        super().set_rect(x, y, width, height)

        self.surface = pg.Surface(self.rect.size)

    def add_beatle(self, beatle: Beatle):
        beatle.base_x, beatle.base_y = self.rect.center

        beatle.rect.x = beatle.base_x + beatle.x
        beatle.rect.y = beatle.base_y + beatle.y

        beatle.is_down = True

        self.beatles.append(beatle)

    def remove_beatle(self, beatle: Beatle):
        if beatle in self.beatles:
            self.beatles.remove(beatle)

    def draw(self, screen: pg.Surface):
        self.surface.fill(self.color)

        for beatle in self.beatles:
            beatle.draw(self.surface)

        screen.blit(self.surface, self.rect)

        # Рисуем рамку
        pg.draw.line(screen, self.outline_color, (self.rect.x, self.rect.y),
                     (self.rect.right, self.rect.y))
        pg.draw.line(screen, self.outline_color, (self.rect.right, self.rect.y),
                     (self.rect.right, self.rect.bottom))
        pg.draw.line(screen, self.outline_color, (self.rect.right, self.rect.bottom),
                     (self.rect.left, self.rect.bottom))
        pg.draw.line(screen, self.outline_color, (self.rect.left, self.rect.bottom),
                     (self.rect.x, self.rect.y))
