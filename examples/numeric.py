import pyne

app = pyne.App()
grid = pyne.widgets.Grid(app, 10, 10)
app.add_widget(grid)

numeric = pyne.widgets.NumericUpDown()

grid.add_widget(numeric, 1, 1)

app.run()
