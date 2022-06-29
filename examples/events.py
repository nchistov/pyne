import pyne

app = pyne.App(window_pos=(0, 0))

app.add_handler("MouseLeft-Alt", lambda: print("Hello"))

app.run()
