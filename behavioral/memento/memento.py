class EditorMemento:
    def __init__(self, content: str, cursor: int):
        self._content = content
        self._cursor = cursor

    @property
    def content(self):
        return self._content

    @property
    def cursor(self):
        return self._cursor
