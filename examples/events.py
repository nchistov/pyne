import pyne

app = pyne.App()

app.add_handler("PageDown", lambda: print("Hello"))

app.run()
