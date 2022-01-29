from pyne import App
from pyne.grid import Grid

from pyne.widgets import beatle_screen, button

app = App(window_size=(1100, 500))

grid = Grid(app, 10, 7)

beatle_screen = beatle_screen.BeatleScreen(app)
run_button = button.Button('Запустить', color=(230, 230, 230), active_color=(150, 150, 150))

grid.add_widget(beatle_screen, 0, 0, 2.5, 9)
grid.add_widget(run_button, 9, 0.5)

app.run()
