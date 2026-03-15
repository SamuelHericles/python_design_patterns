from visitor import ASTVisitor
from concrete_elements import AddNode, NumberNode, MultiplyNode


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
