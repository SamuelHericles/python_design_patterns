from director import PizzaDirector
from concrete_builder import ConcretePizzaBuilder


def builder_demo():
    print("=== BUILDER ===")
    builder = ConcretePizzaBuilder()
    director = PizzaDirector(builder)
    print(director.make_margherita())
    print(director.make_pepperoni())
    print()


if __name__ == "__main__":
    builder_demo()
