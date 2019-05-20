from models.Tools import Tools


class Jigsaw(Tools):
    def __init__(self, MaterialType, DriveType, length, workingMaterial, handleWidth):
        super().__init__(MaterialType, DriveType, length)
        self.workingMaterial = workingMaterial
        self.handleWidth = handleWidth

    def __str__(self):
        return (
            'This tool MaterialType = {0}, DriveType = {1}, length = {2}, workingMaterial = {3}, handleWidth = {4}').format(
            self.MaterialType,
            self.DriveType, self.length, self.workingMaterial, self.handleWidth)

    def __repr__(self):
        return self.__str__()

    def name(self):
        return "Jigsaw"
