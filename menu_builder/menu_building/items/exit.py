from menu_builder.consts import MenuIcons
from menu_builder.menu_building.items.menu_item import MenuItem


class Exit(MenuItem):
    def __init__(self, parent: MenuItem):
        self.parent = parent
        self.title = MenuIcons.EXIT

    def select(self):
        pass
