from menu_builder.index_methods.index_method import IndexMethod
from menu_builder.consts import MenuIcons
from menu_builder.menu_building.items.home import Home
from menu_builder.menu_building.items.back import Back
from menu_builder.menu_building.items.exit import Exit

class AbcIndex(IndexMethod):

    @staticmethod
    def index_items(items, back_keys, parent):

        dict_index = {}
        for item in items:
            dict_index[item.title] = item

        for number, item in enumerate(items):
            dict_index[chr(number + 97).lower()] = item

        dict_index[back_keys[MenuIcons.BACK_MAIN]] = Home(parent)
        dict_index[back_keys[MenuIcons.BACK]] = Back(parent)
        dict_index[back_keys[MenuIcons.EXIT]] = Exit(parent)

        return dict_index