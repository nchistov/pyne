import pyne

app = pyne.App()
grid = pyne.widgets.Grid(3, 3)
app.add_widget(grid)

panel = pyne.widgets.Panel((255, 0, 0), (0, 0, 0))
grid.add_widget(panel, 1, 1)

app.run()
