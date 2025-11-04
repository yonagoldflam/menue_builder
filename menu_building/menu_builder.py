from typing import List, Callable

from menu_building.menu import Menu
from menu_building.items.function_item import FunctionItem

class MenuBuilder:
    def __init__(self):
        self.menus: dict[str, Menu] = {}

    def add_menu(self, io, title: str, requested_exit: str = '*',requested_main:str = '#', requested_back: str = '0'):
        menu = Menu(io, title, requested_exit, requested_main, requested_back)
        self.menus[title] = menu

    def add_sub_menu_item(self, menu_title: str, sub_menu_title: str):
        self.menus[menu_title].items.append(self.menus[sub_menu_title])

    def add_function_item(self, *args, menu_title: str, name: str, function: Callable, parms: List[str] = None):
        item = FunctionItem(title=name, function=function, args=args, parms=parms)
        self.menus[menu_title].items.append(item)
    def run_menu(self, menu_title: str):
        self.menus[menu_title].run_menu()