from abc import ABC, abstractmethod
from abstract_products import Button, Checkbox


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass
