from PySide2.QtWidgets import QGraphicsPixmapItem, QStyleOptionGraphicsItem, QWidget
from PySide2.QtGui import QPixmap, QPainter, QCursor
from PySide2.QtCore import QPointF, QRectF, QSizeF, QPoint
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

    animations: dict

    def __init__(self):
        super().__init__()
        self.speed = 7
        self.direction = 'right'
        self.status = 'idle'
        self.animations = {
            'run': {
                'frames': 8,
                'right': {
                    'image_path': 'assets/miku/run_right.png',
                    'pixmap': None
                },
                'left': {
                    'image_path': 'assets/miku/run_left.png',
                    'pixmap': None
                }
            },
            'idle': {
                'frames': 10,
                'right': {
                    'image_path': 'assets/miku/idle_right.png',
                    'pixmap': None
                },
                'left': {
                    'image_path': 'assets/miku/idle_left.png',
                    'pixmap': None
                }
            }
        }

        self.load_pixmaps()
        self.set_status('idle', True)
        # set sprite position on current mouse position
        mouse = QCursor.pos()
        self.position.setX(mouse.x())
        self.position.setY(mouse.y())

    def load_pixmaps(self):
        for animation in self.animations:
            for key in self.animations[animation]:
                if key != 'frames':
                    path = os.path.join(os.path.dirname(__file__), self.animations[animation][key]['image_path'])
                    pixmap = QPixmap()
                    pixmap.load(path)
                    self.animations[animation][key]['pixmap'] = pixmap

    def set_status(self, status, force=False):
        if self.status != status or force:
            self.status = status
            self.set_sprite_pixmap(self.status, self.direction)

    def set_direction(self, direction, force=False):
        if self.direction != direction or force:
            self.direction = direction
            self.set_sprite_pixmap(self.status, self.direction)

    def set_sprite_pixmap(self, animation: str, direction: str):
        pixmap = self.animations[animation][direction]['pixmap']
        self._frames = self.animations[animation]['frames']
        self.setPixmap(pixmap)
        self.reset()

    def is_mouse_reached(self, mouse: QPoint):
        x = self.position.x()
        y = self.position.y()
        image_x = self.position.x() + (self.pixmap().width() / self._frames)
        image_y = self.position.y() + (self.pixmap().height() / self._frames)

        if (mouse.x() >= x and mouse.x() <= image_x) and (mouse.y() >= y and mouse.y() <= image_y):
            return True

        return False

    def follow_mouse(self, mouse: QPoint):
        x = self.position.x()
        y = self.position.y()

        if mouse.x() > x:
            x += self.speed
            self.set_direction('right')
        elif mouse.x() < x:
            x -= self.speed
            self.set_direction('left')

        if mouse.y() > y:
            y += self.speed
        elif mouse.y() < y:
            y -= self.speed

        self.position.setX(x)
        self.position.setY(y)

    def tick(self):
        # get the current mouse position on screen
        mouse = QCursor.pos()

        if self.is_mouse_reached(mouse) is False:
            self.follow_mouse(mouse)
            self.set_status('run')
        else:
            self.set_status('idle')
