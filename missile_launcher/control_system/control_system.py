from typing import Union

from missile_launcher.missile_battery.missile_battery import MissileBattery
from missile_launcher.missiles_items.ballistic import Ballistic
from missile_launcher.missiles_items.cruise import Cruise
from missile_launcher.missiles_items.missiles_items import MissilesItems
from missile_launcher.consts import MissileNames
from menu_builder.io_selection.console_io import ConsoleIo
from menu_builder.menu_building.menu_builder import MenuBuilder
from missile_launcher.missiles_items.torpedo import Torpedo


class ControlSystem:
    def __init__(self):
        self.missile_battery: MissileBattery = MissileBattery()
        self.io = ConsoleIo()
        self.menu_builder = MenuBuilder()
        self.menu_builder.add_menu(io= self.io, title= 'missile launcher')
        self.menu_builder.add_function_item(menu_title='missile launcher', name='launch', function=self.launch, parms=['missile_name', 'num'])
        self.menu_builder.add_function_item(menu_title='missile launcher', name='insert missiles', function=self.insert_missiles, parms=['missile_name', 'num'])
        self.menu_builder.add_function_item(menu_title='missile launcher', name='inventory report', function=self.inventory_report)


    def run_missile_menu(self):
        self.menu_builder.run_menu('missile launcher')

    def launch(self, missile_name: str, num: str):
        success_counter: int = 0
        for _ in range(int(num)):
            missile = self.get_missile_if_exist(missile_name)
            if missile:
                success = self.missile_battery.missile_launch(missile)
                if success:
                    success_counter += 1
        self.io.output(f'Launching {success_counter} missiles.')

    def insert_missiles(self, missile_name: str, num: str):
        missile = self.validate_input(missile_name)
        if missile:
            for _ in range(int(num)):
                self.missile_battery.add_missile(missile)

    def inventory_report(self):
        self.io.output(f'total of missiles: {len(self.missile_battery.missiles)}')
        self.io.output('the missiles in the order in which they are located:')
        for missile in self.missile_battery.missiles:
            self.io.output(missile.title)

    def get_missile_if_exist(self, missile_name: str):
        for missile in self.missile_battery.missiles:
            if missile.title == missile_name.lower():
                return missile
        return None

    def validate_input(self, user_input: str) -> Union[MissilesItems, None]:
        match user_input:
            case MissileNames.TORPEDO:
                return Torpedo()

            case MissileNames.BALLISTIC:
                return Ballistic()

            case MissileNames.CRUISE:
                return Cruise()
        self.io.output(f'Invalid input!!!!!!!!!!!')
        return None


if __name__ == '__main__':
    cont_system = ControlSystem()
    cont_system.run_missile_menu()
