import pyne

app = pyne.App()
grid = pyne.widgets.Grid(app, 3, 3)
app.add_widget(grid)

link = pyne.widgets.LinkLabel(text='Python', url='https://www.python.org/')

grid.add_widget(link, 1, 1)

app.run()
