from abc import ABC, abstractmethod

class MenuIo(ABC):
    @abstractmethod
    def output(self, message: str) -> str:
        pass
    @abstractmethod
    def input(self, prompt: str) -> str:
        pass
