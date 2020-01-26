from PySide2.QtGui import QPainter
from typing import List


class RenderableObject:

    def start(self):
        pass

    def update(self):
        pass

    def render(self, renderer: QPainter):
        pass


class RenderGroup:

    _render_objects: List[RenderableObject]

    def __init__(self):
        pass

    def add(self, renderable: RenderableObject):
        self._render_objects.append(renderable)

    def start(self):
        for _object in self._render_objects:
            _object.start()

    def update(self):
        for _object in self._render_objects:
            _object.update()

    def render(self, renderer: QPainter):
        for _object in self._render_objects:
            _object.render(renderer)
