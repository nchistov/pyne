import os

import pyne

app = pyne.App()

grid = pyne.Grid(app, 3, 3)

image = pyne.image.Image(app, os.path.join(os.path.dirname(__file__), 'image.png'))
image2 = pyne.image.Image(app, os.path.join(os.path.dirname(__file__), 'image.png'))

grid.add_image(image, 0, 0)
grid.add_image(image2, 1, 1, size_correction=True)

app.run()
