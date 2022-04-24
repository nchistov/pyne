import pyne

app = pyne.App()
grid = pyne.widgets.Grid(3, 3)
app.add_widget(grid)

sub_grid = pyne.widgets.Grid(3, 3)
grid.add_widget(sub_grid, 1, 1)

btn = pyne.widgets.Button('OK', command=lambda: print('OK'))
btn2 = pyne.widgets.Button('1', font_size=20, command=lambda: print('1'))

grid.add_widget(btn, 2, 1)
sub_grid.add_widget(btn2, 2, 2)

app.run()
