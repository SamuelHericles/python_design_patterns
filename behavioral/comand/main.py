from concrete_commands import WriteCommand
from invoker import CommandHistory
from receiver import TextEditor


def command_demo():
    print("=== COMMAND ===")
    editor = TextEditor()
    history = CommandHistory()

    history.execute(WriteCommand(editor, "Olá "))
    history.execute(WriteCommand(editor, "mundo!"))
    print(f"  Texto: '{editor.text}'")
    history.undo()
    print(f"  Após undo: '{editor.text}'")
    print()


if __name__ == "__main__":
    command_demo()
