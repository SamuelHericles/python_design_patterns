import copy
from prototype import Prototype


class Document(Prototype):
    def __init__(self, title: str, content: str, tags: list):
        self.title = title
        self.content = content
        self.tags = tags

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Document(title={self.title}, tags={self.tags})"
