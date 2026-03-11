from windows_factory import WindowsFactory
from mac_factory import MacFactory


def abstract_factory_demo():
    print("=== ABSTRACT FACTORY ===")
    for factory in [WindowsFactory(), MacFactory()]:
        btn = factory.create_button()
        chk = factory.create_checkbox()
        print(f"  {btn.render()} + {chk.render()}")
    print()


if __name__ == "__main__":
    abstract_factory_demo()
