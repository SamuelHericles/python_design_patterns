from comand import Command
from receiver import TextEditor


class WriteCommand(Command):
    def __init__(self, editor: TextEditor, text: str):
        self._editor = editor
        self._text = text

    def execute(self):
        self._editor.write(self._text)

    def undo(self):
        self._editor.delete(len(self._text))
