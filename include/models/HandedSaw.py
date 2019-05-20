from models.Tools import Tools


class HandedSaw(Tools):
    def __init__(self, MaterialType, DriveType, length, prongsPerInch):
        super().__init__(MaterialType, DriveType, length)
        self.prongsPerInch = prongsPerInch

    def __str__(self):
        return ('This tool MaterialType = {0}, DriveType = {1}, length = {2}, prongsPerInch = {3}').format(
            self.MaterialType,
            self.DriveType, self.length, self.prongsPerInch)

    def __repr__(self):
        return self.__str__()

    def name(self):
        return "HandedSaw"
