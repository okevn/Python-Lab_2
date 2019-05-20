from models.Tools import Tools


class TwoHandedSaw(Tools):
    def __init__(self, MaterialType, DriveType, length, model, price):
        super().__init__(MaterialType, DriveType, length)
        self.model = model
        self.price = price

    def __str__(self):
        return ('This tool MaterialType = {0}, DriveType = {1}, length = {2}, model = {3}, price = {4}').format(
            self.MaterialType,
            self.DriveType, self.length, self.model, self.price)

    def __repr__(self):
        return self.__str__()

    def name(self):
        return "TwoHandedSaw"
