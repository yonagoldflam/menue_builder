from typing import List, Callable

from menu_building.menu import Menu
from menu_building.menu_item import MenuItem

class MenuBuilder:
    def __init__(self):
        self.menus: List[Menu] = []

    def add_menu(self, io, title: str, requested_exit: str = '*',requested_main:str = '#', requested_back: str = '0'):
        menu = Menu(io, title, requested_exit, requested_main, requested_back)
        self.menus.append(menu)

    def add_sub_menu_item(self, menu_title: str, sub_menu_title: str):
        for menu in self.menus:
            if menu.title == menu_title:
                for sub_menu in self.menus:
                    if sub_menu.title == sub_menu_title:
                        item = MenuItem(name=sub_menu_title, sub_menu=sub_menu)
                        menu.items.append(item)

    def add_function_item(self, *args, menu_title: str, name: str, function: Callable, parms: List[str] = None):
        item = MenuItem(name=name, function=function, args=args, parms=parms)
        for menu in self.menus:
            if menu.title == menu_title:
                menu.items.append(item)

    def run_menu(self, menu_title: str):
        for menu in self.menus:
            if menu.title == menu_title:
                menu.run_menu()