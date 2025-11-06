from typing import Union, List, Dict

from menu_builder.menu_building.items.function_item import FunctionItem
from ..index_methods.index_method import IndexMethod
from menu_builder.consts import MenuIcons


class Menu:

    def __init__(self, io, title: str, requested_exit: str, requested_main:str, requested_back: str, index_type: IndexMethod) -> None:
        self.io = io
        self.title = title
        self.items: List[Union[FunctionItem, Menu]] = []
        self.requested_exit = requested_exit
        self.requested_main = requested_main
        self.requested_back = requested_back
        self.index_type = index_type


    def run_menu(self, is_root: bool = True) -> Union[str, None]:
        while True:
            choice: Union[Menu, FunctionItem, str] = self.output_menu_and_input_choice()
            if isinstance(choice, str):
                result = self.validate_default_options(choice, is_root)
                match result:
                    case MenuIcons.CONTINUE:
                        continue

                    case MenuIcons.EXIT:
                        return MenuIcons.EXIT

                    case MenuIcons.BACK_MAIN:
                        return MenuIcons.BACK_MAIN

                    case MenuIcons.BACK:
                        return MenuIcons.BACK

            self.execute_if_is_function(choice)
            if isinstance(choice, Menu):
                result = choice.run_menu(is_root=False)
                match result:
                    case MenuIcons.BACK_MAIN:
                        if not is_root:
                            return MenuIcons.BACK_MAIN

                    case MenuIcons.EXIT:
                        return MenuIcons.EXIT

    def output_menu_and_input_choice(self) -> Union['Menu', FunctionItem, str]:
        indexes: Dict[str, Union[Menu, FunctionItem]] = self.index_type.index_items(self.items)
        for index, item in indexes.items():
            if len(index) == 1:
                self.io.output(f'{index} - {item.title}')

        self.out_put_menu_icon_options()
        choice: str = self.io.input('enter your choice: ')

        if choice.lower() in indexes:
            return indexes[choice.lower()]

        return choice

    def out_put_menu_icon_options(self):
        self.io.output(f'{self.requested_back} - {MenuIcons.BACK}')
        self.io.output(f'{self.requested_main} - {MenuIcons.BACK_MAIN}')
        self.io.output(f'{self.requested_exit} - {MenuIcons.EXIT}')

    def validate_default_options(self, choice: str, is_root: bool) -> Union[MenuIcons.CONTINUE, MenuIcons.BACK_MAIN, MenuIcons.EXIT]:

        if choice == self.requested_back or choice == MenuIcons.BACK:
            if is_root:
                self.io.output('you are already on the main menu')
                return MenuIcons.CONTINUE
            return MenuIcons.BACK

        if choice == self.requested_main or choice == MenuIcons.BACK_MAIN:
            if is_root:
                self.io.output('you are already on the main menu')
                return MenuIcons.CONTINUE
            return MenuIcons.BACK_MAIN

        if choice == self.requested_exit or choice == MenuIcons.EXIT:
            return MenuIcons.EXIT

        self.io.output('invalid choice!! please enter your choice again')
        return MenuIcons.CONTINUE

    def execute_if_is_function(self, item_choice: Union['Menu', FunctionItem]) -> None:
        if isinstance(item_choice, FunctionItem):
            item_choice.input_arguments(self.io)
            item_choice.execute()



