import os

from pyne import App
from pyne.grid import Grid

from pyne.image import Image

app = App()

grid = Grid(app, 3, 3)

image = Image(app, os.path.join(os.path.dirname(__file__), 'image.png'))
image2 = Image(app, os.path.join(os.path.dirname(__file__), 'image.png'))

grid.add_image(image, 0, 0)
grid.add_image(image2, 1, 1, size_correction=True)

app.run()
