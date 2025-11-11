from typing import List, Dict
from ..index_methods.index_method import IndexMethod
from menu_builder.consts import MenuIcons
from menu_builder.menu_building.items.menu_item import MenuItem


class Menu(MenuItem):

    def __init__(self, parent, io, title, requested_exit, requested_main, requested_back,
                 index_type: IndexMethod) -> None:
        self.parent = parent
        self.io = io
        self.title = title
        self.items: List[MenuItem] = []
        self.back_keys: Dict[str, str] = self.build_back_keys(requested_exit, requested_main, requested_back)
        self.index_type = index_type

    def build_back_keys(self, requested_exit: str, requested_main: str, requested_back: str) -> Dict[str, str]:
        back_keys: Dict[str, str] = {}
        if requested_main:
            back_keys[MenuIcons.BACK_MAIN] = requested_main

        if requested_back:
            back_keys[MenuIcons.BACK] = requested_back

        if requested_exit:
            back_keys[MenuIcons.EXIT] = requested_exit

        return back_keys

    def run_menu(self) -> None:
        item_choice: MenuItem = self.output_menu_and_input_choice()
        item_choice.select()

    def output_menu_and_input_choice(self) -> MenuItem:
        indexes: Dict[str, MenuItem] = self.index_type.index_items(self.items, self.back_keys, self)
        while True:
            for index, item in indexes.items():
                if not index == item.title:
                    self.io.output(f'{index} - {item.title}')

            choice: str = self.io.input('enter your choice: ')

            if choice.lower() in indexes:
                return indexes[choice.lower()]

            self.io.output('invalid choice!! please enter your choice again')

    def select(self):
        self.run_menu()
