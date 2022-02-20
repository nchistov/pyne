import pyne

app = pyne.App()
grid = pyne.Grid(app, 1, 1)

canvas = pyne.widgets.Canvas((0, 255, 150))
grid.add_widget(canvas, 0, 0)

canvas.point(5, 5, (255, 0, 0))

app.run()
