import pyne

app = pyne.App()
grid = pyne.widgets.Grid(3, 3)
app.add_widget(grid)

link = pyne.widgets.LinkLabel(text='Pyne source code', url='https://gitflic.ru/project/pyne/pyne', press='center')

grid.add_widget(link, 1, 0, 3)

app.run()
