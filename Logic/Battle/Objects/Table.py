import csv


class Column:
    def __init__(self):
        self.values = []

    def add(self, value: str):
        self.values.append(value)

    def get(self, index: int) -> str:
        return self.values[index] if index < len(self.values) else None

    def get_size(self) -> int:
        return len(self.values)

    @staticmethod
    def get_array_size(offset: int, next_offset: int) -> int:
        return next_offset - offset


class Row:
    def __init__(self, table: 'Table'):
        self.table = table
        self.offset = len(table._rows)  # offset could be the position in the rows

    def get_offset(self) -> int:
        return self.offset


class Table:
    def __init__(self, path: str):
        self._columns = []
        self._headers = []
        self._rows = []
        self._types = []

        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            columns = next(reader)  # read headers
            for column in columns:
                self._headers.append(column)
                self._columns.append(Column())

            types = next(reader)  # read types
            for type in types:
                self._types.append(type)

            for values in reader:
                if values and values[0]:  # ensure there's data in the first column
                    self.add_row(Row(self))

                for i in range(len(self._headers)):
                    if i < len(values):
                        self._columns[i].add(values[i])

    def add_row(self, row: Row):
        self._rows.append(row)

    def get_array_size_at(self, row: Row, column_index: int) -> int:
        index = self._rows.index(row) + 1
        if index == -1 or column_index >= len(self._columns):
            return 0

        if index + 1 >= len(self._rows):
            next_offset = self._columns[column_index].get_size()
        else:
            next_row = self._rows[index + 1]
            next_offset = next_row.get_offset()

        return Column.get_array_size(row.get_offset(), next_offset)

    def get_column_index_by_name(self, name: str) -> int:
        return self._headers.index(name) if name in self._headers else -1

    def get_column_name(self, index: int) -> str:
        return self._headers[index] if 0 <= index < len(self._headers) else None

    def get_column_row_count(self) -> int:
        return len(self._columns[0].values) if self._columns else 0

    def get_row_at(self, index: int) -> Row:
        return self._rows[index] if 0 <= index < len(self._rows) else None

    def get_row_count(self) -> int:
        return len(self._rows)

    def get_value(self, name: str, level: int) -> str:
        index = self.get_column_index_by_name(name)
        return self.get_value_at(index, level) if index != -1 else None

    def get_value_at(self, column: int, row: int) -> str:
        if 0 <= column < len(self._columns) and 0 <= row < len(self._rows):
            return self._columns[column].get(row)
        return None

