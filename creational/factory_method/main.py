from concrete_creator import (
    EmailCreator,
    SMSCreator,
    PushCreator,
)


def factory_method_demo():
    print("=== FACTORY METHOD ===")
    creators = [EmailCreator(), SMSCreator(), PushCreator()]
    for creator in creators:
        print(creator.send("Olá, mundo!"))
    print()


if __name__ == "__main__":
    factory_method_demo()
