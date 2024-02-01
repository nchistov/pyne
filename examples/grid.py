import pyne

app = pyne.App()

btn1 = pyne.widgets.Button('1', command=lambda: print('Hello from btn1!'))
btn2 = pyne.widgets.Button('2', command=lambda: print('Hello from btn2!'))

grid = pyne.widgets.Grid(5, 5)
app.add_widget(grid)

grid.add_widget(btn1, 1, 0)
grid.add_widget(btn2, 1, 1)

app.add_widget(btn1)
app.add_widget(btn2)

app.run()
