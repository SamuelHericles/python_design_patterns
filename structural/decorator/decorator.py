from component import TextFormatter


class TextDecorator(TextFormatter):
    def __init__(self, wrapped: TextFormatter):
        self._wrapped = wrapped

    def format(self, text: str) -> str:
        return self._wrapped.format(text)
