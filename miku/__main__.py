import sys
from PySide2.QtWidgets import QApplication, QGraphicsScene, QGraphicsView
from PySide2.QtCore import Qt, QThread
from PySide2.QtGui import QShowEvent
from miku.sprite import MikuSprite
import miku


class SceneUpdateThread(QThread):

    def __init__(self, _scene: QGraphicsScene):
        super().__init__()
        self.scene = _scene

    def run(self):
        while True:
            self.scene.update()
            self.msleep(int(1000 / 10))


class MyScene(QGraphicsScene):

    _update_thread: QThread

    def __init__(self):
        super().__init__()
        self.update_task = SceneUpdateThread(self)
        self.installEventFilter(self)


class GraphicsView(QGraphicsView):

    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)

    def showEvent(self, event: QShowEvent):
        self.setSceneRect(self.rect())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    scene = MyScene()
    # Sprite
    _miku = MikuSprite()

    scene.addItem(_miku)

    view = GraphicsView()
    # background transparent
    view.setAttribute(Qt.WA_TranslucentBackground, True)
    view.setAttribute(Qt.WA_NoSystemBackground, True)
    view.setStyleSheet("background: transparent; border: none;")
    # click through window
    view.setWindowFlags(Qt.FramelessWindowHint | Qt.X11BypassWindowManagerHint | Qt.WindowStaysOnTopHint | Qt.Tool)
    view.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
    view.setScene(scene)

    if sys.platform == miku.PLATFORM_MACOS:
        screen = app.primaryScreen()
        view.resize(screen.size().width(), screen.size().height())
        view.show()
    else:
        view.showFullScreen()

    scene.update_task.start()

    sys.exit(app.exec_())
