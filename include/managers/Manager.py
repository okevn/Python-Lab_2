class Manager:
    def __init__(self, tools_list):
        self.tools_list = tools_list

    def sort_tools_list_by_length(self, reverse):
        return sorted(self.tools_list, key=lambda tools: tools.length, reverse=reverse)

    def find_tools_list_by_MaterialType(self, MaterialType):
        return list(filter(lambda tools: tools.MaterialType == MaterialType, self.tools_list))

    def find_tools_list_by_DriveType(self, DriveType):
        return list(filter(lambda tools: tools.DriveType == DriveType, self.tools_list))
