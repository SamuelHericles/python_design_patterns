from abstract_products import Button, Checkbox
from abstract_factory import GUIFactory


class WindowsButton(Button):
    def render(self) -> str:
        return "[Windows Button]"


class WindowsCheckbox(Checkbox):
    def render(self) -> str:
        return "[Windows Checkbox]"


class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()
