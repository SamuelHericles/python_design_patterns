from component import FileSystemComponent


class File(FileSystemComponent):
    def __init__(self, name: str, size_kb: int):
        super().__init__(name)
        self._size = size_kb

    def display(self, indent: int = 0) -> str:
        return "  " * indent + f"📄 {self.name} ({self._size}kb)"

    def size(self) -> int:
        return self._size
