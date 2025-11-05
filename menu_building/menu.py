from typing import Union, List

from menu_building.items.function_item import FunctionItem
from consts import MenuIcons

class Menu:

    def __init__(self, io, title: str, abc_option: bool, requested_exit: str, requested_main:str, requested_back: str) -> None:
        self.io = io
        self.title = title
        self.items: List[Union[FunctionItem, Menu]] = []
        self.requested_exit = requested_exit
        self.requested_main = requested_main
        self.requested_back = requested_back
        self.abc_option = abc_option

    def run_menu(self, is_root: bool = True) -> Union[str, None]:
        while True:
            choice: str = self.output_menu_and_input_choice(self.items, self.abc_option)

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

                case None:
                    pass

            item_choice: Union[Menu, FunctionItem, MenuIcons.CONTINUE] = self.analysis_choice_and_select_item(choice, self.abc_option)
            if item_choice == MenuIcons.CONTINUE:
                continue
            self.execute_if_is_function(item_choice)
            if isinstance(item_choice, Menu):
                result = item_choice.run_menu(is_root=False)
                match result:
                    case MenuIcons.BACK_MAIN:
                        if not is_root:
                            return MenuIcons.BACK_MAIN

                    case MenuIcons.EXIT:
                        return MenuIcons.EXIT

    def output_menu_and_input_choice(self, items: List[Union['Menu', FunctionItem]],abc_option ) -> str:
        if abc_option:
            for number, item in enumerate(items):
                self.io.output(f'{chr(number + 65)} - {item.title}')
            self.io.output(f'{self.requested_back} - {MenuIcons.BACK}')
            self.io.output(f'{self.requested_main} - {MenuIcons.BACK_MAIN}')
            self.io.output(f'{self.requested_exit} - {MenuIcons.EXIT}')
            return self.io.input('enter your choice: ')

        for number, item in enumerate(items):
            self.io.output(f'{number + 1} - {item.title}')
        self.io.output(f'{self.requested_back} - {MenuIcons.BACK}')
        self.io.output(f'{self.requested_main} - {MenuIcons.BACK_MAIN}')
        self.io.output(f'{self.requested_exit} - {MenuIcons.EXIT}')
        return self.io.input('enter your choice: ')

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

    def execute_if_is_function(self, item_choice: Union['Menu', FunctionItem]) -> None:
        if isinstance(item_choice, FunctionItem):
            item_choice.input_arguments(self.io)
            item_choice.execute()

    def analysis_choice_and_select_item(self, choice: str, abc_option) -> Union[FunctionItem, 'Menu', MenuIcons.CONTINUE]:
        for item in self.items:
            if item.title.lower() == choice.lower():
                return item
        index_choice = self.validate_choice_and_convert_to_int(choice, abc_option)
        if index_choice == MenuIcons.CONTINUE:
            return MenuIcons.CONTINUE
        return self.items[index_choice]

    def validate_choice_and_convert_to_int(self, choice: str, abc_option: bool):
        if abc_option:
            if len(choice) != 1:
                self.io.output('invalid choice!! please enter your choice again')
                return MenuIcons.CONTINUE
            index_choice = ord(choice.upper()) - 65
        else:
            if not choice.isdigit():
                self.io.output('invalid choice!! please enter your choice again')
                return MenuIcons.CONTINUE
            index_choice = int(choice) - 1

        if index_choice >= len(self.items) or index_choice < 0:
            self.io.output('invalid choice!! please enter your choice again')
            return MenuIcons.CONTINUE
        return index_choice



