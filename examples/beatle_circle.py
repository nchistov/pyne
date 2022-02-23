import pyne

app = pyne.App(window_size=(1100, 500))  # Creating white window 1100x500

grid = pyne.widgets.Grid(app, 1, 1)  # Adding grid
app.add_widget(grid)

beatle_screen = pyne.widgets.BeatleScreen(app)  # Adding screen for beatle
grid.add_widget(beatle_screen, 0, 0)

t = pyne.beatle.Beatle(beatle_screen)  # Creating Beatle

# Draw circle
for i in range(10, 361, 10):
    t.forward(10)
    t.setheading(i)

app.run()
t.stop()  # Stopping all process
