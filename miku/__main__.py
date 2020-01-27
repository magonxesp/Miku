import sys
from PySide2.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsView
from PySide2.QtCore import Qt, QEvent, QObject, QThread
from PySide2.QtGui import QMouseEvent
from miku.objects import Miku


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

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.MouseMove:
            print("mouse move!")

        return super().eventFilter(watched, event)

    def mouseMoveEvent(self, event: QMouseEvent):
        # print("Mouse move event!", event.x(), event.y())
        # print("Scene", self.scene().height(), self.scene().width())
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    scene = MyScene()
    miku = Miku()

    scene.addItem(miku.sprite_idle_right)

    view = GraphicsView()
    # background transparent
    view.setAttribute(Qt.WA_TranslucentBackground, True)
    view.setAttribute(Qt.WA_NoSystemBackground, True)
    view.setStyleSheet("background: transparent; border: none;")
    # click through window
    view.setWindowFlags(Qt.FramelessWindowHint | Qt.X11BypassWindowManagerHint | Qt.WindowStaysOnTopHint | Qt.Tool)
    view.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
    view.setScene(scene)
    view.showFullScreen()

    scene.update_task.start()

    sys.exit(app.exec_())
