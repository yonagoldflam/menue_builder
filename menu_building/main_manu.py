from typing import List, Callable

from menu_building.menu_item import MenuItem

class MainMenu:
    def __init__(self, title: str):
        self.title = title
        self.items: List[MenuItem] = []

    def add_item(self, name: str, sub_menu: 'MainMenu' = None, function: Callable = None):
        item = MenuItem(name, sub_menu=sub_menu, function=function)
        self.items.append(item)


# class Manager:
#     def __init__(self):
#         self.items: List[MenuItem] = []
#
#     def add_item(self, name: str, sub_menu: MainMenu = None, function: Callable = None):
#         self.items.append(MenuItem(name, sub_menu, function))