import os

import pygame as pg


class CanvasObject:
    def __init__(self, info):
        self.info = info

        match info[0]:
            case 'point':
                self.rect = pg.Rect(info[1][0], info[1][1], 1, 1)

                self.x = info[1][0]
                self.y = info[1][1]

                self.color = info[2]
            case 'line':
                self.end_pos = info[2]

                self.x = info[1][0]
                self.y = info[1][1]

                self.color = info[3]

                self.line_width = info[4]
            case 'rect':
                self.rect = pg.Rect(info[1][0], info[1][1], info[2], info[3])

                self.x = info[1][0]
                self.y = info[1][1]

                self.color = info[4]
            case 'circle':
                self.x = info[1][0]
                self.y = info[1][1]

                self.R = info[2]

                self.color = info[3]
            case 'image':
                self.image = pg.image.load(info[1])

                self.x = info[2][0]
                self.y = info[2][1]

                self.rect = self.image.get_rect()
                self.rect.x = info[2][0]
                self.rect.y = info[2][1]
            case 'polygon':
                self.coordinates = info[1]

                self.color = info[2]
            case 'text':
                self.font = pg.font.Font(os.path.join(os.path.dirname(__file__), '../fonts/font.ttf'), info[3])

                self.text = info[2]

                self.text_image = self.font.render(info[2], True, info[4])

                self.text_image_rect = self.text_image.get_rect()

                self.x, self.y = info[1][0], info[1][1]

                self.text_image_rect.x = info[1][0]
                self.text_image_rect.y = info[1][1]

    def draw(self, screen: pg.Surface):
        match self.info[0]:
            case 'point':
                self.rect.x = self.x
                self.rect.y = self.y

                pg.draw.rect(screen, self.color, self.rect)
            case 'line':
                pg.draw.line(screen, self.color, (self.x, self.y), self.end_pos, self.line_width)
            case 'rect':
                self.rect.x = self.x
                self.rect.y = self.y

                pg.draw.rect(screen, self.color, self.rect)
            case 'circle':
                pg.draw.circle(screen, self.color, (self.x, self.y), self.R)
            case 'image':
                self.rect.x = self.x
                self.rect.y = self.y

                screen.blit(self.image, self.rect)
            case 'polygon':
                pg.draw.polygon(screen, self.color, self.coordinates)
            case 'text':
                self.text_image_rect.x = self.x
                self.text_image_rect.y = self.y

                screen.blit(self.text_image, self.text_image_rect)
