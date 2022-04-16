import pyne

app = pyne.App()
grid = pyne.widgets.Grid(app, 3, 3)
app.add_widget(grid)

slider = pyne.widgets.Slider(0, 100)

grid.add_widget(slider, 1, 1)

app.run()
