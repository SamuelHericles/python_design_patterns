from subject import Image
from real_subject import RealImage


class ProxyImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self._real_image = None

    def display(self) -> str:
        if self._real_image is None:
            self._real_image = RealImage(self.filename)
        return self._real_image.display()
