import pyne

app = pyne.App()
grid = pyne.widgets.Grid(3, 3)

app.add_widget(grid)

btn = pyne.widgets.Button('OK', command=lambda: print('OK'))
grid.add_widget(btn, 0, 0)

grid.change_pos_of_widget(btn, 2, 2)

app.run()
