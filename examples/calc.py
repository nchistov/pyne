import pyne

calculation = ''

app = pyne.App((500, 700), title='Calc')

grid = pyne.widgets.Grid(app, 5, 4)
app.add_widget(grid)


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
btn0 = pyne.widgets.Button('0', command=lambda: add_symbol('0'))
btn1 = pyne.widgets.Button('1', command=lambda: add_symbol('1'))
btn2 = pyne.widgets.Button('2', command=lambda: add_symbol('2'))
btn3 = pyne.widgets.Button('3', command=lambda: add_symbol('3'))
btn4 = pyne.widgets.Button('4', command=lambda: add_symbol('4'))
btn5 = pyne.widgets.Button('5', command=lambda: add_symbol('5'))
btn6 = pyne.widgets.Button('6', command=lambda: add_symbol('6'))
btn7 = pyne.widgets.Button('7', command=lambda: add_symbol('7'))
btn8 = pyne.widgets.Button('8', command=lambda: add_symbol('8'))
btn9 = pyne.widgets.Button('9', command=lambda: add_symbol('9'))

multiply_btn = pyne.widgets.Button('*', command=lambda: add_symbol('*'))
minus_btn = pyne.widgets.Button('-', command=lambda: add_symbol('-'))
plus_btn = pyne.widgets.Button('+', command=lambda: add_symbol('+'))
divide_btn = pyne.widgets.Button('/', command=lambda: add_symbol('/'))

enter = pyne.widgets.Button('=', command=equal)

clear_btn = pyne.widgets.Button('AC', command=clear)

label = pyne.widgets.Label(calculation, outline_color=(0, 0, 0))

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

app.run()
