from facade import Computer


def facade_demo():
    print("=== FACADE ===")
    computer = Computer()
    print(computer.start())
    print()


if __name__ == "__main__":
    facade_demo()
