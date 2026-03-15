from memento import EditorMemento
from originator import CodeEditor
from typing import List


class EditorHistory:
    def __init__(self, editor: CodeEditor):
        self._editor = editor
        self._history: List[EditorMemento] = []

    def backup(self):
        self._history.append(self._editor.save())

    def undo(self):
        if self._history:
            self._editor.restore(self._history.pop())
