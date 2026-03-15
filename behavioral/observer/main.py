from concrete_observers import AlertObserver, LogObserver
from subject import Stock


def observer_demo():
    print("=== OBSERVER ===")
    petr4 = Stock("PETR4", 35.00)
    petr4.attach(AlertObserver("Trader A", 36.0))
    petr4.attach(AlertObserver("Trader B", 37.0))
    petr4.attach(LogObserver())

    petr4.price = 36.50
    petr4.price = 37.20
    print()


if __name__ == "__main__":
    observer_demo()
