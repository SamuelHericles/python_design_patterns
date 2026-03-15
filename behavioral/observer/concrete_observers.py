from observer import Observer


class AlertObserver(Observer):
    def __init__(self, name: str, threshold: float):
        self.name = name
        self.threshold = threshold

    def update(self, event: str, data):
        if data["price"] > self.threshold:
            print(
                f"  🚨 {self.name}: {data['symbol']} = R${data['price']:.2f} ({event})"
            )


class LogObserver(Observer):
    def update(self, event: str, data):
        print(f"  📋 Log: {data['symbol']} {event} -> R${data['price']:.2f}")
