from models.Tools import Tools


class Chainsaw(Tools):
    def __init__(self, MaterialType, DriveType, length, engineCapacity, chainSpeed, tankVolume):
        super().__init__(MaterialType, DriveType, length)
        self.engineCapacity = engineCapacity
        self.chainSpeed = chainSpeed
        self.tankVolume = tankVolume

    def __str__(self):
        return (
            'This tool MaterialType = {0}, DriveType = {1}, length = {2}, engineCapacity = {3}, chainSpeed = {4}, tankVolume = {5}').format(
            self.MaterialType,
            self.DriveType, self.length, self.engineCapacity, self.chainSpeed, self.tankVolume)

    def __repr__(self):
        return self.__str__()

    def name(self):
        return "Chainsaw"
