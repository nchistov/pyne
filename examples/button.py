import pyne

app = pyne.App(bg_color=(0, 0, 0))

btn = pyne.widgets.Button('Hello', command=lambda: print('Hello!'))  # Создаем кнопку

app.add_widget(btn)

app.run()
