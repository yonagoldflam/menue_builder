from missile_launcher.consts import PrecentSuccess, MissileNames
from missile_launcher.missiles_items.missiles_items import MissilesItems


class Cruise(MissilesItems):
    def __init__(self):
        self.title: str = MissileNames.CRUISE
        self.precent = PrecentSuccess.CRUISE