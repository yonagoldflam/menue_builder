from missile_launcher.consts import PrecentSuccess, MissileNames
from missile_launcher.missiles_items.missiles_items import MissilesItems


class Torpedo(MissilesItems):
    def __init__(self):
        self.title: str = MissileNames.TORPEDO
        self.precent = PrecentSuccess.TORPEDO