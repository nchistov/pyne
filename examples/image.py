from pyne.app import App
from pyne.image import Image

app = App()

image = Image(app, 'image.png')
app.add_to_schedule(image.draw)

app.run()
