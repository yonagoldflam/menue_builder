from menu_builder.menu_building.items.menu_item import MenuItem
from menu_builder.consts import MenuIcons


class Back(MenuItem):

    def __init__(self, parent: MenuItem):
        self.title = MenuIcons.BACK
        self.parent = parent

    def select(self):
        if self.parent.parent:
            self.parent.parent.run_menu()

        else:
            self.parent.io.output('you are already on the main menu')
            self.parent.run_menu()
