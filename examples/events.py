import pyne

app = pyne.App(window_pos=(50, 50))

app.add_handler("MouseLeft-Alt", lambda: print("Hello"))

app.run()
