from component import TextFormatter


class PlainText(TextFormatter):
    def format(self, text: str) -> str:
        return text
