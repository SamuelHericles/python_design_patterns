from abc import ABC, abstractmethod


class FileSystemComponent(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def display(self, indent: int = 0) -> str:
        pass

    @abstractmethod
    def size(self) -> int:
        pass
