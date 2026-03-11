from typing import List
from component import FileSystemComponent


class Directory(FileSystemComponent):
    def __init__(self, name: str):
        super().__init__(name)
        self._children: List[FileSystemComponent] = []

    def add(self, component: FileSystemComponent):
        self._children.append(component)

    def remove(self, component: FileSystemComponent):
        self._children.remove(component)

    def display(self, indent: int = 0) -> str:
        result = "  " * indent + f"📁 {self.name}/\n"
        for child in self._children:
            result += child.display(indent + 1) + "\n"
        return result.rstrip()

    def size(self) -> int:
        return sum(child.size() for child in self._children)
