from comand import Command


class CommandHistory:
    def __init__(self):
        self._history = []

    def execute(self, command: Command):
        command.execute()
        self._history.append(command)

    def undo(self):
        if self._history:
            self._history.pop().undo()
