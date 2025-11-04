from typing import Union, List, Callable
from menu_building.menu_item import MenuItem
from consts import *
from enum import Enum

class MenuBuilder:

    def __init__(self, io, title: str, requested_exit: str = '*',requested_main:str = '#', requested_back: str = '0') -> None:
        self.io = io
        self.title = title
        self.items: List[MenuItem] = []
        self.requested_exit = requested_exit
        self.requested_main = requested_main
        self.requested_back = requested_back

    def add_sub_menu_item(self, name: str, sub_menu: 'MenuBuilder'):
        item = MenuItem(name=name, sub_menu=sub_menu)
        self.items.append(item)

    def add_function_item(self, *args, name: str, function: Callable, parms: List[str] = None):
        item = MenuItem(name=name, function=function, args=args, parms=parms)
        self.items.append(item)


    def run_menu(self, is_root: bool = True) -> Union[str, None]:
        while True:
            choice: str = self.output_menu_and_input_choice(self.items)

            if self.validation(tested=choice ,strings=(self.requested_main, self.requested_back, self.requested_exit), boolians=(choice.isdigit(), False)):
                continue

            if choice == self.requested_exit:
                return EXIT_MENU

            if choice == self.requested_back:
                if is_root:
                    self.io.output('you are already on the main menu')
                    continue
                return None

            if choice == self.requested_main:
                if is_root:
                    self.io.output('you are already on the main menu')
                    continue
                return BACK_MAIN_MENU

            index_choice: int = int(choice) - 1

            if index_choice >= len(self.items) or index_choice < 0:
                self.io.output('invalid choice!! please enter your choice again')
                continue

            item_choice: MenuItem = self.items[index_choice]
            self.execute_if_is_function(item_choice)
            result = self.run_sub_menu(item_choice, is_root)
            if result == EXIT_MENU:
                return EXIT_MENU

            if result == BACK_MAIN_MENU:
                return BACK_MAIN_MENU

    def run_sub_menu(self, item_choice: MenuItem, is_root: bool) :
        if item_choice.is_sub_menu():
            result = item_choice.sub_menu.run_menu(is_root=False)
            if result == BACK_MAIN_MENU and is_root:
                result = None
            return result
        return None

    def output_menu_and_input_choice(self, items: List[MenuItem] ) -> str:
        for number, item in enumerate(items):
            self.io.output(f'{number + 1} - {item.name}')
        self.io.output(f'{self.requested_back} - back to the previous menu')
        self.io.output(f'{self.requested_main} - return to the main menu')
        self.io.output(f'{self.requested_exit} - exiting the program')
        return self.io.input('enter your choice: ')

    def execute_if_is_function(self, item_choice: MenuItem) -> None:
        if item_choice.is_function():
            item_choice.input_arguments(self.io)
            item_choice.execute()

    def validation(self, tested = None, strings= (), boolians= ()) -> bool:
        for test in strings:
            if test == tested:
                return False
        for boolian in boolians:
            if boolian:
                return False
        self.io.output('invalid choice!! please enter your choice again')
        return True
