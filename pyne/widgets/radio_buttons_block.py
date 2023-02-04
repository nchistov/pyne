import pygame as pg

from .radio_button import RadioButton
from .base_widget import Widget


class SpecialRadioButton(RadioButton):
    def __init__(self, text, radio_buttons, text_color=(0, 0, 0), font_size=25):
        super().__init__(text, text_color=text_color, font_size=font_size)

        self.radio_buttons = radio_buttons

    def update(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos  # Получаем координаты мыши
            if self.choosing_rect.collidepoint(mouse_x, mouse_y):  # Если кнопка нажата
                if not self.is_choose:
                    self.is_choose = True  # Изменяем флаг is_choose
                    self.color = (25, 155, 250)  # и цвет

                    for r_btn in self.radio_buttons:
                        if r_btn != self:
                            r_btn.unset()
                elif self.is_choose:
                    self.is_choose = False

                    self.color = (255, 255, 255)


class RadioButtonsBlock(Widget):
    def __init__(self, texts: list[str], y_step=15):
        super().__init__()

        self.texts = texts
        self.y_step = y_step

        self._current_text = ''
        self.current_radio_button = None

        self.radio_buttons: list[SpecialRadioButton] = []

        self._generate()

    def _generate(self):
        self.radio_buttons = []
        y = 5

        for text in self.texts:
            new_radio_button = SpecialRadioButton(text, self.radio_buttons)
            new_radio_button.set_rect(self.rect.x, self.rect.y + y, 10, 10)
            self.radio_buttons.append(new_radio_button)

            y += self.y_step

    def get_selected(self) -> str | None:
        for r_btn in self.radio_buttons:
            if r_btn.is_choose:
                return r_btn.text
        return None

    def set_rect(self, x, y, width, height):
        super().set_rect(x, y, width, height)
        self._generate()

    def update(self, event):
        for radio_button in self.radio_buttons:
            radio_button.update(event)

    def draw(self, screen: pg.Surface):
        for radio_button in self.radio_buttons:
            radio_button.draw(screen)
