import pyne

app = pyne.App()
grid = pyne.widgets.Grid(app, 3, 3)
app.add_widget(grid)

file_dialog = pyne.widgets.FileDialog()
grid.add_widget(file_dialog, 0, 0, 3, 3)

app.run()
