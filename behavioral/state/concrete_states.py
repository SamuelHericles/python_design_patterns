from context import TrafficLightState
from state import GreenState


class TrafficLight:
    def __init__(self):
        # Estado inicial
        self.state: TrafficLightState = GreenState()

    def change(self) -> str:
        # Só muda o estado quando executa o change - handle já no gatilho
        return self.state.handle(self)
