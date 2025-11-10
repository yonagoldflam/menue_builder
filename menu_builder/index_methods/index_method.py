from abc import ABC, abstractmethod
from typing import List, Dict

from menu_builder.consts import MenuIcons
from menu_builder.menu_building.items.menu_item import MenuItem, Back, Home, Exit


class IndexMethod(ABC):

    @staticmethod
    @abstractmethod
    def index_items(items: List[MenuItem], back_keys: Dict[str, str], parent: MenuItem) -> Dict[str, MenuItem]:
        pass


class NumberIndex(IndexMethod):

    @staticmethod
    def index_items(items, back_keys, parent):

        dict_index = {}
        for item in items:
            dict_index[item.title] = item

        for number, item in enumerate(items):
            dict_index[str(number + 1)] = item

        dict_index[back_keys[MenuIcons.BACK_MAIN]] = Home(parent)
        dict_index[back_keys[MenuIcons.BACK]] = Back(parent)
        dict_index[back_keys[MenuIcons.EXIT]] = Exit(parent)

        return dict_index


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

