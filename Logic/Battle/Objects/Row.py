import typing
from Logic.Battle.Objects.LogicData import LogicData
from Logic.Battle.Objects.Table import Table

class Row:
    def __init__(self, table: 'Table'):
        self._table = table
        self.row_start = table.get_column_row_count()
        table.add_row(self)

    @property
    def offset(self) -> int:
        return self.row_start

    def load_data(self, data: 'LogicData'):
        for property_name in dir(data):
            property_value = getattr(data, property_name, None)

            # Check if the property is a valid one (excluding built-in)
            if isinstance(property_value, property):
                property_type = property_value.fget.__annotations__.get('return', None)
                
                if property_type is typing.List:
                    list_type = getattr(data, property_name, [])
                    self._load_generic_list(data, property_name, list_type)
                elif property_type is typing.List[bool]:
                    setattr(data, property_name, self.load_bool_array(property_name))
                elif property_type is typing.List[int]:
                    setattr(data, property_name, self.load_int_array(property_name))
                elif property_type is typing.List[str]:
                    setattr(data, property_name, self.load_string_array(property_name))
                elif isinstance(property_type, type) and issubclass(property_type, LogicData):
                    sub_data = property_type()  # Create instance of the property type
                    self.load_data(sub_data)  # Recursively load data for nested LogicData
                    setattr(data, property_name, sub_data)
                else:
                    value = self.get_value(property_name, 0)
                    if value:
                        setattr(data, property_name, self.convert_value(value, property_type))

    def _load_generic_list(self, data: 'LogicData', property_name: str, list_type: typing.List):
        # Handle the loading of generic lists (similar to C# List<T>)
        for i in range(self.offset, self.offset + self.get_array_size(property_name)):
            value = self.get_value(property_name, i - self.offset)
            if value:
                list_type.append(value)

    def get_array_size(self, name: str) -> int:
        index = self._table.get_column_index_by_name(name)
        return self._table.get_array_size_at(self, index) if index != -1 else 0

    def get_value(self, name: str, level: int = 0) -> str:
        return self._table.get_value(name, level + self.row_start)

    def load_bool_array(self, column: str) -> typing.List[bool]:
        array_size = self.get_array_size(column)
        array = []
        for i in range(array_size):
            value = self.get_value(column, i)
            if value and value.lower() in ['true', 'false']:
                array.append(value.lower() == 'true')
        return array

    def load_int_array(self, column: str) -> typing.List[int]:
        array_size = self.get_array_size(column)
        array = []
        for i in range(array_size):
            value = self.get_value(column, i)
            if value and value.isdigit():
                array.append(int(value))
        return array

    def load_string_array(self, column: str) -> typing.List[str]:
        array_size = self.get_array_size(column)
        return [self.get_value(column, i) for i in range(array_size)]

    def convert_value(self, value: str, target_type: type):
        if target_type == bool:
            return value.lower() in ['true', '1']
        elif target_type == int:
            return int(value) if value.isdigit() else 0
        elif target_type == str:
            return value
        else:
            return value  # For other types, we will return the value as is
