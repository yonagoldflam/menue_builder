from typing import List, Callable

from menu_building.menu_item import MenuItem

class MainMenu:
    def __init__(self, title: str):
        self.title = title
        self.items: List[MenuItem] = []

    def add_sub_menu_item(self, name: str, sub_menu: 'MainMenu'):
        item = MenuItem(name = name, sub_menu=sub_menu)
        self.items.append(item)

    def add_function_item(self, *args, name: str, function: Callable):
        item = MenuItem(name = name, function=function, args = args)
        self.items.append(item)
