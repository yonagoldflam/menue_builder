from abc import ABC, abstractmethod
from typing import List, Dict
from menu_builder.menu_building.items.menu_item import MenuItem


class IndexMethod(ABC):

    @staticmethod
    @abstractmethod
    def index_items(items: List[MenuItem], back_keys: Dict[str, str], parent: MenuItem) -> Dict[str, MenuItem]:
        pass