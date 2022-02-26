import pyne

app = pyne.App()
grid = pyne.widgets.Grid(app, 3, 3)

app.add_widget(grid)

btn = pyne.widgets.Button('OK', command=lambda: print('OK'), image='image.png', sound='pop.wav')

grid.add_widget(btn, 1, 1)

app.run()
