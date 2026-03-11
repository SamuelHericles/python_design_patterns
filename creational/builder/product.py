# ---- builder/product.py
class Pizza:
    def __init__(self):
        self.size = None
        self.crust = None
        self.sauce = None
        self.toppings = []

    def __str__(self):
        return (
            f"Pizza({self.size}, crust={self.crust}, "
            f"sauce={self.sauce}, toppings={self.toppings})"
        )
