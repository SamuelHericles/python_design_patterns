from subject import Image


class RealImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self._load()

    def _load(self):
        print(f"  RealImage: carregando {self.filename} do disco...")

    def display(self) -> str:
        return f"  RealImage: exibindo {self.filename}"
