from models.Tools import Tools


class MetalKnife(Tools):
    def __init__(self, MaterialType, DriveType, length, guarantee, weight):
        super().__init__(MaterialType, DriveType, length)
        self.guarantee = guarantee
        self.weight = weight

    def __str__(self):
        return ('This tool MaterialType = {0}, DriveType = {1}, length = {2}, guarantee = {3}, weight = {4}').format(
            self.MaterialType,
            self.DriveType, self.length, self.guarantee, self.weight)

    def __repr__(self):
        return self.__str__()

    def name(self):
        return "MetalKnife"
