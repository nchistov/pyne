import pyne

app = pyne.App()
grid = pyne.widgets.Grid(10, 10)
app.add_widget(grid)

numeric = pyne.widgets.NumericUpDown()

grid.add_widget(numeric, 1, 1, 2)

app.run()
