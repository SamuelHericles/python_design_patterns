from abc import ABC, abstractmethod
from implementation import Renderer


class Shape(ABC):
    def __init__(self, renderer: Renderer):
        self._renderer = renderer

    @abstractmethod
    def draw(self) -> str:
        pass
