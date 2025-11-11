import random
from typing import Dict, List
from missile_launcher.missiles_items.missiles_items import MissilesItems
from missile_launcher.consts import MissileNames, PrecentSuccess


class MissileBattery:
    def __init__(self):
        self.missiles: List[MissilesItems] = []

    def add_missile(self, missile: MissilesItems) -> None:
        self.missiles.insert(0, missile)


    def missile_launch(self, missile: MissilesItems) -> bool:
        if missile not in self.missiles:
            return False

        success = self.calculate_success(missile)
        self.missiles.remove(missile)
        if not success:
            return False
        return True

    def calculate_success(self, missile: MissilesItems) -> bool:
        ran = random.random()
        percent = missile.precent / 100

        if percent > ran:
            return True
        return False
