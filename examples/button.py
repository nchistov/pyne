from pyne.app import App
from pyne.widgets import Button

btn = Button('Hello', command=lambda: print('Hello!'))

app = App()

app.add_widget(btn)

app.run()
