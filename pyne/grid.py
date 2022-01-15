class Grid:
    def __init__(self, rows, columns):
        self.rows = rows - 1
        self.columns = columns - 1

    def add_widget(self, widget, row, column):
        try:
            widget.max_rows = self.rows
            widget.max_columns = self.columns

            widget.row = row
            widget.column = column

        except AttributeError:
            raise AttributeError("Widget must have got attributes max_rows, max_columns, row and column")
