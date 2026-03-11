from refined_abstraction import Circle, Square
from concrete_impl import VectorRenderer, RasterRenderer


# ---- bridge/main.py
def bridge_demo():
    print("=== BRIDGE ===")
    shapes = [
        Circle(VectorRenderer(), 0, 0, 5),
        Circle(RasterRenderer(), 1, 2, 3),
        Square(VectorRenderer(), 4, 4, 10),
    ]
    for shape in shapes:
        print(f"  {shape.draw()}")
    print()


if __name__ == "__main__":
    bridge_demo()
