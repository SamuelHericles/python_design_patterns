from context import TrafficLightState


# Sempre haverá uma sequência exata de eventos, talvez ciclicos.
class GreenState(TrafficLightState):
    def color(self) -> str:
        return "VERDE"

    def handle(self, context: "TrafficLight") -> str:
        context.state = YellowState()
        return "  🟢 Verde - Pode passar. Próximo: Amarelo"


class YellowState(TrafficLightState):
    def color(self) -> str:
        return "AMARELO"

    def handle(self, context: "TrafficLight") -> str:
        context.state = RedState()
        return "  🟡 Amarelo - Atenção. Próximo: Vermelho"


class RedState(TrafficLightState):
    def color(self) -> str:
        return "VERMELHO"

    def handle(self, context: "TrafficLight") -> str:
        context.state = GreenState()
        return "  🔴 Vermelho - Pare. Próximo: Verde"
