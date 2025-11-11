from typing import List, Callable

from menu_builder.menu_building.menu import Menu
from menu_builder.consts import DefaultKeys
from .items.function_item import FunctionItem
from ..index_methods.numbers_index import NumberIndex
from ..index_methods.abc_index import AbcIndex


class MenuBuilder:
    def __init__(self):
        self.menus: dict[str, Menu] = {}

    def add_menu(self, io, title: str, abc_option: bool = False, requested_exit: str = DefaultKeys.EXIT_KEY,
                 requested_main: str = DefaultKeys.MAIN_KEY, requested_back: str = DefaultKeys.BACK_KEY,
                 back_main: bool = True, back: bool = True, exit_op: bool = True):
        if abc_option:
            index_type = AbcIndex
        else:
            index_type = NumberIndex

        if not back_main:
            requested_main = None

        if not back:
            requested_back = None

        if not exit_op:
            requested_exit = None

        menu = Menu(None, io, title.lower(), requested_exit, requested_main, requested_back, index_type)
        self.menus[title] = menu

    def add_sub_menu_item(self, menu_title: str, sub_menu_title: str):
        self.menus[sub_menu_title].parent = self.menus[menu_title]
        self.menus[menu_title].items.append(self.menus[sub_menu_title])

    def add_function_item(self, *args, menu_title: str, name: str, function: Callable, io=None,
                          parms: List[str] = None):
        parent = self.menus[menu_title]
        io = io or parent.io
        item = FunctionItem(parent=parent, io=io, title=name, function=function, args=args, parms=parms)
        parent.items.append(item)

    def run_menu(self, menu_title: str):
        self.menus[menu_title].run_menu()
