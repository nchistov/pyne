import pyne

app = pyne.App(window_size=(1100, 500))

grid = pyne.widgets.Grid(1, 2)
app.add_widget(grid)

beatle_screen = pyne.widgets.BeatleScreen()  # Создаем экран для Beatle
grid.add_widget(beatle_screen, 0, 0, 1)

t = pyne.beatle.Beatle(beatle_screen)  # Создаем Beatle
beatle_screen.add_beatle(t)

# Рисуем круг
for i in range(10, 361, 10):
    t.forward(10)
    t.setheading(i)

t.forward(500)
t.reset()

app.run()
t.stop()  # Останавливаем все процессы
