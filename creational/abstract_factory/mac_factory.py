# ---- abstract_factory/mac_factory.py
from abstract_products import Button, Checkbox
from abstract_factory import GUIFactory


class MacButton(Button):
    def render(self) -> str:
        return "(Mac Button)"


class MacCheckbox(Checkbox):
    def render(self) -> str:
        return "(Mac Checkbox)"


class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()
