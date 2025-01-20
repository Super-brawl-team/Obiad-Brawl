from Logic.Battle.Objects.DataTables import DataTables 
from Logic.Battle.Objects.DataTable import DataTable
from Logic.Battle.Objects.DataType import DataType
class Gamefiles:
    def __init__(self):
        # Initialize the dictionary to hold DataTable instances
        self._data_tables = {}

        # Check if there are any game files to initialize
        if len(DataTables.Gamefiles) > 0:
            for data_type in DataTables.Gamefiles.keys():
                self._data_tables[int(data_type.value)] = DataTable()

    def dispose(self):
        """
        Clears the internal data tables dictionary.
        """
        self._data_tables.clear()

    def get(self, index):
        """
        Retrieves a DataTable by its DataType or integer index.
        """
        if isinstance(index, DataType):
            index = int(index.value)
        return self._data_tables.get(index, None)

    def contains_table(self, t):
        """
        Checks if a DataTable exists for the given integer index.
        """
        return t in self._data_tables

    def initialize(self, table, index):
        """
        Initializes a DataTable with the given Table and DataType index.
        """
        self._data_tables[int(index.value)] = DataTable(table, index)

