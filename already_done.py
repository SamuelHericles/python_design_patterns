# =============================================================================
# ==================== PADRÕES CRIACIONAIS (CREATIONAL) =======================
# =============================================================================

# =============================================================================
# FACTORY METHOD
# =============================================================================
#
# Estrutura de arquivos (abstracted into sections below):
#
# factory_method/
# ├── creator.py          # Classe abstrata com factory method
# ├── concrete_creator.py # Implementações concretas do criador
# ├── product.py          # Interface do produto
# ├── concrete_product.py # Produtos concretos
# └── main.py             # Cliente
#
# =============================================================================

from abc import ABC, abstractmethod


# ---- factory_method/product.py
class Notification(ABC):
    @abstractmethod
    def notify(self, message: str) -> str:
        pass


# ---- factory_method/concrete_product.py
class EmailNotification(Notification):
    def notify(self, message: str) -> str:
        return f"[EMAIL] {message}"


class SMSNotification(Notification):
    def notify(self, message: str) -> str:
        return f"[SMS] {message}"


class PushNotification(Notification):
    def notify(self, message: str) -> str:
        return f"[PUSH] {message}"


# ---- factory_method/creator.py
class NotificationCreator(ABC):
    @abstractmethod
    def create_notification(self) -> Notification:
        pass

    def send(self, message: str) -> str:
        notification = self.create_notification()
        return notification.notify(message)


# ---- factory_method/concrete_creator.py
class EmailCreator(NotificationCreator):
    def create_notification(self) -> Notification:
        return EmailNotification()


class SMSCreator(NotificationCreator):
    def create_notification(self) -> Notification:
        return SMSNotification()


class PushCreator(NotificationCreator):
    def create_notification(self) -> Notification:
        return PushNotification()


# ---- factory_method/main.py
def factory_method_demo():
    print("=== FACTORY METHOD ===")
    creators = [EmailCreator(), SMSCreator(), PushCreator()]
    for creator in creators:
        print(creator.send("Olá, mundo!"))
    print()


factory_method_demo()

# =============================================================================
# ABSTRACT FACTORY
# =============================================================================
#
# abstract_factory/
# ├── abstract_factory.py    # Interface da fábrica abstrata
# ├── abstract_products.py   # Interfaces dos produtos
# ├── windows_factory.py     # Fábrica Windows
# ├── mac_factory.py         # Fábrica Mac
# └── main.py
#
# =============================================================================


# ---- abstract_factory/abstract_products.py
class Button(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class Checkbox(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


# ---- abstract_factory/abstract_factory.py
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


# ---- abstract_factory/windows_factory.py
class WindowsButton(Button):
    def render(self) -> str:
        return "[Windows Button]"


class WindowsCheckbox(Checkbox):
    def render(self) -> str:
        return "[Windows Checkbox]"


class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


# ---- abstract_factory/mac_factory.py
class MacButton(Button):
    def render(self) -> str:
        return "(Mac Button)"


class MacCheckbox(Checkbox):
    def render(self) -> str:
        return "(Mac Checkbox)"


class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


# ---- abstract_factory/main.py
def abstract_factory_demo():
    print("=== ABSTRACT FACTORY ===")
    for factory in [WindowsFactory(), MacFactory()]:
        btn = factory.create_button()
        chk = factory.create_checkbox()
        print(f"  {btn.render()} + {chk.render()}")
    print()


abstract_factory_demo()
