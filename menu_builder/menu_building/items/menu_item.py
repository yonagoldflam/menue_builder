from abc import ABC, abstractmethod


class MenuItem(ABC):
    parent: 'MenuItem'
    @abstractmethod
    def select(self):
        pass

from typing import Callable, List

class FunctionItem(MenuItem):
    def __init__(self,parent: MenuItem, io, title: str, function: Callable = None, args: tuple = None, parms: List = None):
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

class Back(MenuItem):

    def __init__(self, parent: MenuItem):

        self.parent = parent

    def select(self):
        if self.parent.parent:
            self.parent.parent.run_menu()

        else:
            self.parent.io.output('you are already on the main menu')
            self.parent.run_menu()


class Home(MenuItem):

    def __init__(self, parent: MenuItem):
        self.parent = parent

    def select(self):
        current_parent = self.parent
        while current_parent.parent:

            current_parent = current_parent.parent
        current_parent.run_menu()

class Exit(MenuItem):
    def __init__(self, parent: MenuItem):
        self.parent = parent

    def select(self):
        pass


