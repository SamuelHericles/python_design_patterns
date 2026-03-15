from context import Sorter
from concrete_strategies import (
    BubbleSortStrategy,
    QuickSortStrategy,
    ReverseSortStrategy,
)


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


if __name__ == "__main__":
    strategy_demo()
