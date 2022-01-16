from pyne.app import App
from pyne.widgets import Button
from pyne.grid import Grid

btn1 = Button('1', command=lambda: print('Hello from btn1!'))
btn2 = Button('2', command=lambda: print('Hello from btn2!'))

grid = Grid(5, 5)
grid.add_widget(btn1, 1, 0)
grid.add_widget(btn2, 1, 1)

app = App()

app.add_widget(btn1)
app.add_widget(btn2)

app.run()
