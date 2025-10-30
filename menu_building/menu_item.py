from typing import Callable
class MenuItem:
    def __init__(self, name: str, function: Callable = None, sub_menu = None):
        self.name = name
        self.function = function
        self.sub_menu = sub_menu

    def is_function(self) -> bool:
        return self.function is not None
    def is_sub_menu(self) -> bool:
        return self.sub_menu is not None



