from abstraction import Shape


class Circle(Shape):
    def __init__(self, renderer, x, y, radius):
        super().__init__(renderer)
        self.x, self.y, self.radius = x, y, radius

    def draw(self) -> str:
        return self._renderer.render_circle(self.x, self.y, self.radius)


class Square(Shape):
    def __init__(self, renderer, x, y, side):
        super().__init__(renderer)
        self.x, self.y, self.side = x, y, side

    def draw(self) -> str:
        return self._renderer.render_square(self.x, self.y, self.side)
