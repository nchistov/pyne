from pyne.app import App
from pyne.grid import Grid
from pyne.widgets import Button, Label

calculation = ''

grid = Grid(5, 4)

app = App((500, 700))


def add_symbol(symbol: str):
    global calculation
    if not symbol.isdigit() and len(calculation) >= 1:
        calculation += symbol
    elif symbol.isdigit():
        calculation += symbol
    label.set_text(calculation)


def equal():
    global calculation
    try:
        calculation = str(eval(calculation))
        label.set_text(calculation)
    except (ArithmeticError, SyntaxError, TypeError):
        calculation = ''
        label.set_text('-E-')


def clear():
    global calculation
    calculation = ''
    label.set_text(calculation)


# Создаем кнопки
btn0 = Button('0', command=lambda: add_symbol('0'))
btn1 = Button('1', command=lambda: add_symbol('1'))
btn2 = Button('2', command=lambda: add_symbol('2'))
btn3 = Button('3', command=lambda: add_symbol('3'))
btn4 = Button('4', command=lambda: add_symbol('4'))
btn5 = Button('5', command=lambda: add_symbol('5'))
btn6 = Button('6', command=lambda: add_symbol('6'))
btn7 = Button('7', command=lambda: add_symbol('7'))
btn8 = Button('8', command=lambda: add_symbol('8'))
btn9 = Button('9', command=lambda: add_symbol('9'))

multiply_btn = Button('*', command=lambda: add_symbol('*'))
minus_btn = Button('-', command=lambda: add_symbol('-'))
plus_btn = Button('+', command=lambda: add_symbol('+'))
divide_btn = Button('/', command=lambda: add_symbol('/'))

enter = Button('=', command=equal)

clear_btn = Button('C', command=clear)

label = Label(calculation, outline_color=(0, 0, 0))

grid.add_widget(btn0, 4, 0)
grid.add_widget(btn1, 3, 0)
grid.add_widget(btn2, 3, 1)
grid.add_widget(btn3, 3, 2)
grid.add_widget(btn4, 2, 0)
grid.add_widget(btn5, 2, 1)
grid.add_widget(btn6, 2, 2)
grid.add_widget(btn7, 1, 0)
grid.add_widget(btn8, 1, 1)
grid.add_widget(btn9, 1, 2)

grid.add_widget(plus_btn, 4, 2)
grid.add_widget(minus_btn, 4, 3)
grid.add_widget(multiply_btn, 3, 3)
grid.add_widget(divide_btn, 2, 3)

grid.add_widget(enter, 4, 1)

grid.add_widget(clear_btn, 1, 3)

grid.add_widget(label, 0, 0, 4, 1)

app.add_widget(btn0)
app.add_widget(btn1)
app.add_widget(btn2)
app.add_widget(btn3)
app.add_widget(btn4)
app.add_widget(btn5)
app.add_widget(btn6)
app.add_widget(btn7)
app.add_widget(btn8)
app.add_widget(btn9)

app.add_widget(plus_btn)
app.add_widget(minus_btn)
app.add_widget(multiply_btn)
app.add_widget(divide_btn)

app.add_widget(enter)

app.add_widget(clear_btn)

app.add_widget(label)

app.run()
