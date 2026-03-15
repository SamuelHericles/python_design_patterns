from concrete_handlers import (
    Level1Support,
    Level2Support,
    Level3Support,
)


def chain_of_responsibility_demo():
    print("=== CHAIN OF RESPONSIBILITY ===")
    l1 = Level1Support()
    l2 = Level2Support()
    l3 = Level3Support()
    l1.set_next(l2).set_next(l3)

    issues = [
        (1, "Reset senha"),
        (2, "Bug no módulo X"),
        (3, "Falha crítica DB"),
    ]
    for level, issue in issues:
        print(l1.handle(level, issue))
    print()


if __name__ == "__main__":
    chain_of_responsibility_demo()
