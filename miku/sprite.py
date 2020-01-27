from PySide2.QtWidgets import QGraphicsPixmapItem, QStyleOptionGraphicsItem, QWidget, QGraphicsSceneMouseEvent
from PySide2.QtGui import QPixmap, QPainter
from PySide2.QtCore import QPointF, QRectF, QSizeF
import os


class Sprite(QGraphicsPixmapItem):

    _current_frame: float = 0
    _frames: int
    position: QPointF

    def __init__(self, sprite_image_path: str = "", frames: int = 0):
        super().__init__()
        self.position = QPointF()
        self.position.setX(0)
        self.position.setY(0)

        if sprite_image_path != "" and frames != 0:
            self.load(sprite_image_path, frames)

    def load(self, sprite_image_path: str, frames: int):
        path = os.path.join(os.path.dirname(__file__), sprite_image_path)
        image = QPixmap()
        image.load(path)
        self.setPixmap(image)
        self._frames = frames

    def next_frame(self):
        total_width = self.pixmap().width()
        frame_width = total_width / self._frames
        self._current_frame += frame_width

        if self._current_frame >= total_width:
            self._current_frame = 0

    def prev_frame(self):
        total_width = self.pixmap().width()
        frame_width = total_width / self._frames
        self._current_frame -= frame_width

        if self._current_frame <= 0:
            self._current_frame = frame_width

    def reset(self):
        self._current_frame = 0

    def boundingRect(self) -> QRectF:
        return QRectF(self.position, QSizeF(float(self.pixmap().width() / self._frames), float(self.pixmap().height())))

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget):
        self.tick()
        self.next_frame()
        frame_width = float(self.pixmap().width() / self._frames)
        rect = QRectF(self._current_frame, 0.0, frame_width, float(self.pixmap().height()))
        painter.drawPixmap(self.position, self.pixmap(), rect)

    # Sprite update
    def tick(self):
        pass


class MikuSprite(Sprite):

    def __init__(self):
        super().__init__()
        self.animations = {
            'run': {
                'frames': 8,
                'pixmap': None
            }
        }
