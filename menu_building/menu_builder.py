from typing import Callable, TypeAlias, Union, List
from menu_building.main_manu import MainMenu
from menu_building.menu_item import MenuItem


class MenuBuilder:

    def __init__(self, io) -> None:
        self.io = io

    def build_menu(self, menu: MainMenu, requested_exit: str = '*',requested_main:str = '#', requested_back: str = '0', is_root: bool = True) -> Union[str, None]:
        while True:
            for number, item in enumerate(menu.items):
                self.io.output(f'{number + 1} - {item.name}')
            choose: str = self.io.input('enter your choice: ')
            if choose != requested_main and choose != requested_back and choose != requested_exit and not choose.isdigit():
                self.io.output('invalid choice!! please enter your choice again')
                continue
            if choose == requested_exit:
                return 'exit'
            if choose == requested_back:
                if is_root:
                    self.io.output('you are already on the main menu')
                    continue
                else:
                    return ''
            if choose == requested_main:
                if is_root:
                    self.io.output('you are already on the main menu')
                    continue
                return 'main'
            index_choose: int = int(choose) - 1
            items: List[MenuItem] = menu.items
            if index_choose >= len(items):
                self.io.output('invalid choice!! please enter your choice again')
                continue
            choose_option: MenuItem = items[index_choose]
            if choose_option.is_function():
                choose_option.function()
            elif choose_option.is_sub_menu():
                result = self.build_menu(choose_option.sub_menu, requested_exit, requested_main, requested_back, is_root = False)
                if result == 'exit':
                    return 'exit'
                if result == 'main':
                    if not is_root:
                        return 'main'