import pyne

app = pyne.App()

app.add_handler("MouseLeft-LeftAlt", lambda: print("Hello"))

app.run()
