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
