"""
module in which one are located all widgets
in package pyne
"""

import pygame as pg


class Widget:
    def __init__(self):
        self.row = 0
        self.column = 0

        self.max_rows = 0
        self.max_columns = 0

        self.width = 1
        self.height = 1

    def update(self, event):
        pass

    def draw(self, screen: pg.Surface):
        pass


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

        pg.font.init()

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
            mouse_x, mouse_y = event.pos  # Получаем координаты миши
            if self.rect.collidepoint(mouse_x, mouse_y):  # Если кнопка нажата
                self.current_color = self.active_color    # Изменяем цвет
                self.is_pressed = True                    # И флаг is_pressed
                if self.command is not None:
                    self.command()                        # Если комманда зарегестрирована, вызываем ее
        elif event.type == pg.MOUSEBUTTONUP:
            self.current_color = self.color
            self.is_pressed = False

        self.text_image_rect.center = self.rect.center

    def draw(self, screen):
        pg.draw.rect(screen, self.current_color, self.rect)
        screen.blit(self.text_image, self.text_image_rect)

        if not self.is_pressed:  # Если кнопка не нажата поррисовываем линии с краю
            pg.draw.line(screen, (200, 200, 200), (self.rect.right - 1,
                                                   self.rect.bottom),
                         (self.rect.right - 1, self.rect.top))

            pg.draw.line(screen, (200, 200, 200), (self.rect.right, self.rect.top),
                         (self.rect.left, self.rect.top))


class Label(Widget):
    def __init__(self, text: str, bg_color=(255, 255, 255), outline_color=(255, 255, 255),
                 text_color=(0, 0, 0), font_size=40, press='right'):
        super().__init__()

        self.text = text

        self.bg_color = bg_color
        self.outline_color = outline_color
        self.text_color = text_color

        self.press = press

        self.rect = pg.Rect(0, 0, 100, 50)

        self.font = pg.font.SysFont('', font_size)

        self.set_text(text)

    def set_text(self, text):
        self.text_image = self.font.render(text, True, self.text_color)

        self.text_image_rect = self.text_image.get_rect()

        match self.press:  # Прижимаем текст к нужниму краю
            case 'right':
                self.text_image_rect.right = self.rect.right - 3
            case 'left':
                self.text_image_rect.left = self.rect.left + 3
            case 'center':
                self.text_image_rect.centerx = self.rect.centerx

        self.text_image_rect.centery = self.rect.centery

    def draw(self, screen):
        pg.draw.rect(screen, self.bg_color, self.rect)
        screen.blit(self.text_image, self.text_image_rect)

        # Рисуем рамку
        pg.draw.line(screen, self.outline_color, (self.rect.right, self.rect.bottom), (self.rect.right, self.rect.top))
        pg.draw.line(screen, self.outline_color, (self.rect.right, self.rect.top), (self.rect.left, self.rect.top))
        pg.draw.line(screen, self.outline_color, (self.rect.left, self.rect.top), (self.rect.left, self.rect.bottom))
        pg.draw.line(screen, self.outline_color, (self.rect.left, self.rect.bottom),
                     (self.rect.right, self.rect.bottom))
