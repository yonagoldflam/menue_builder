from typing import Callable, TypeAlias, Union


Menu: TypeAlias = dict[str, Union[Callable[[], None], dict]]


class MenuBuilder:

    def __init__(self, io) -> None:
        self.io = io

    def build_menu(self, menu: Menu, requested_exit: str = '*',requested_main:str = '#', requested_back: str = '0', is_root: bool = True) -> Union[str, None]:
        while True:
            options: list[str] = []
            for number, key in enumerate(menu):
                options.append(key)
                self.io.output(f'{number + 1} - {key}')
            choose: str = self.io.input('enter your choice: ')
            if choose != requested_main and choose != requested_back and choose != requested_exit and not choose.isdigit():
                self.io.output('invalid choice!! please enter your choice again')
                continue
            if choose == requested_exit:
                return 'exit'
            if choose == requested_back:
                if is_root:
                    self.io.output('you are already on the main menu')
                    continue
                else:
                    return ''
            if choose == requested_main:
                if is_root:
                    self.io.output('you are already on the main menu')
                    continue
                return 'main'
            index_choose: int = int(choose) - 1
            if index_choose >= len(options):
                self.io.output('invalid choice!! please enter your choice again')
                continue
            choose_option: str = options[index_choose]
            selected_menu: Union[Callable[[], None], dict] = menu[choose_option]
            if callable(selected_menu):
                selected_menu()
            if type(selected_menu) is dict:
                result = self.build_menu(selected_menu, requested_exit, requested_main, requested_back, is_root=False)
                if result == 'exit':
                    return 'exit'
                if result == 'main':
                    if not is_root:
                        return 'main'