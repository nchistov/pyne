import pyne

app = pyne.App()
grid = pyne.Grid(app, 3, 3)

panel = pyne.widgets.Panel((255, 0, 0), (0, 0, 0))
grid.add_widget(panel, 1, 1)

app.run()
