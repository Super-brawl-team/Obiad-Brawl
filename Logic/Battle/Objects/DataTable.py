#from Logic.Battle.Objects.DataTables import DataTables  
from Logic.Battle.Objects.GlobalId import GlobalId
class DataTable:
    def __init__(self, table=None, index=None):
        """
        Initialize the DataTable. Optionally populate it with data from a table.
        :param table: A Table instance containing the rows.
        :param index: The DataType index associated with this DataTable.
        """
        self.index = index
        self.datas = []

        if table is not None:
            for i in range(0, table.get_row_count(), 2):
                row = table.get_row_at(i)
                data = DataTables.create(self.index, row, self)
                self.datas.append(data)

    @property
    def count(self):
        """
        Get the count of LogicData items in the DataTable.
        :return: Number of data items.
        """
        return len(self.datas) if self.datas else 0

    def get_datas(self):
        """
        Get all LogicData items.
        :return: List of LogicData items.
        """
        return self.datas

    def get_data_with_id(self, id_):
        """
        Get a LogicData item by its ID.
        :param id_: The global ID of the data item.
        :return: The LogicData item or None if not found.
        """
        index = GlobalId.get_instance_id(id_)
        if 0 <= index < len(self.datas):
            return self.datas[index]
        return None

    def get_data_with_id_typed(self, id_, data_type):
        """
        Get a LogicData item by its ID and cast it to a specific type.
        :param id_: The global ID of the data item.
        :param data_type: The expected type of the data item.
        :return: The LogicData item cast to the specified type or None if not found.
        """
        data = self.get_data_with_id(id_)
        return data if isinstance(data, data_type) else None

    def get_data_by_name(self, name, data_type=None):
        """
        Get a LogicData item by its name.
        :param name: The name of the data item.
        :param data_type: (Optional) The expected type of the data item.
        :return: The LogicData item or None if not found.
        """
        data = next((d for d in self.datas if d.get_name() == name), None)
        if data_type and not isinstance(data, data_type):
            return None
        return data

    def get_data_by_global_id(self, id_, data_type=None):
        """
        Get a LogicData item by its global ID and optionally check its type.
        :param id_: The global ID of the data item.
        :param data_type: (Optional) The expected type of the data item.
        :return: The LogicData item or None if not found.
        """
        index = GlobalId.get_instance_id(id_)
        if 0 <= index < len(self.datas):
            data = self.datas[index]
            return data if not data_type or isinstance(data, data_type) else None
        return None

    def get_instance_id(self, name):
        """
        Get the instance ID of a LogicData item by its name.
        :param name: The name of the data item.
        :return: The instance ID or -1 if not found.
        """
        data = next((d for d in self.datas if d.get_name() == name), None)
        return data.get_instance_id() if data else -1

    def get_index(self):
        """
        Get the index of the DataType for this DataTable.
        :return: The DataType index as an integer.
        """
        return int(self.index)
