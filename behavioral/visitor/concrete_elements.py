from element import ASTNode
from visitor import ASTVisitor


class NumberNode(ASTNode):
    def __init__(self, value: float):
        self.value = value

    def accept(self, visitor: ASTVisitor):
        return visitor.visit_number(self)


class AddNode(ASTNode):
    def __init__(self, left: ASTNode, right: ASTNode):
        self.left = left
        self.right = right

    def accept(self, visitor: ASTVisitor):
        return visitor.visit_add(self)


class MultiplyNode(ASTNode):
    def __init__(self, left: ASTNode, right: ASTNode):
        self.left = left
        self.right = right

    def accept(self, visitor: "ASTVisitor"):
        return visitor.visit_multiply(self)
