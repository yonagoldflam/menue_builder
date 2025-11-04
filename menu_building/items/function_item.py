from typing import Callable, List

class FunctionItem:
    def __init__(self, title: str, function: Callable = None, args: tuple = None, parms: List = None):
        self.title = title
        self.function = function
        self.args = args
        self.parms: List[str] = parms
        self.parms_args: dict = {}

    def input_arguments(self, io) -> None:
        if self.parms:
            for parm in self.parms:
                arg = io.input(f'enter argument for {parm}: ')
                self.parms_args[parm] = arg

    def execute(self) -> None:
        self.function(*self.args, **self.parms_args)
        self.parms_args.clear()



