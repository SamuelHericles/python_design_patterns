from builder import PizzaBuilder
from product import Pizza


class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self._builder = builder

    def make_margherita(self) -> Pizza:
        return (
            self._builder.set_size("medium")
            .set_crust("thin")
            .set_sauce("tomato")
            .add_topping("mozzarella")
            .add_topping("basil")
            .build()
        )

    def make_pepperoni(self) -> Pizza:
        return (
            self._builder.set_size("large")
            .set_crust("thick")
            .set_sauce("tomato")
            .add_topping("pepperoni")
            .add_topping("cheese")
            .build()
        )
