# =============================================================================
# ==================== PADRÕES CRIACIONAIS (CREATIONAL) =======================
# =============================================================================

# =============================================================================
# SINGLETON
# =============================================================================
#
# singleton/
# ├── singleton.py
# └── main.py
#
# =============================================================================


# ---- singleton/singleton.py
class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._connected = False
            cls._instance._url = None
        return cls._instance

    def connect(self, url: str):
        if not self._connected:
            self._url = url
            self._connected = True
            print(f"  Conectado a: {url}")
        else:
            print(f"  Já conectado a: {self._url}")

    def query(self, sql: str) -> str:
        return f"  Resultado de: {sql}"


# ---- singleton/main.py
def singleton_demo():
    print("=== SINGLETON ===")
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    db1.connect("postgresql://localhost:5432/mydb")
    db2.connect("mysql://localhost:3306/otherdb")  # será ignorado
    print(f"  db1 is db2: {db1 is db2}")
    print(db1.query("SELECT * FROM users"))
    print()


singleton_demo()

# =============================================================================
# PROTOTYPE
# =============================================================================
#
# prototype/
# ├── prototype.py         # Interface Prototype
# ├── concrete_prototype.py
# └── main.py
#
# =============================================================================

import copy


# ---- prototype/prototype.py
class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


# ---- prototype/concrete_prototype.py
class Document(Prototype):
    def __init__(self, title: str, content: str, tags: list):
        self.title = title
        self.content = content
        self.tags = tags

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Document(title={self.title}, tags={self.tags})"


# ---- prototype/main.py
def prototype_demo():
    print("=== PROTOTYPE ===")
    original = Document("Relatório Q1", "Conteúdo original", ["financeiro", "2024"])
    clone1 = original.clone()
    clone1.title = "Relatório Q2"
    clone1.tags.append("revisado")

    print(f"Original: {original}")
    print(f"Clone:    {clone1}")
    print()


prototype_demo()

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


# =============================================================================
# BUILDER
# =============================================================================
#
# builder/
# ├── builder.py          # Interface do builder
# ├── concrete_builder.py # Builder concreto
# ├── director.py         # Diretor
# ├── product.py          # Produto
# └── main.py
#
# =============================================================================


# ---- builder/product.py
class Pizza:
    def __init__(self):
        self.size = None
        self.crust = None
        self.sauce = None
        self.toppings = []

    def __str__(self):
        return (
            f"Pizza({self.size}, crust={self.crust}, "
            f"sauce={self.sauce}, toppings={self.toppings})"
        )


# ---- builder/builder.py
class PizzaBuilder(ABC):
    @abstractmethod
    def set_size(self, size: str):
        pass

    @abstractmethod
    def set_crust(self, crust: str):
        pass

    @abstractmethod
    def set_sauce(self, sauce: str):
        pass

    @abstractmethod
    def add_topping(self, topping: str):
        pass

    @abstractmethod
    def build(self) -> Pizza:
        pass


# ---- builder/concrete_builder.py
class ConcretePizzaBuilder(PizzaBuilder):
    def __init__(self):
        self._pizza = Pizza()

    def set_size(self, size: str):
        self._pizza.size = size
        return self

    def set_crust(self, crust: str):
        self._pizza.crust = crust
        return self

    def set_sauce(self, sauce: str):
        self._pizza.sauce = sauce
        return self

    def add_topping(self, topping: str):
        self._pizza.toppings.append(topping)
        return self

    def build(self) -> Pizza:
        pizza = self._pizza
        self._pizza = Pizza()
        return pizza


# ---- builder/director.py
class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self._builder = builder

    def make_margherita(self) -> Pizza:
        return (
            self._builder.set_size("medium")
            .set_crust("thin")
            .set_sauce("tomato")
            .add_topping("mozzarella")
            .add_topping("basil")
            .build()
        )

    def make_pepperoni(self) -> Pizza:
        return (
            self._builder.set_size("large")
            .set_crust("thick")
            .set_sauce("tomato")
            .add_topping("pepperoni")
            .add_topping("cheese")
            .build()
        )


# ---- builder/main.py
def builder_demo():
    print("=== BUILDER ===")
    builder = ConcretePizzaBuilder()
    director = PizzaDirector(builder)
    print(director.make_margherita())
    print(director.make_pepperoni())
    print()


builder_demo()
