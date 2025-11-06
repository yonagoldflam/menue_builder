from menu_builder.io_selection.menu_io import MenuIo

class ConsoleIo(MenuIo):

    def output(self, message: str) -> None:
        print(message)

    def input(self, user_guide: str) -> str:
        return input(user_guide)
