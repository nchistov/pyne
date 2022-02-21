import pyne

app = pyne.App()
grid = pyne.Grid(app, 3, 3)

sub_grid = pyne.Grid(app, 3, 3, 25, 25, 50, 50)

btn = pyne.widgets.Button('OK', command=lambda: print('OK'))
btn2 = pyne.widgets.Button('1', font_size=20, command=lambda: print('1'))

grid.add_widget(btn, 2, 1)
sub_grid.add_widget(btn2, 2, 2)

app.run()
