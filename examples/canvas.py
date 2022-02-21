import pyne

app = pyne.App()
grid = pyne.Grid(app, 1, 1)

canvas = pyne.widgets.Canvas((0, 255, 150))
grid.add_widget(canvas, 0, 0)

canvas.draw_point(5, 5, (255, 0, 0))
canvas.draw_line(10, 10, 25, 25, (255, 0, 0))
canvas.draw_line(200, 200, 250, 255, (255, 0, 0), 5)
canvas.draw_rect(30, 50, 50, 200, (0, 0, 255))
canvas.draw_circle(150, 150, 10, (255, 255, 0))

app.run()
