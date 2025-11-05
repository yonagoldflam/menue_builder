from menu_building.menu_builder import MenuBuilder
from io_selection.console_io import ConsoleIo




def print_hello():
    print('hello')


def print_world():
    print('world')


def print_home():
    print('home')


def print_name(*names, name1, name2):
    # name = input('enter your name: ')
    for name in names:
        print(name)
    print(name1, name2)


# menu = {'print': {'hello': {'world': print_world, 'home': print_home}, 'world': print_world}, 'print name': print_name}

io = ConsoleIo()

menu_builder = MenuBuilder()

menu_builder.add_menu(io=io, title= 'hello')
menu_builder.add_function_item(menu_title='hello', name = 'home', function=print_home)
menu_builder.add_function_item(menu_title='hello',name = 'world', function=print_world)

menu_builder.add_menu(io=io, title='print')
menu_builder.add_sub_menu_item('print', sub_menu_title= 'hello')
menu_builder.add_function_item(menu_title= 'print', name = 'world', function=print_world)

menu_builder.add_menu(io = io, title = 'main menu', abc_option=True, requested_main='20',requested_exit='10',requested_back='30')
menu_builder.add_sub_menu_item('main menu', sub_menu_title='print')
menu_builder.add_function_item('zalmen', 'shneyor', menu_title='main menu',name = 'print name', function=print_name, parms=['name1', 'name2'])

menu_builder.run_menu('main menu')
