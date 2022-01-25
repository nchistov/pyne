from pyne import App
from pyne.grid import Grid

from pyne.image import Image

app = App()

grid = Grid(app, 3, 3)

image = Image(app, 'image.png')
grid.add_image(image, 1, 1)

app.run()
