from implementation import Renderer


# ---- bridge/concrete_impl.py
class VectorRenderer(Renderer):
    def render_circle(self, x, y, radius) -> str:
        return f"Círculo vetorial em ({x},{y}) r={radius}"

    def render_square(self, x, y, side) -> str:
        return f"Quadrado vetorial em ({x},{y}) l={side}"


class RasterRenderer(Renderer):
    def render_circle(self, x, y, radius) -> str:
        return f"Círculo raster em ({x},{y}) r={radius}"

    def render_square(self, x, y, side) -> str:
        return f"Quadrado raster em ({x},{y}) l={side}"
