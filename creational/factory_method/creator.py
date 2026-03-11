from abc import ABC, abstractmethod
from creational.factory_method.product import Notification


# ABC -> needed to create a abstract class and methods - just rules names


class NotificationCreator(ABC):
    @abstractmethod
    def create_notification(self) -> Notification:
        pass

    def send(self, message: str) -> str:
        notification = self.create_notification()
        return notification.notify(message)
