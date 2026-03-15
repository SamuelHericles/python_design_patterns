class TextEditor:
    def __init__(self):
        self._text = ""

    def write(self, text: str):
        self._text += text
        print(f"  Editor: escreveu '{text}'")

    def delete(self, count: int):
        removed = self._text[-count:]
        self._text = self._text[:-count]
        print(f"  Editor: deletou '{removed}'")
        return removed

    @property
    def text(self):
        return self._text
