import pygame as pg


class App:
    """Class App, it is a class which manages windows"""

    def __init__(self, window_size=(500, 500), title="Pyne", bg_color=(255, 255, 255)):
        """
        :param window_size: list or tuple of two numbers: first width and last height
        :param title: title of the window
        :param bg_color: color of background, in format RGB
        """
        pg.init()

        self.screen = pg.display.set_mode(window_size)
        pg.display.set_caption(title)

        self.clock = pg.time.Clock()

        self.time_table = []
        self.widgets = []
        self.running = False
        self.bg = bg_color
        self.fps = 30

    def add_to_time_table(self, func: callable):
        """
        :param func: function which one need to append to time_table
        :return: None
        """
        self.time_table.append(func)

    def add_widget(self, widget):
        try:
            sell_height = self.screen.get_height() / widget.max_rows
            sell_width = self.screen.get_width() / widget.max_columns

            widget.rect.x = widget.column * sell_width
            widget.rect.y = widget.row * sell_height

            widget.rect.width = sell_width * widget.width
            widget.rect.height = sell_height * widget.height
        except ZeroDivisionError:
            pass

        self.widgets.append(widget)

    def _check_events(self):
        for event in pg.event.get():
            match event.type:
                case pg.QUIT:
                    self.quit()

            for widget in self.widgets:
                widget.update(event)

    def run(self):
        """method which start mainloop"""
        self.running = True
        while self.running:
            self.screen.fill(self.bg)

            for business in self.time_table:
                business()

            for widget in self.widgets:
                widget.draw(self.screen)

            self._check_events()

            pg.display.flip()

            self.clock.tick()

        pg.quit()

    def quit(self):
        """change running to False"""
        self.running = False
