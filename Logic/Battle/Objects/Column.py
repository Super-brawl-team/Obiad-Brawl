class Column:
    def __init__(self):
        self._values = []

    @staticmethod
    def get_array_size(offset: int, n_offset: int) -> int:
        """Calculates the array size between two offsets."""
        return n_offset - offset

    def add(self, value: str):
        """Adds a value to the column. If the value is None, add the last value or an empty string."""
        if value is None:
            self._values.append(self._values[-1] if self._values else "")
        else:
            self._values.append(value)

    def get(self, row: int) -> str:
        """Gets the value at the specified row index."""
        return self._values[row]

    def get_size(self) -> int:
        """Returns the size of the column."""
        return len(self._values)
