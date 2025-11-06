from abc import ABC, abstractmethod
from typing import List, Union, Dict

from menu_building.items.function_item import FunctionItem
# from menu_building.menu import Menu


class IndexMethod(ABC):
    @staticmethod
    @abstractmethod
    def index_items(items):
        pass


class NumberIndex(IndexMethod):
    @staticmethod
    def index_items(items):
        dict_index = {}
        for item in items:
            dict_index[item.title] = item
        for number, item in enumerate(items):
            dict_index[str(number + 1)] = item
        return dict_index


class AbcIndex(IndexMethod):
    @staticmethod
    def index_items(items):
        dict_index = {}
        for item in items:
            dict_index[item.title] = item
        for number, item in enumerate(items):
            dict_index[chr(number + 97).lower()] = item
        return dict_index


class TextIndex(IndexMethod):
    @staticmethod
    def index_items(items):
        dict_index = {}
        for item in items:
            dict_index[item.title] = item
        return dict_index