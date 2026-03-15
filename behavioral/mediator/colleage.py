from mediator import ChatMediator


class ChatUser:
    def __init__(self, name: str, mediator: ChatMediator):
        self.name = name
        self._mediator = mediator
        self._mediator.add_user(self)

    def send(self, message: str):
        print(f"  {self.name} envia: {message}")
        self._mediator.send_message(message, self)

    def receive(self, message: str, sender: str):
        print(f"  {self.name} recebe de {sender}: {message}")
