from typing import Union, List, Tuple
from unittest import case

from menu_building.items.function_item import FunctionItem
import consts
from consts import *

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
                case consts.CONTINUE_MENU:
                    continue

                case consts.EXIT_MENU:
                    return EXIT_MENU

                case consts.BACK_MAIN_MENU:
                    return BACK_MAIN_MENU

                case consts.BACK_MENU:
                    return BACK_MENU

                case None:
                    pass

            item_choice: Union[Menu, FunctionItem, None] = self.analysis_choice(choice)
            if not item_choice:
                index_choice = self.validate_choice_and_convert_to_int(choice, self.abc_option)
                if index_choice == CONTINUE_MENU:
                    continue

                item_choice: Union[Menu, FunctionItem] = self.items[index_choice]
            self.execute_if_is_function(item_choice)
            if isinstance(item_choice, Menu):
                result = item_choice.run_menu(is_root=False)
                match result:
                    case consts.BACK_MAIN_MENU:
                        if not is_root:
                            return BACK_MAIN_MENU

                    case consts.EXIT_MENU:
                        return EXIT_MENU

    def output_menu_and_input_choice(self, items: List[Union['Menu', FunctionItem]],abc_option ) -> str:
        if abc_option:
            for number, item in enumerate(items):
                self.io.output(f'{chr(number + 65)} - {item.title}')
            self.io.output(f'{self.requested_back} - {BACK_MENU}')
            self.io.output(f'{self.requested_main} - {BACK_MAIN_MENU}')
            self.io.output(f'{self.requested_exit} - {EXIT_MENU}')
            return self.io.input('enter your choice: ')

        for number, item in enumerate(items):
            self.io.output(f'{number + 1} - {item.title}')
        self.io.output(f'{self.requested_back} - {BACK_MENU}')
        self.io.output(f'{self.requested_main} - {BACK_MAIN_MENU}')
        self.io.output(f'{self.requested_exit} - {EXIT_MENU}')
        return self.io.input('enter your choice: ')

    def validate_default_options(self, choice: str, is_root: bool):
        if choice == self.requested_back or choice == BACK_MENU:
            if is_root:
                self.io.output('you are already on the main menu')
                return CONTINUE_MENU
            return BACK_MENU

        if choice == self.requested_main or choice == BACK_MAIN_MENU:
            if is_root:
                self.io.output('you are already on the main menu')
                return CONTINUE_MENU
            return BACK_MAIN_MENU

        if choice == self.requested_exit or choice == EXIT_MENU:
            return EXIT_MENU

    def execute_if_is_function(self, item_choice: Union['Menu', FunctionItem]) -> None:
        if isinstance(item_choice, FunctionItem):
            item_choice.input_arguments(self.io)
            item_choice.execute()

    def validate_choice_and_convert_to_int(self, choice: str, abc_option: bool):
        if abc_option:
            if len(choice) != 1:
                self.io.output('invalid choice!! please enter your choice again')
                return CONTINUE_MENU
            index_choice = ord(choice.upper()) - 65
        else:
            if not choice.isdigit():
                self.io.output('invalid choice!! please enter your choice again')
                return CONTINUE_MENU
            index_choice = int(choice) - 1

        if index_choice >= len(self.items) or index_choice < 0:
            self.io.output('invalid choice!! please enter your choice again')
            return CONTINUE_MENU
        return index_choice

    def analysis_choice(self, choice: str) -> Union[FunctionItem, 'Menu', None]:
        for item in self.items:
            if item.title == choice:
                return item
        return None


