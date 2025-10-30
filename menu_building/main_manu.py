from typing import List

from menu_building.menu_item import MenuItem

class MainMenu:
    def __init__(self, title: str):
        self.title = title
        self.items: List[MenuItem] = []

    def add_item(self, item: MenuItem):
        self.items.append(item)