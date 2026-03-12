# =============================================================================
# GOF - GANG OF FOUR - 23 DESIGN PATTERNS IN PYTHON
# =============================================================================
from abc import ABC, abstractmethod


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

from typing import Iterator as TypingIterator, Generic, TypeVar

T = TypeVar("T")


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
# TEMPLATE METHOD
# =============================================================================
#
# template_method/
# ├── abstract_class.py
# ├── concrete_classes.py
# └── main.py
#
# =============================================================================


# ---- template_method/abstract_class.py
class DataMiner(ABC):
    def mine(self, path: str) -> dict:
        """Template method"""
        raw = self.extract_data(path)
        parsed = self.parse_data(raw)
        analysis = self.analyze_data(parsed)
        self.send_report(analysis)
        return analysis

    @abstractmethod
    def extract_data(self, path: str) -> str:
        pass

    @abstractmethod
    def parse_data(self, raw: str) -> list:
        pass

    def analyze_data(self, data: list) -> dict:
        return {"count": len(data), "sample": data[:2]}

    def send_report(self, analysis: dict):
        print(f"  Relatório: {analysis}")


# ---- template_method/concrete_classes.py
class CSVMiner(DataMiner):
    def extract_data(self, path: str) -> str:
        return "a,b,c\n1,2,3\n4,5,6"

    def parse_data(self, raw: str) -> list:
        lines = raw.split("\n")
        headers = lines[0].split(",")
        return [dict(zip(headers, l.split(","))) for l in lines[1:] if l]


class JSONMiner(DataMiner):
    def extract_data(self, path: str) -> str:
        return '[{"id":1,"val":"x"},{"id":2,"val":"y"}]'

    def parse_data(self, raw: str) -> list:
        import json

        return json.loads(raw)


# ---- template_method/main.py
def template_method_demo():
    print("=== TEMPLATE METHOD ===")
    print("  CSV Miner:")
    CSVMiner().mine("data.csv")
    print("  JSON Miner:")
    JSONMiner().mine("data.json")
    print()


template_method_demo()


# =============================================================================
# VISITOR
# =============================================================================
#
# visitor/
# ├── visitor.py
# ├── concrete_visitors.py
# ├── element.py
# ├── concrete_elements.py
# └── main.py
#
# =============================================================================


# ---- visitor/element.py
class ASTNode(ABC):
    @abstractmethod
    def accept(self, visitor: "ASTVisitor"):
        pass


# ---- visitor/concrete_elements.py
class NumberNode(ASTNode):
    def __init__(self, value: float):
        self.value = value

    def accept(self, visitor: "ASTVisitor"):
        return visitor.visit_number(self)


class AddNode(ASTNode):
    def __init__(self, left: ASTNode, right: ASTNode):
        self.left = left
        self.right = right

    def accept(self, visitor: "ASTVisitor"):
        return visitor.visit_add(self)


class MultiplyNode(ASTNode):
    def __init__(self, left: ASTNode, right: ASTNode):
        self.left = left
        self.right = right

    def accept(self, visitor: "ASTVisitor"):
        return visitor.visit_multiply(self)


# ---- visitor/visitor.py
class ASTVisitor(ABC):
    @abstractmethod
    def visit_number(self, node: NumberNode):
        pass

    @abstractmethod
    def visit_add(self, node: AddNode):
        pass

    @abstractmethod
    def visit_multiply(self, node: MultiplyNode):
        pass


# ---- visitor/concrete_visitors.py
class EvaluatorVisitor(ASTVisitor):
    def visit_number(self, node: NumberNode):
        return node.value

    def visit_add(self, node: AddNode):
        return node.left.accept(self) + node.right.accept(self)

    def visit_multiply(self, node: MultiplyNode):
        return node.left.accept(self) * node.right.accept(self)


class PrinterVisitor(ASTVisitor):
    def visit_number(self, node: NumberNode):
        return str(node.value)

    def visit_add(self, node: AddNode):
        return f"({node.left.accept(self)} + {node.right.accept(self)})"

    def visit_multiply(self, node: MultiplyNode):
        return f"({node.left.accept(self)} * {node.right.accept(self)})"


# ---- visitor/main.py
def visitor_demo():
    print("=== VISITOR ===")
    # AST para: (3 + 4) * 2
    tree = MultiplyNode(AddNode(NumberNode(3), NumberNode(4)), NumberNode(2))
    printer = PrinterVisitor()
    evaluator = EvaluatorVisitor()
    expr = tree.accept(printer)
    result = tree.accept(evaluator)
    print(f"  Expressão: {expr} = {result}")
    print()


visitor_demo()

# =============================================================================
# FIM - 23 PADRÕES GOF IMPLEMENTADOS
# =============================================================================
