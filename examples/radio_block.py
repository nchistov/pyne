import pyne

app = pyne.App()
grid = pyne.widgets.Grid(app, 3, 3)
app.add_widget(grid)

block = pyne.widgets.RadioButtonsBlock(['Hello #1', 'Hello #2', 'Hello #3'])

grid.add_widget(block, 1, 1)

app.run()
