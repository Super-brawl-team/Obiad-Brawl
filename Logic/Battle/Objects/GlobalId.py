class GlobalId:
    @staticmethod
    def create_global_id(class_id: int, instance_id: int) -> int:
        """
        Create a global ID using the class ID and instance ID.
        :param class_id: The class ID.
        :param instance_id: The instance ID.
        :return: The generated global ID.
        """
        return 1000000 + instance_id if class_id <= 0 else class_id * 1000000 + instance_id

    @staticmethod
    def get_class_id(global_id: int) -> int:
        """
        Extract the class ID from a global ID.
        :param global_id: The global ID.
        :return: The class ID.
        """
        return global_id // 1000000

    @staticmethod
    def get_instance_id(global_id: int) -> int:
        """
        Extract the instance ID from a global ID.
        :param global_id: The global ID.
        :return: The instance ID.
        """
        return global_id % 1000000
