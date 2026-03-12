from flyweight_factory import TreeFactory, Tree


def flyweight_demo():
    print("=== FLYWEIGHT ===")
    forest = []

    types = [
        ("Carvalho", "verde", "rugosa"),
        ("Pinheiro", "verde-escuro", "suave"),
        ("Carvalho", "verde", "rugosa"),
    ]
    for i, (name, color, texture) in enumerate(types):
        t = TreeFactory.get_tree_type(name, color, texture)
        forest.append(Tree(i * 10, i * 5, t))

    for tree in forest:
        print(tree.draw())
    print(f"  Tipos únicos criados: {TreeFactory.count()}, Árvores: {len(forest)}")
    print()


if __name__ == "__main__":
    flyweight_demo()
