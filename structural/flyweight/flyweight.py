class TreeType:
    """Flyweight: estado intrínseco compartilhado"""

    def __init__(self, name: str, color: str, texture: str):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, x: int, y: int) -> str:
        return f"  Árvore [{self.name}/{self.color}] em ({x},{y})"
