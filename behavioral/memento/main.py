from originator import CodeEditor
from caretaker import EditorHistory


def memento_demo():
    print("=== MEMENTO ===")
    editor = CodeEditor()
    history = EditorHistory(editor)

    history.backup()
    editor.type("def hello():")
    history.backup()
    editor.type("\n    print('hi')")
    print(editor)

    history.undo()
    print(f"  Após undo: {editor}")
    print()


if __name__ == "__main__":
    memento_demo()
