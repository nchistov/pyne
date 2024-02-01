import pyne

app = pyne.App()
grid = pyne.widgets.Grid(10, 3)

app.add_widget(grid)

entry = pyne.widgets.Entry(prompt='password', text='MyPassword')

grid.add_widget(entry, 4, 1)

app.run()
