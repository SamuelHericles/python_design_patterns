from builder import PizzaBuilder
from product import Pizza


class ConcretePizzaBuilder(PizzaBuilder):
    def __init__(self):
        self._pizza = Pizza()

    def set_size(self, size: str):
        self._pizza.size = size
        return self

    def set_crust(self, crust: str):
        self._pizza.crust = crust
        return self

    def set_sauce(self, sauce: str):
        self._pizza.sauce = sauce
        return self

    def add_topping(self, topping: str):
        self._pizza.toppings.append(topping)
        return self

    def build(self) -> Pizza:
        pizza = self._pizza
        self._pizza = Pizza()
        return pizza
