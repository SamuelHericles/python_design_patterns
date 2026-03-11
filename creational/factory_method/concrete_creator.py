from product import Notification
from creator import NotificationCreator
from concrete_product import (
    EmailNotification,
    SMSNotification,
    PushNotification,
)


class EmailCreator(NotificationCreator):
    def create_notification(self) -> Notification:
        return EmailNotification()


class SMSCreator(NotificationCreator):
    def create_notification(self) -> Notification:
        return SMSNotification()


class PushCreator(NotificationCreator):
    def create_notification(self) -> Notification:
        return PushNotification()
