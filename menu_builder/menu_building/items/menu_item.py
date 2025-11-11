from abc import ABC, abstractmethod


class MenuItem(ABC):
    parent: 'MenuItem'
    title: str

    @abstractmethod
    def select(self):
        pass
