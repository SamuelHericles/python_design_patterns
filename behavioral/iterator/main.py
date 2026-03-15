from collection import BinaryTree


def iterator_demo():
    print("=== ITERATOR ===")
    tree = BinaryTree()
    for val in [5, 3, 7, 1, 4, 6, 8]:
        tree.insert(val)
    print(f"  In-order: {list(tree)}")
    print()


if __name__ == "__main__":
    iterator_demo()
