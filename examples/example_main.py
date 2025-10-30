from menu_building.menu_builder import MenuBuilder
from io_selection.console_io import ConsoleIo
from menu_building.main_manu import MainMenu
from menu_building.menu_item import MenuItem

def print_hello():
    print('hello')


def print_world():
    print('world')


def print_home():
    print('home')


def print_name():
    name = input('enter your name: ')
    print(name)


# menu = {'print': {'hello': {'world': print_world, 'home': print_home}, 'world': print_world}, 'print name': print_name}
hello = MainMenu('hello')
hello.add_item(MenuItem('home', function=print_home))
hello.add_item(MenuItem('world', function=print_world))

printt = MainMenu('print')
printt.add_item(MenuItem('hello', sub_menu= hello))
printt.add_item(MenuItem('world', function=print_world))

main_menu = MainMenu('main menu')
main_menu.add_item(MenuItem('print', sub_menu=printt))
main_menu.add_item(MenuItem('print name', function=print_name))

io = ConsoleIo()
t = MenuBuilder(io)
a = t.build_menu(main_menu)
