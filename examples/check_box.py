import pyne

app = pyne.App()
grid = pyne.widgets.Grid(5, 5)
app.add_widget(grid)

check = pyne.widgets.CheckBox('Say hello', command=lambda: print('Hello'), unset_command=lambda: print('Buy'))
check.set()

grid.add_widget(check, 0, 0, 5, 1)

app.run()
