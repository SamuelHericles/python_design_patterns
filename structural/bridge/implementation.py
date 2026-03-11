from abc import ABC, abstractmethod


class Renderer(ABC):
    @abstractmethod
    def render_circle(self, x, y, radius) -> str:
        pass

    @abstractmethod
    def render_square(self, x, y, side) -> str:
        pass
