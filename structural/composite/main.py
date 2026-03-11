from leaf import File
from composite import Directory


def composite_demo():
    print("=== COMPOSITE ===")
    root = Directory("projeto")
    src = Directory("src")
    src.add(File("main.py", 10))
    src.add(File("utils.py", 5))
    tests = Directory("tests")
    tests.add(File("test_main.py", 8))
    root.add(src)
    root.add(tests)
    root.add(File("README.md", 2))

    print(root.display())
    print(f"  Tamanho total: {root.size()}kb")
    print()


if __name__ == "__main__":
    composite_demo()
