from pyne import App
from pyne.grid import Grid

from pyne.widgets import beatle_screen

from pyne import beatle

app = App(window_size=(1100, 500))  # Creating white window 1100x500

grid = Grid(app, 1, 1)  # Adding grid

beatle_screen = beatle_screen.BeatleScreen(app)  # Adding screen for beatle
grid.add_widget(beatle_screen, 0, 0)

t = beatle.Beatle(beatle_screen)  # Creating Beatle

# Draw circle
for i in range(10, 361, 10):
    t.forward(10)
    t.setheading(i)

app.run()
t.stop()  # Stopping all process
