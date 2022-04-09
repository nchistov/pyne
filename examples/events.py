import pyne

app = pyne.App()

app.add_handler("MouseLeft-Alt", lambda: print("Hello"))

app.run()
