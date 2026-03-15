# =============================================================================
# GOF - GANG OF FOUR - 23 DESIGN PATTERNS IN PYTHON
# =============================================================================
from abc import ABC, abstractmethod

# =============================================================================
# STRATEGY
# =============================================================================
#
# strategy/
# ├── strategy.py
# ├── concrete_strategies.py
# ├── context.py
# └── main.py
#
# =============================================================================


# ---- strategy/strategy.py
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: list) -> list:
        pass


# ---- strategy/concrete_strategies.py
class BubbleSortStrategy(SortStrategy):
    def sort(self, data: list) -> list:
        arr = data.copy()
        n = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


class QuickSortStrategy(SortStrategy):
    def sort(self, data: list) -> list:
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        mid = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + mid + self.sort(right)


class ReverseSortStrategy(SortStrategy):
    def sort(self, data: list) -> list:
        return sorted(data, reverse=True)


# ---- strategy/context.py
class Sorter:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: SortStrategy):
        self._strategy = strategy

    def sort(self, data: list) -> list:
        return self._strategy.sort(data)


# ---- strategy/main.py
def strategy_demo():
    print("=== STRATEGY ===")
    data = [5, 2, 8, 1, 9, 3]
    sorter = Sorter(BubbleSortStrategy())
    print(f"  Bubble:  {sorter.sort(data)}")
    sorter.strategy = QuickSortStrategy()
    print(f"  Quick:   {sorter.sort(data)}")
    sorter.strategy = ReverseSortStrategy()
    print(f"  Reverse: {sorter.sort(data)}")
    print()


strategy_demo()
# =============================================================================
# STATE
# =============================================================================
#
# state/
# ├── state.py
# ├── concrete_states.py
# ├── context.py
# └── main.py
#
# =============================================================================


# ---- state/state.py
class TrafficLightState(ABC):
    @abstractmethod
    def handle(self, context: "TrafficLight") -> str:
        pass

    @abstractmethod
    def color(self) -> str:
        pass


# ---- state/concrete_states.py
class GreenState(TrafficLightState):
    def color(self) -> str:
        return "VERDE"

    def handle(self, context: "TrafficLight") -> str:
        context.state = YellowState()
        return "  🟢 Verde - Pode passar. Próximo: Amarelo"


class YellowState(TrafficLightState):
    def color(self) -> str:
        return "AMARELO"

    def handle(self, context: "TrafficLight") -> str:
        context.state = RedState()
        return "  🟡 Amarelo - Atenção. Próximo: Vermelho"


class RedState(TrafficLightState):
    def color(self) -> str:
        return "VERMELHO"

    def handle(self, context: "TrafficLight") -> str:
        context.state = GreenState()
        return "  🔴 Vermelho - Pare. Próximo: Verde"


# ---- state/context.py
class TrafficLight:
    def __init__(self):
        self.state: TrafficLightState = GreenState()

    def change(self) -> str:
        return self.state.handle(self)


# ---- state/main.py
def state_demo():
    print("=== STATE ===")
    light = TrafficLight()
    for _ in range(4):
        print(light.change())
    print()


state_demo()


# =============================================================================
# OBSERVER
# =============================================================================
#
# observer/
# ├── observer.py
# ├── subject.py
# ├── concrete_observers.py
# └── main.py
#
# =============================================================================


# ---- observer/observer.py
class Observer(ABC):
    @abstractmethod
    def update(self, event: str, data):
        pass


# ---- observer/subject.py (EventBus/Observable)
class Stock:
    def __init__(self, symbol: str, price: float):
        self._symbol = symbol
        self._price = price
        self._observers: List[Observer] = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def _notify(self, event: str):
        for obs in self._observers:
            obs.update(event, {"symbol": self._symbol, "price": self._price})

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        old = self._price
        self._price = value
        direction = "↑" if value > old else "↓"
        self._notify(f"price_change {direction}")


# ---- observer/concrete_observers.py
class AlertObserver(Observer):
    def __init__(self, name: str, threshold: float):
        self.name = name
        self.threshold = threshold

    def update(self, event: str, data):
        if data["price"] > self.threshold:
            print(
                f"  🚨 {self.name}: {data['symbol']} = R${data['price']:.2f} ({event})"
            )


class LogObserver(Observer):
    def update(self, event: str, data):
        print(f"  📋 Log: {data['symbol']} {event} -> R${data['price']:.2f}")


# ---- observer/main.py
def observer_demo():
    print("=== OBSERVER ===")
    petr4 = Stock("PETR4", 35.00)
    petr4.attach(AlertObserver("Trader A", 36.0))
    petr4.attach(AlertObserver("Trader B", 37.0))
    petr4.attach(LogObserver())

    petr4.price = 36.50
    petr4.price = 37.20
    print()


observer_demo()
# =============================================================================
# MEMENTO
# =============================================================================
#
# memento/
# ├── memento.py
# ├── originator.py
# ├── caretaker.py
# └── main.py
#
# =============================================================================


# ---- memento/memento.py
class EditorMemento:
    def __init__(self, content: str, cursor: int):
        self._content = content
        self._cursor = cursor

    @property
    def content(self):
        return self._content

    @property
    def cursor(self):
        return self._cursor


# ---- memento/originator.py
class CodeEditor:
    def __init__(self):
        self._content = ""
        self._cursor = 0

    def type(self, text: str):
        self._content += text
        self._cursor += len(text)

    def save(self) -> EditorMemento:
        return EditorMemento(self._content, self._cursor)

    def restore(self, memento: EditorMemento):
        self._content = memento.content
        self._cursor = memento.cursor

    def __str__(self):
        return f"  Editor: '{self._content}' | cursor={self._cursor}"


# ---- memento/caretaker.py
class EditorHistory:
    def __init__(self, editor: CodeEditor):
        self._editor = editor
        self._history: List[EditorMemento] = []

    def backup(self):
        self._history.append(self._editor.save())

    def undo(self):
        if self._history:
            self._editor.restore(self._history.pop())


# ---- memento/main.py
def memento_demo():
    print("=== MEMENTO ===")
    editor = CodeEditor()
    history = EditorHistory(editor)

    history.backup()
    editor.type("def hello():")
    history.backup()
    editor.type("\n    print('hi')")
    print(editor)

    history.undo()
    print(f"  Após undo: {editor}")
    print()


memento_demo()

# =============================================================================
# MEDIATOR
# =============================================================================
#
# mediator/
# ├── mediator.py
# ├── concrete_mediator.py
# ├── colleague.py
# └── main.py
#
# =============================================================================

from typing import Iterator as TypingIterator, Generic, TypeVar

T = TypeVar("T")


# ---- mediator/mediator.py
class ChatMediator(ABC):
    @abstractmethod
    def send_message(self, message: str, sender: "ChatUser"):
        pass

    @abstractmethod
    def add_user(self, user: "ChatUser"):
        pass


# ---- mediator/colleague.py
class ChatUser:
    def __init__(self, name: str, mediator: ChatMediator):
        self.name = name
        self._mediator = mediator
        self._mediator.add_user(self)

    def send(self, message: str):
        print(f"  {self.name} envia: {message}")
        self._mediator.send_message(message, self)

    def receive(self, message: str, sender: str):
        print(f"  {self.name} recebe de {sender}: {message}")


# ---- mediator/concrete_mediator.py
class ChatRoom(ChatMediator):
    def __init__(self):
        self._users: List[ChatUser] = []

    def add_user(self, user: ChatUser):
        self._users.append(user)

    def send_message(self, message: str, sender: ChatUser):
        for user in self._users:
            if user is not sender:
                user.receive(message, sender.name)


# ---- mediator/main.py
def mediator_demo():
    print("=== MEDIATOR ===")
    room = ChatRoom()
    alice = ChatUser("Alice", room)
    bob = ChatUser("Bob", room)
    carol = ChatUser("Carol", room)
    alice.send("Olá a todos!")
    print()


mediator_demo()


# =============================================================================
# ITERATOR
# =============================================================================
#
# iterator/
# ├── iterator.py
# ├── concrete_iterator.py
# ├── collection.py
# └── main.py
#
# =============================================================================


# ---- iterator/iterator.py
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# ---- iterator/concrete_iterator.py
class InOrderIterator:
    def __init__(self, root: TreeNode):
        self._stack = []
        self._push_left(root)

    def _push_left(self, node):
        while node:
            self._stack.append(node)
            node = node.left

    def __iter__(self):
        return self

    def __next__(self):
        if not self._stack:
            raise StopIteration
        node = self._stack.pop()
        self._push_left(node.right)
        return node.value


# ---- iterator/collection.py
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert(node.right, value)

    def __iter__(self):
        return InOrderIterator(self.root)


# ---- iterator/main.py
def iterator_demo():
    print("=== ITERATOR ===")
    tree = BinaryTree()
    for val in [5, 3, 7, 1, 4, 6, 8]:
        tree.insert(val)
    print(f"  In-order: {list(tree)}")
    print()


iterator_demo()

# =============================================================================
# COMMAND
# =============================================================================
#
# command/
# ├── command.py
# ├── concrete_commands.py
# ├── receiver.py
# ├── invoker.py
# └── main.py
#
# =============================================================================


# ---- command/receiver.py
class TextEditor:
    def __init__(self):
        self._text = ""

    def write(self, text: str):
        self._text += text
        print(f"  Editor: escreveu '{text}'")

    def delete(self, count: int):
        removed = self._text[-count:]
        self._text = self._text[:-count]
        print(f"  Editor: deletou '{removed}'")
        return removed

    @property
    def text(self):
        return self._text


# ---- command/command.py
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


# ---- command/concrete_commands.py
class WriteCommand(Command):
    def __init__(self, editor: TextEditor, text: str):
        self._editor = editor
        self._text = text

    def execute(self):
        self._editor.write(self._text)

    def undo(self):
        self._editor.delete(len(self._text))


class DeleteCommand(Command):
    def __init__(self, editor: TextEditor, count: int):
        self._editor = editor
        self._count = count
        self._deleted = ""

    def execute(self):
        self._deleted = self._editor.text[-self._count :]
        self._editor.delete(self._count)

    def undo(self):
        self._editor.write(self._deleted)


# ---- command/invoker.py
class CommandHistory:
    def __init__(self):
        self._history = []

    def execute(self, command: Command):
        command.execute()
        self._history.append(command)

    def undo(self):
        if self._history:
            self._history.pop().undo()


# ---- command/main.py
def command_demo():
    print("=== COMMAND ===")
    editor = TextEditor()
    history = CommandHistory()

    history.execute(WriteCommand(editor, "Olá "))
    history.execute(WriteCommand(editor, "mundo!"))
    print(f"  Texto: '{editor.text}'")
    history.undo()
    print(f"  Após undo: '{editor.text}'")
    print()


command_demo()

# =============================================================================
# ================= PADRÕES COMPORTAMENTAIS (BEHAVIORAL) =====================
# =============================================================================


# =============================================================================
# CHAIN OF RESPONSIBILITY
# =============================================================================
#
# chain_of_responsibility/
# ├── handler.py
# ├── concrete_handlers.py
# └── main.py
#
# =============================================================================


# ---- chain_of_responsibility/handler.py
class SupportHandler(ABC):
    def __init__(self):
        self._next: SupportHandler = None

    def set_next(self, handler: "SupportHandler") -> "SupportHandler":
        self._next = handler
        return handler

    @abstractmethod
    def handle(self, level: int, issue: str) -> str:
        pass

    def _pass_to_next(self, level: int, issue: str) -> str:
        if self._next:
            return self._next.handle(level, issue)
        return f"  Sem handler para nível {level}: {issue}"


# ---- chain_of_responsibility/concrete_handlers.py
class Level1Support(SupportHandler):
    def handle(self, level: int, issue: str) -> str:
        if level <= 1:
            return f"  [L1] Resolvido: {issue}"
        return self._pass_to_next(level, issue)


class Level2Support(SupportHandler):
    def handle(self, level: int, issue: str) -> str:
        if level <= 2:
            return f"  [L2] Resolvido: {issue}"
        return self._pass_to_next(level, issue)


class Level3Support(SupportHandler):
    def handle(self, level: int, issue: str) -> str:
        return f"  [L3 - Especialista] Resolvido: {issue}"


# ---- chain_of_responsibility/main.py
def chain_of_responsibility_demo():
    print("=== CHAIN OF RESPONSIBILITY ===")
    l1 = Level1Support()
    l2 = Level2Support()
    l3 = Level3Support()
    l1.set_next(l2).set_next(l3)

    issues = [(1, "Reset senha"), (2, "Bug no módulo X"), (3, "Falha crítica DB")]
    for level, issue in issues:
        print(l1.handle(level, issue))
    print()


chain_of_responsibility_demo()


# =============================================================================
# ================== PADRÕES ESTRUTURAIS (STRUCTURAL) ========================
# =============================================================================

# =============================================================================
# PROXY
# =============================================================================
#
# proxy/
# ├── subject.py
# ├── real_subject.py
# ├── proxy.py
# └── main.py
#
# =============================================================================


# ---- proxy/subject.py
class Image(ABC):
    @abstractmethod
    def display(self) -> str:
        pass


# ---- proxy/real_subject.py
class RealImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self._load()

    def _load(self):
        print(f"  RealImage: carregando {self.filename} do disco...")

    def display(self) -> str:
        return f"  RealImage: exibindo {self.filename}"


# ---- proxy/proxy.py
class ProxyImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self._real_image = None

    def display(self) -> str:
        if self._real_image is None:
            self._real_image = RealImage(self.filename)
        return self._real_image.display()


# ---- proxy/main.py
def proxy_demo():
    print("=== PROXY (Virtual/Lazy Loading) ===")
    img = ProxyImage("foto_grande.jpg")
    print("  Proxy criado, imagem ainda não carregada")
    print(img.display())
    print(img.display())  # segundo acesso: sem recarga
    print()


proxy_demo()

# =============================================================================
# FLYWEIGHT
# =============================================================================
#
# flyweight/
# ├── flyweight.py
# ├── flyweight_factory.py
# └── main.py
#
# =============================================================================


# ---- flyweight/flyweight.py
class TreeType:
    """Flyweight: estado intrínseco compartilhado"""

    def __init__(self, name: str, color: str, texture: str):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, x: int, y: int) -> str:
        return f"  Árvore [{self.name}/{self.color}] em ({x},{y})"


# ---- flyweight/flyweight_factory.py
class TreeFactory:
    _tree_types = {}

    @classmethod
    def get_tree_type(cls, name, color, texture) -> TreeType:
        key = (name, color, texture)
        if key not in cls._tree_types:
            cls._tree_types[key] = TreeType(name, color, texture)
            print(f"  Factory: criando novo tipo {key}")
        return cls._tree_types[key]

    @classmethod
    def count(cls) -> int:
        return len(cls._tree_types)


class Tree:
    """Contexto: estado extrínseco único por instância"""

    def __init__(self, x: int, y: int, tree_type: TreeType):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self) -> str:
        return self.tree_type.draw(self.x, self.y)


# ---- flyweight/main.py
def flyweight_demo():
    print("=== FLYWEIGHT ===")
    forest = []
    import random

    types = [
        ("Carvalho", "verde", "rugosa"),
        ("Pinheiro", "verde-escuro", "suave"),
        ("Carvalho", "verde", "rugosa"),
    ]
    for i, (name, color, texture) in enumerate(types):
        t = TreeFactory.get_tree_type(name, color, texture)
        forest.append(Tree(i * 10, i * 5, t))

    for tree in forest:
        print(tree.draw())
    print(f"  Tipos únicos criados: {TreeFactory.count()}, Árvores: {len(forest)}")
    print()


flyweight_demo()

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
