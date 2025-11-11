from typing import Callable, List
from menu_builder.menu_building.items.menu_item import MenuItem


class FunctionItem(MenuItem):

    def __init__(self, parent: MenuItem, io, title: str, function: Callable = None, args: tuple = None,
                 parms: List = None):
        self.parent = parent
        self.io = io
        self.title = title
        self.function = function
        self.args = args
        self.parms: List[str] = parms
        self.parms_args: dict = {}

    def input_arguments(self) -> None:
        if self.parms:
            for parm in self.parms:
                arg = self.io.input(f'enter argument for {parm}: ')
                self.parms_args[parm] = arg

    def execute(self) -> None:
        self.function(*self.args, **self.parms_args)
        self.parms_args.clear()

    def select(self):
        self.input_arguments()
        self.execute()
        self.parent.run_menu()
