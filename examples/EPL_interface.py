import pyne

app = pyne.App(window_size=(1100, 500))

grid = pyne.Grid(app, 10, 7)

beatle_screen = pyne.widgets.BeatleScreen(app)
grid.add_widget(beatle_screen, 0, 0, 2.5, 9)

t = pyne.beatle.Beatle(beatle_screen)

run_button = pyne.widgets.Button('Запустить', color=(230, 230, 230), active_color=(150, 150, 150), font_size=30)

grid.add_widget(run_button, 9, 0.5)

app.run()
t.stop()  # Stopping all process
