from typing import Callable
class MenuItem:
    def __init__(self, name: str, function: Callable = None, sub_menu = None, args: tuple = None):
        self.name = name
        self.function = function
        self.sub_menu = sub_menu
        self.args = args

    def is_function(self) -> bool:
        return self.function is not None
    def is_sub_menu(self) -> bool:
        return self.sub_menu is not None

    def execute(self) -> None:
        if self.is_function():
            self.function(*self.args)



