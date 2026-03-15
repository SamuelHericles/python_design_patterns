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
