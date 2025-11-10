from typing import Union, List, Dict
from ..index_methods.index_method import IndexMethod
from menu_builder.consts import MenuIcons
from menu_builder.menu_building.items.menu_item import MenuItem, Back, Home, Exit


class Menu(MenuItem):

    def __init__(self, parent, io, title: str, requested_exit: str, requested_main:str, requested_back: str, index_type: IndexMethod) -> None:
        self.parent = parent
        self.io = io
        self.title = title
        self.items: List[MenuItem] = []
        self.requested_exit = requested_exit
        self.requested_main = requested_main
        self.requested_back = requested_back
        self.index_type = index_type

    def run_menu(self) -> Union[str, None]:

        choice: MenuItem = self.output_menu_and_input_choice()
        choice.select()

    def output_menu_and_input_choice(self) -> MenuItem:

        indexes: Dict[str, MenuItem] = self.index_type.index_items(self.items)
        while True:
            for index, item in indexes.items():
                if len(index) == 1:
                    self.io.output(f'{index} - {item.title}')

            self.out_put_menu_icon_options()
            choice: str = self.io.input('enter your choice: ')

            if choice.lower() in indexes:
                return indexes[choice.lower()]

            if choice == self.requested_back:
                return Back(self)

            if choice == self.requested_main:
                return Home(self)

            if choice == self.requested_exit:
                return Exit(self)

            self.io.output('invalid choice!! please enter your choice again')

    def out_put_menu_icon_options(self):
        self.io.output(f'{self.requested_back} - {MenuIcons.BACK}')
        self.io.output(f'{self.requested_main} - {MenuIcons.BACK_MAIN}')
        self.io.output(f'{self.requested_exit} - {MenuIcons.EXIT}')

    def select(self):

        self.run_menu()





