class NoSouchPositionError(Exception): pass


class Grid:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

    def add_widget(self, widget, row, column):
        if row >= self.rows:
            raise NoSouchPositionError("Row must be less then max rows")
        if column >= self.columns:
            raise NoSouchPositionError("Column must be less then max columns")

        try:
            widget.max_rows = self.rows
            widget.max_columns = self.columns

            widget.row = row
            widget.column = column

        except AttributeError:
            raise AttributeError("Widget must have got attributes max_rows, max_columns, row and column")
