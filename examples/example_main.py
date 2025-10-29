from menu_builder.menu_builder import MenuBuilder
from io_selection.console_io import ConsoleIo

def print_hello():
    print('hello')


def prnt_world():
    print('world')


def print_home():
    print('home')


def print_name():
    name = input('enter your name: ')
    print(name)


menu = {'print': {'hello': {'world': prnt_world, 'home': print_home}, 'world': prnt_world}, 'print name': print_name}
io = ConsoleIo()
t = MenuBuilder(io)
a = t.build_menu(menu)
