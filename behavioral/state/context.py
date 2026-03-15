from abc import ABC, abstractmethod


class TrafficLightState(ABC):
    @abstractmethod
    def handle(self, context: "TrafficLight") -> str:
        pass

    @abstractmethod
    def color(self) -> str:
        pass
