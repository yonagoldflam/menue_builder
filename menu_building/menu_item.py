from typing import Callable, List
class MenuItem:
    def __init__(self, name: str, function: Callable = None, sub_menu = None, args: tuple = None, parms: List = None):
        self.name = name
        self.function = function
        self.sub_menu = sub_menu
        self.args = args
        self.parms: List[str] = parms
        self.parms_args: dict = {}

    def is_function(self) -> bool:
        return self.function is not None
    def is_sub_menu(self) -> bool:
        return self.sub_menu is not None

    def input_arguments(self, io):
        if self.parms:
            for parm in self.parms:
                arg = io.input(f'enter argument for {parm}: ')
                self.parms_args[parm] = arg

    def execute(self) -> None:
        if self.is_function():
            self.function(*self.args, **self.parms_args)
            self.parms_args.clear()



