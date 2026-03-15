from abc import ABC, abstractmethod
from visitor import ASTVisitor


# AST = Abstract sintax tree
class ASTNode(ABC):
    @abstractmethod
    def accept(self, visitor: ASTVisitor):
        pass
