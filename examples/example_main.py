from menu_building.menu_builder import MenuBuilder
from io_selection.console_io import ConsoleIo




def print_hello():
    print('hello')


def print_world():
    print('world')


def print_home():
    print('home')


def print_name(*names):
    # name = input('enter your name: ')
    for name in names:
        print(name)


# menu = {'print': {'hello': {'world': print_world, 'home': print_home}, 'world': print_world}, 'print name': print_name}

io = ConsoleIo()

hello = MenuBuilder(io=io, title= 'hello')
hello.add_function_item(name = 'home', function=print_home)
hello.add_function_item(name = 'world', function=print_world)

printt = MenuBuilder(io=io, title='print')
printt.add_sub_menu_item('hello', sub_menu= hello)
printt.add_function_item(name = 'world', function=print_world)

main_menu = MenuBuilder(io = io, title = 'main menu')
main_menu.add_sub_menu_item('print', sub_menu=printt)
main_menu.add_function_item('zalmen', 'shneyor', name = 'print name', function=print_name)

main_menu.run_menu(menu=main_menu, requested_exit='30', requested_main='10', requested_back='20')
# main_menu.build_menu(main_menu)
