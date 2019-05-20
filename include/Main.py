from managers.Manager import Manager
from models.Chainsaw import Chainsaw
from models.DriveType import DriveType
from models.Electrobogger import Electrobogger
from models.HandedSaw import HandedSaw
from models.Jigsaw import Jigsaw
from models.MaterialType import MaterialType
from models.MetalKnife import MetalKnife
from models.SpeedType import SpeedType
from models.Tools import Tools
from models.TwoHandedSaw import TwoHandedSaw

chainsaw = Chainsaw(MaterialType.PLASTIC, DriveType.MECHANICAL, 22, 5, 40, 10)
electrobogger = Electrobogger(MaterialType.METAL, DriveType.ENGINE, 18, 9, "electric", "yes")
handedSaw = HandedSaw(MaterialType.WOODEN, DriveType.MECHANICAL, 30, 4)

tools = [chainsaw, electrobogger, handedSaw]
manager = Manager(tools)

for number in manager.sort_tools_list_by_length(True):
    print("Sort by length: ", number.name(), number.length)

print(manager.find_tools_list_by_MaterialType(MaterialType.METAL))
print(manager.find_tools_list_by_DriveType(DriveType.MECHANICAL))