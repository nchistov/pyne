from pyne import App
from pyne.grid import Grid

from pyne.widgets import beatle_screen

from pyne import beatle

app = App(window_size=(1100, 500))

grid = Grid(app, 1, 1)

beatle_screen = beatle_screen.BeatleScreen(app)
grid.add_widget(beatle_screen, 0, 0)

t = beatle.Beatle(beatle_screen)

steps = 100


def f():
    global steps
    if steps > 0:
        t.forward(10)
    steps -= 1


app.add_to_schedule(f)

app.run()
t.stop()  # Stopping all process
