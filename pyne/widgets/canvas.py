import pygame as pg

from .base_widget import Widget

from ._canvas_object import CanvasObject


class Canvas(Widget):
    def __init__(self, bg_color=(255, 255, 255), outline_color=(255, 255, 255)):
        super().__init__()

        self.bg_color = bg_color
        self.outline_color = outline_color

        self.surface = pg.Surface(self.rect.size)

        self.width = 0
        self.height = 0

        self.objects = []

    def set_rect(self, x, y, width, height):
        super().set_rect(x, y, width, height)

        self.width, self.height = width, height

        self.surface = pg.Surface(self.rect.size)

    def draw_point(self, x: int, y: int, color=(0, 0, 0)) -> int:
        new_obj = CanvasObject(('point', (x, y), color))
        self.objects.append(new_obj)

        return len(self.objects) - 1

    def draw_line(self, x1: int, y1: int, x2: int, y2: int, color=(0, 0, 0), width=1) -> int:
        new_obj = CanvasObject(('line', (x1, y1), (x2, y2), color, width))
        self.objects.append(new_obj)

        return len(self.objects) - 1

    def draw_rect(self, x: int, y: int, width: int, height: int, color=(0, 0, 0)) -> int:
        new_obj = CanvasObject(('rect', (x, y), width, height, color))
        self.objects.append(new_obj)

        return len(self.objects) - 1

    def draw_circle(self, x: int, y: int, R: int, color=(0, 0, 0)) -> int:
        new_obj = CanvasObject(('circle', (x, y), R, color))
        self.objects.append(new_obj)

        return len(self.objects) - 1

    def draw_polygon(self, coordinates, color=(0, 0, 0)) -> int:
        new_obj = CanvasObject(('polygon', coordinates, color))
        self.objects.append(new_obj)

        return len(self.objects) - 1

    def draw_image(self, file_name: str, x: int, y: int) -> int:
        new_obj = CanvasObject(('image', file_name, (x, y)))
        self.objects.append(new_obj)

        return len(self.objects) - 1

    def draw_text(self, text: str, x: int, y: int, font_size: int, color=(0, 0, 0)):
        new_obj = CanvasObject(('text', (x, y), text, font_size, color))
        self.objects.append(new_obj)

        return len(self.objects) - 1

    def move(self, obj: int, x, y):
        new_coordinates = []

        if self.objects[obj].info[0] == 'polygon':  # Если надо двигать многоугольник, подвинем все углы
            for pos in self.objects[obj].coordinates:
                new_coordinates.append((pos[0] + x, pos[1] + y))

                self.objects[obj].coordinates = new_coordinates

            return

        self.objects[obj].x += x
        self.objects[obj].y += y

        if self.objects[obj].info[0] == 'line':  # Если надо двигать линию, изменяем не только start_pos
            new_end_pos = self.objects[obj].end_pos[0] + x, self.objects[obj].end_pos[1] + y  # end_pos тоже

            self.objects[obj].end_pos = new_end_pos

    def delete(self, obj: int):
        try:
            del self.objects[obj]
        except IndexError:
            pass

    def save_to_file(self, file_name: str):
        pg.image.save(self.surface, file_name)

    def draw(self, screen: pg.Surface):
        self.surface.fill(self.bg_color)

        for obj in self.objects:
            obj.draw(self.surface)

        screen.blit(self.surface, self.rect)

        # Рисуем рамку
        pg.draw.line(screen, self.outline_color, (self.rect.right, self.rect.bottom),
                     (self.rect.right, self.rect.top))
        pg.draw.line(screen, self.outline_color, (self.rect.right, self.rect.top),
                     (self.rect.left, self.rect.top))
        pg.draw.line(screen, self.outline_color, (self.rect.left, self.rect.top),
                     (self.rect.left, self.rect.bottom))
        pg.draw.line(screen, self.outline_color, (self.rect.left, self.rect.bottom),
                     (self.rect.right, self.rect.bottom))
