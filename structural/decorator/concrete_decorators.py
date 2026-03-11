from decorator import TextDecorator


class BoldDecorator(TextDecorator):
    def format(self, text: str) -> str:
        return f"**{self._wrapped.format(text)}**"


class ItalicDecorator(TextDecorator):
    def format(self, text: str) -> str:
        return f"_{self._wrapped.format(text)}_"


class UpperCaseDecorator(TextDecorator):
    def format(self, text: str) -> str:
        return self._wrapped.format(text).upper()
