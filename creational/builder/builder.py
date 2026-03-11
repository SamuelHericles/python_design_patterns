from abc import ABC, abstractmethod
from product import Pizza


# ---- builder/builder.py
class PizzaBuilder(ABC):
    @abstractmethod
    def set_size(self, size: str):
        pass

    @abstractmethod
    def set_crust(self, crust: str):
        pass

    @abstractmethod
    def set_sauce(self, sauce: str):
        pass

    @abstractmethod
    def add_topping(self, topping: str):
        pass

    @abstractmethod
    def build(self) -> Pizza:
        pass
