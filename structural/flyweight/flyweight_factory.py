from flyweight import TreeType


class TreeFactory:
    _tree_types = {}

    @classmethod
    def get_tree_type(cls, name, color, texture) -> TreeType:
        key = (name, color, texture)
        if key not in cls._tree_types:
            cls._tree_types[key] = TreeType(name, color, texture)
            print(f"  Factory: criando novo tipo {key}")
        return cls._tree_types[key]

    @classmethod
    def count(cls) -> int:
        return len(cls._tree_types)


class Tree:
    """Contexto: estado extrínseco único por instância"""

    def __init__(self, x: int, y: int, tree_type: TreeType):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self) -> str:
        return self.tree_type.draw(self.x, self.y)
