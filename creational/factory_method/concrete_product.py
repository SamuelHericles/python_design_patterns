from product import Notification


class EmailNotification(Notification):
    def notify(self, message: str) -> str:
        return f"[EMAIL] {message}"


class SMSNotification(Notification):
    def notify(self, message: str) -> str:
        return f"[SMS] {message}"


class PushNotification(Notification):
    def notify(self, message: str) -> str:
        return f"[PUSH] {message}"
