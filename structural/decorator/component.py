from abc import ABC, abstractmethod


class TextFormatter(ABC):
    @abstractmethod
    def format(self, text: str) -> str:
        pass
