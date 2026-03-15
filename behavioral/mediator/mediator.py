from abc import ABC, abstractmethod


class ChatMediator(ABC):
    @abstractmethod
    def send_message(self, message: str, sender: "ChatUser"):
        pass

    @abstractmethod
    def add_user(self, user: "ChatUser"):
        pass
