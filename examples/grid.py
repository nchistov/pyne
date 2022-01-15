from pyne.app import App
from pyne.widgets import Button
from pyne.grid import Grid

btn = Button('Hello', command=lambda: print('Hello!'))

grid = Grid(3, 3)
grid.add_widget(btn, 1, 1)

app = App()

app.add_widget(btn)

app.run()
