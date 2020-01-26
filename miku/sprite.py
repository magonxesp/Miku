from miku.animation import MikuIdleAnimation, MikuRunAnimation
from PySide2.QtWidgets import QGraphicsItem
from PySide2.QtGui import QPixmap, QPainter
from PySide2.QtCore import QPoint
import os
from typing import List


class FrameList:

    def __init__(self, images: List[QPixmap]):
        self.frames = images
        self.index = 0

    def __len__(self):
        return len(self.frames)

    def next(self, offset=1, speed=1):
        if self.index < images_len:
            self.index += (offset * speed)

        if self.index >= images_len:
            self.index = 0

        return self.frames[int(self.index)]


class Sprite(QGraphicsItem):

    _image: QPixmap
    _current_frame: int = 0
    _frames: int
    position: QPoint

    def __init__(self, sprite_image_path: str, frames: int):
        super().__init__()
        path = os.path.join(os.path.dirname(__file__), sprite_image_path)
        self._image = QPixmap()
        self._image.load(path)
        self._frames = frames
        self.position = QPoint()

    def next_frame(self):
        total_width = self._image.width()
        frame_width = total_width / self._frames
        self._current_frame += frame_width

        if self._current_frame >= total_width:
            self._current_frame = 0

    def reset(self):
        self._current_frame = 0

    def render(self, renderer: QPainter):
        renderer.drawPixmap(self.position, self._image, self._current_frame, 0, self._image.width(), self._image.height())


class DirectionalSprite:

    _right: Sprite
    _left: Sprite
    _current_direction: str
    current_sprite: Sprite

    def __init__(self):
        pass

    def set_sprite(self, direction: str, sprite: Sprite):
        if direction == 'right':
            self._right = sprite
        elif direction == 'left':
            self._left = sprite

        self.current_sprite = sprite
        self._current_direction = direction

    def set_direction(self, direction: str):
        if self._current_direction == 'right':
            self._right = self.current_sprite
        elif self._current_direction == 'left':
            self._left = self.current_sprite

        if direction == 'right':
            self.current_sprite = self._right
        elif direction == 'left':
            self.current_sprite = self._left

        self._current_direction = direction
        self.current_sprite.reset()

    def render(self, renderer: QPainter):
        self._current_sprite.render(renderer)
