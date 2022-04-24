import pyne

app = pyne.App()
grid = pyne.widgets.Grid(3, 3)

app.add_widget(grid)

panel1 = pyne.widgets.Panel(color=(0, 0, 0))
panel2 = pyne.widgets.Panel(color=(255, 0, 0))

grid.add_widget(panel1, 0, 0, 2, 2)
grid.add_widget(panel2, 1, 1, 2, 2, priority=0)

app.run()
