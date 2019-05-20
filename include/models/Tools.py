from models.MaterialType import MaterialType


class Tools:
    def __init__(self, MaterialType, DriveType, length):
        self.MaterialType = MaterialType
        self.DriveType = DriveType
        self.length = length

    def __str__(self):
        return ('This tool MaterialType = {0}, DriveType = {1}, length = {2}').format(self.MaterialType,
                                                                                       self.DriveType, self.length)

    def __repr__(self):
        return self.__str__()

    def __del__(self):
        print("Destructor")
