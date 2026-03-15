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
