from abc import ABC, abstractmethod
from concrete_elements import (
    NumberNode,
    AddNode,
    MultiplyNode,
)


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
