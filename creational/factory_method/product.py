from abc import ABC, abstractmethod

# ABC -> needed to create a abstract class and methods - just rules names


class Notification(ABC):
    @abstractmethod
    def notify(self, message: str) -> str:
        pass
