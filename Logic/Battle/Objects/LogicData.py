from Logic.Battle.Objects.GlobalId import GlobalId
from Logic.Battle.Objects.DataTables import DataTables
class LogicData:
    def __init__(self, row, data_table):
        """
        Initializes a LogicData instance.
        :param row: The row associated with this logic data.
        :param data_table: The data table this logic data belongs to.
        """
        self._data_type = None
        self._id = None
        self.data_table = data_table
        self.row = row

    def load_data(self, data, data_type=None):
        """
        Loads data into the current LogicData object.
        :param data: The LogicData to load into this instance.
        :param data_type: Optional data type; defaults to the current type if not provided.
        """
        self._data_type = data_type if data_type is not None else DataTables.types[type(self)]
        self._id = GlobalId.create_global_id(self._data_type, len(self.data_table.datas))
        self.row = data.row
        self.row.load_data(data)

    def get_data_type(self):
        """
        Returns the data type of this LogicData instance.
        :return: The data type as an integer.
        """
        return self._data_type

    def get_global_id(self):
        """
        Returns the global ID for this LogicData instance.
        :return: The global ID.
        """
        return self._id

    def get_instance_id(self):
        """
        Returns the instance ID for this LogicData instance.
        :return: The instance ID.
        """
        return GlobalId.get_instance_id(self._id)

    def get_class_id(self):
        """
        Returns the class ID for this LogicData instance.
        :return: The class ID.
        """
        return GlobalId.get_class_id(self._id)

    def get_name(self):
        """
        Returns the name of the row associated with this LogicData.
        :return: The name of the row as a string.
        """
        return self.row.get_name()
