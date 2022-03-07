import pyne

app = pyne.App()
grid = pyne.widgets.Grid(app, 1, 1)
app.add_widget(grid)

scrolling_grid = pyne.widgets.Grid(app, 3, 3, scrolling=True)
grid.add_widget(scrolling_grid, 0, 0, 1, 3)

btn = pyne.widgets.Button('OK', command=lambda: print('OK'))
entry = pyne.widgets.Entry(prompt='Name')

scrolling_grid.add_widget(entry, 0, 1, 1, 0.1)
scrolling_grid.add_widget(btn, 0, 0, 1, 0.5)

app.run()
