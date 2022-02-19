import pyne

app = pyne.App()
grid = pyne.Grid(app, 5, 5)

check = pyne.widgets.CheckBox('Say hello', command=lambda: print('Hello'))

grid.add_widget(check, 0, 0, 5, 1)

app.run()
