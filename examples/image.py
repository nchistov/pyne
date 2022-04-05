import pyne

app = pyne.App()
grid = pyne.widgets.Grid(app, 3, 3)
app.add_widget(grid)

img = pyne.widgets.ImageBox('image.png')
grid.add_widget(img, 1, 1)

img.scale()

app.run()
