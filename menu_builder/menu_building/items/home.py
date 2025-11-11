from menu_builder.menu_building.items.menu_item import MenuItem
from menu_builder.consts import MenuIcons


class Home(MenuItem):

    def __init__(self, parent: MenuItem):
        self.title = MenuIcons.BACK_MAIN
        self.parent = parent

    def select(self):
        current_parent = self.parent
        while current_parent.parent:
            current_parent = current_parent.parent
        current_parent.run_menu()
