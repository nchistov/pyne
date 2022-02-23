import pyne

app = pyne.App()
grid = pyne.widgets.Grid(app, 1, 1)
app.add_widget(grid)

canvas = pyne.widgets.Canvas((0, 255, 150))
grid.add_widget(canvas, 0, 0)

canvas.draw_point(5, 5, (255, 0, 0))
canvas.draw_line(10, 10, 25, 25, (255, 0, 0))
canvas.draw_line(200, 200, 250, 255, (255, 0, 0), 5)
canvas.draw_rect(30, 50, 50, 200, (0, 0, 255))
canvas.draw_circle(150, 150, 10, (255, 255, 0))
image = canvas.draw_image('image.png', 0, 350)
canvas.draw_polygon(((400, 50), (450, 100), (400, 150)))

x = 0

moving = 'left'


def f():
    global x, moving

    if x < 450 and moving == 'left':
        canvas.move(image, 1, 0)
        x += 1
    elif x > 348:
        moving = 'right'
    if x > 0 and moving == 'right':
        canvas.move(image, -1, 0)
        x -= 1
    elif x < 2:
        moving = 'left'


app.add_to_schedule(f)
app.run()
