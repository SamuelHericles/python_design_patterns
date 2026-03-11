from creational.factory_method.concrete_creator import (
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


factory_method_demo()
