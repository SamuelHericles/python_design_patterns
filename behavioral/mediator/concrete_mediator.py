from mediator import ChatMediator
from colleage import ChatUser
from typing import List


class ChatRoom(ChatMediator):
    def __init__(self):
        self._users: List[ChatUser] = []

    def add_user(self, user: ChatUser):
        self._users.append(user)

    def send_message(self, message: str, sender: ChatUser):
        for user in self._users:
            if user is not sender:
                user.receive(message, sender.name)
