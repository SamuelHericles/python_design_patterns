from concrete_elements import (
    MultiplyNode,
    AddNode,
    NumberNode,
)
from concrete_visitors import (
    PrinterVisitor,
    EvaluatorVisitor,
)

# AST = Abstract sintax tree - mathmatics expresions


def visitor_demo():
    print("=== VISITOR ===")

    # AST para: (3 + 4) * 2
    tree = MultiplyNode(
        AddNode(
            NumberNode(3),
            NumberNode(4),
        ),
        NumberNode(2),
    )
    printer = PrinterVisitor()
    evaluator = EvaluatorVisitor()
    expr = tree.accept(printer)
    result = tree.accept(evaluator)
    print(f"  Expressão: {expr} = {result}")
    print()


if __name__ == "__main__":
    visitor_demo()
