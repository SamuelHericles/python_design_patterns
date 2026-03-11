from concrete_component import PlainText
from concrete_decorators import ItalicDecorator, UpperCaseDecorator, BoldDecorator


def decorator_demo():
    print("=== DECORATOR ===")
    text = PlainText()
    bold_italic = ItalicDecorator(BoldDecorator(text))
    upper_bold = UpperCaseDecorator(BoldDecorator(text))

    print(f"  Plain:       {text.format('hello world')}")
    print(f"  Bold+Italic: {bold_italic.format('hello world')}")
    print(f"  Upper+Bold:  {upper_bold.format('hello world')}")
    print()


if __name__ == "__main__":
    decorator_demo()
