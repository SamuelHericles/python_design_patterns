# =============================================================================
# ================== PADRÕES ESTRUTURAIS (STRUCTURAL) ========================
# =============================================================================

# =============================================================================
# FACADE
# =============================================================================
#
# facade/
# ├── subsystems/
# │   ├── cpu.py
# │   ├── memory.py
# │   ├── hard_drive.py
# │   └── bios.py
# ├── facade.py
# └── main.py
#
# =============================================================================


# ---- facade/subsystems/cpu.py
class CPU:
    def freeze(self):
        return "  CPU: freeze"

    def jump(self, address):
        return f"  CPU: jump to {address}"

    def execute(self):
        return "  CPU: execute"


# ---- facade/subsystems/memory.py
class Memory:
    def load(self, position, data):
        return f"  Memory: load {data} at {position}"


# ---- facade/subsystems/hard_drive.py
class HardDrive:
    def read(self, lba, size):
        return f"  HDD: read {size} bytes from sector {lba}"


# ---- facade/subsystems/bios.py
class BIOS:
    BOOT_ADDRESS = "0x00"
    BOOT_SECTOR = 0
    SECTOR_SIZE = 512


# ---- facade/facade.py
class Computer:
    def __init__(self):
        self._cpu = CPU()
        self._memory = Memory()
        self._hdd = HardDrive()

    def start(self):
        steps = []
        steps.append(self._cpu.freeze())
        steps.append(
            self._memory.load(
                BIOS.BOOT_ADDRESS, self._hdd.read(BIOS.BOOT_SECTOR, BIOS.SECTOR_SIZE)
            )
        )
        steps.append(self._cpu.jump(BIOS.BOOT_ADDRESS))
        steps.append(self._cpu.execute())
        return "\n".join(steps)


# ---- facade/main.py
def facade_demo():
    print("=== FACADE ===")
    computer = Computer()
    print(computer.start())
    print()


facade_demo()

# =============================================================================
# DECORATOR
# =============================================================================
#
# decorator/
# ├── component.py
# ├── concrete_component.py
# ├── decorator.py
# ├── concrete_decorators.py
# └── main.py
#
# =============================================================================


# ---- decorator/component.py
class TextFormatter(ABC):
    @abstractmethod
    def format(self, text: str) -> str:
        pass


# ---- decorator/concrete_component.py
class PlainText(TextFormatter):
    def format(self, text: str) -> str:
        return text


# ---- decorator/decorator.py
class TextDecorator(TextFormatter):
    def __init__(self, wrapped: TextFormatter):
        self._wrapped = wrapped

    def format(self, text: str) -> str:
        return self._wrapped.format(text)


# ---- decorator/concrete_decorators.py
class BoldDecorator(TextDecorator):
    def format(self, text: str) -> str:
        return f"**{self._wrapped.format(text)}**"


class ItalicDecorator(TextDecorator):
    def format(self, text: str) -> str:
        return f"_{self._wrapped.format(text)}_"


class UpperCaseDecorator(TextDecorator):
    def format(self, text: str) -> str:
        return self._wrapped.format(text).upper()


# ---- decorator/main.py
def decorator_demo():
    print("=== DECORATOR ===")
    text = PlainText()
    bold_italic = ItalicDecorator(BoldDecorator(text))
    upper_bold = UpperCaseDecorator(BoldDecorator(text))

    print(f"  Plain:       {text.format('hello world')}")
    print(f"  Bold+Italic: {bold_italic.format('hello world')}")
    print(f"  Upper+Bold:  {upper_bold.format('hello world')}")
    print()


decorator_demo()


# =============================================================================
# COMPOSITE
# =============================================================================
#
# composite/
# ├── component.py
# ├── leaf.py
# ├── composite.py
# └── main.py
#
# =============================================================================

from typing import List


# ---- composite/component.py
class FileSystemComponent(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def display(self, indent: int = 0) -> str:
        pass

    @abstractmethod
    def size(self) -> int:
        pass


# ---- composite/leaf.py
class File(FileSystemComponent):
    def __init__(self, name: str, size_kb: int):
        super().__init__(name)
        self._size = size_kb

    def display(self, indent: int = 0) -> str:
        return "  " * indent + f"📄 {self.name} ({self._size}kb)"

    def size(self) -> int:
        return self._size


# ---- composite/composite.py
class Directory(FileSystemComponent):
    def __init__(self, name: str):
        super().__init__(name)
        self._children: List[FileSystemComponent] = []

    def add(self, component: FileSystemComponent):
        self._children.append(component)

    def remove(self, component: FileSystemComponent):
        self._children.remove(component)

    def display(self, indent: int = 0) -> str:
        result = "  " * indent + f"📁 {self.name}/\n"
        for child in self._children:
            result += child.display(indent + 1) + "\n"
        return result.rstrip()

    def size(self) -> int:
        return sum(child.size() for child in self._children)


# ---- composite/main.py
def composite_demo():
    print("=== COMPOSITE ===")
    root = Directory("projeto")
    src = Directory("src")
    src.add(File("main.py", 10))
    src.add(File("utils.py", 5))
    tests = Directory("tests")
    tests.add(File("test_main.py", 8))
    root.add(src)
    root.add(tests)
    root.add(File("README.md", 2))

    print(root.display())
    print(f"  Tamanho total: {root.size()}kb")
    print()


composite_demo()
# =============================================================================
# BRIDGE
# =============================================================================
#
# bridge/
# ├── implementation.py     # Interface de implementação
# ├── concrete_impl.py      # Implementações concretas
# ├── abstraction.py        # Abstração
# ├── refined_abstraction.py
# └── main.py
#
# =============================================================================


# ---- bridge/implementation.py
class Renderer(ABC):
    @abstractmethod
    def render_circle(self, x, y, radius) -> str:
        pass

    @abstractmethod
    def render_square(self, x, y, side) -> str:
        pass


# ---- bridge/concrete_impl.py
class VectorRenderer(Renderer):
    def render_circle(self, x, y, radius) -> str:
        return f"Círculo vetorial em ({x},{y}) r={radius}"

    def render_square(self, x, y, side) -> str:
        return f"Quadrado vetorial em ({x},{y}) l={side}"


class RasterRenderer(Renderer):
    def render_circle(self, x, y, radius) -> str:
        return f"Círculo raster em ({x},{y}) r={radius}"

    def render_square(self, x, y, side) -> str:
        return f"Quadrado raster em ({x},{y}) l={side}"


# ---- bridge/abstraction.py
class Shape(ABC):
    def __init__(self, renderer: Renderer):
        self._renderer = renderer

    @abstractmethod
    def draw(self) -> str:
        pass


# ---- bridge/refined_abstraction.py
class Circle(Shape):
    def __init__(self, renderer, x, y, radius):
        super().__init__(renderer)
        self.x, self.y, self.radius = x, y, radius

    def draw(self) -> str:
        return self._renderer.render_circle(self.x, self.y, self.radius)


class Square(Shape):
    def __init__(self, renderer, x, y, side):
        super().__init__(renderer)
        self.x, self.y, self.side = x, y, side

    def draw(self) -> str:
        return self._renderer.render_square(self.x, self.y, self.side)


# ---- bridge/main.py
def bridge_demo():
    print("=== BRIDGE ===")
    shapes = [
        Circle(VectorRenderer(), 0, 0, 5),
        Circle(RasterRenderer(), 1, 2, 3),
        Square(VectorRenderer(), 4, 4, 10),
    ]
    for shape in shapes:
        print(f"  {shape.draw()}")
    print()


bridge_demo()

# =============================================================================
# ADAPTER
# =============================================================================
#
# adapter/
# ├── target.py           # Interface esperada pelo cliente
# ├── adaptee.py          # Classe incompatível existente
# ├── adapter.py          # Adaptador
# └── main.py
#
# =============================================================================


# ---- adapter/target.py
class JSONDataProcessor:
    def process(self, data: dict) -> str:
        return f"JSON processado: {data}"


# ---- adapter/adaptee.py
class XMLDataProcessor:
    def process_xml(self, xml_string: str) -> str:
        return f"XML processado: {xml_string}"


# ---- adapter/adapter.py
import json


class XMLToJSONAdapter(JSONDataProcessor):
    def __init__(self, xml_processor: XMLDataProcessor):
        self._xml_processor = xml_processor

    def process(self, data: dict) -> str:
        xml_string = self._dict_to_xml(data)
        return self._xml_processor.process_xml(xml_string)

    def _dict_to_xml(self, data: dict) -> str:
        items = "".join(f"<{k}>{v}</{k}>" for k, v in data.items())
        return f"<root>{items}</root>"


# ---- adapter/main.py
def adapter_demo():
    print("=== ADAPTER ===")
    data = {"name": "Alice", "age": 30}
    json_proc = JSONDataProcessor()
    xml_proc = XMLDataProcessor()
    adapter = XMLToJSONAdapter(xml_proc)

    print(f"  {json_proc.process(data)}")
    print(f"  {adapter.process(data)}")
    print()


adapter_demo()


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
