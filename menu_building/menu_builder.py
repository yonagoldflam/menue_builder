from typing import List, Callable

from menu_building.menu import Menu
from menu_building.items.function_item import FunctionItem
from consts import *

class MenuBuilder:
    def __init__(self):
        self.menus: dict[str, Menu] = {}

    def add_menu(self, io, title: str, abc_option: bool = False, requested_exit: str = DEFAULT_EXIT_KEY, requested_main:str = DEFAULT_MAIN_KEY, requested_back: str = DEFAULT_BACK_KEY):
        menu = Menu(io, title, abc_option, requested_exit, requested_main, requested_back)
        self.menus[title] = menu

    def add_sub_menu_item(self, menu_title: str, sub_menu_title: str):
        self.menus[menu_title].items.append(self.menus[sub_menu_title])

    def add_function_item(self, *args, menu_title: str, name: str, function: Callable, parms: List[str] = None):
        item = FunctionItem(title=name, function=function, args=args, parms=parms)
        self.menus[menu_title].items.append(item)
    def run_menu(self, menu_title: str):
        self.menus[menu_title].run_menu()