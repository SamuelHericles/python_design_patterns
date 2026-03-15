from typing import List
from observer import Observer


class Stock:
    def __init__(self, symbol: str, price: float):
        self._symbol = symbol
        self._price = price
        self._observers: List[Observer] = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def _notify(self, event: str):
        for obs in self._observers:
            obs.update(event, {"symbol": self._symbol, "price": self._price})

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        old = self._price
        self._price = value
        # Toda vez que muda o valor, é notificado
        direction = "↑" if value > old else "↓"
        self._notify(f"price_change {direction}")
