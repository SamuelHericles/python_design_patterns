from creational.factory_method.product import Notification
from creational.factory_method.creator import NotificationCreator
from creational.factory_method.concrete_product import (
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
