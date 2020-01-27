from miku.sprite import Sprite
from miku.render import RenderableObject
from PySide2.QtGui import QPainter


class Miku(RenderableObject):

    def __init__(self):
        self.sprite_idle_left = Sprite('assets/miku/idle_left.png', 10)
        self.sprite_idle_right = Sprite('assets/miku/idle_right.png', 10)
        self.sprite_run_left = Sprite('assets/miku/run_left.png', 8)
        self.sprite_run_right = Sprite('assets/miku/run_right.png', 8)

    def start(self):
        pass

    def update(self):
        self.sprite_idle_left.next_frame()

    def render(self, renderer: QPainter):
        self.sprite_idle_left.render(renderer)
