from models.Tools import Tools


class Electrobogger(Tools):
    def __init__(self, MaterialType, DriveType, length, maximumSpeed, typeOfSupply, backlighting):
        super().__init__(MaterialType, DriveType, length)
        self.maximumSpeed = maximumSpeed
        self.typeOfSupply = typeOfSupply
        self.backlighting = backlighting

    def __str__(self):
        return (
            'This tool MaterialType = {0}, DriveType = {1}, length = {2}, maximumSpeed = {3}, typeOfSupply = {4}, backlighting{5}').format(
            self.MaterialType,
            self.DriveType, self.length, self.maximumSpeed, self.typeOfSupply, self.backlighting)

    def __repr__(self):
        return self.__str__()

    def name(self):
        return "Electrobogger"
