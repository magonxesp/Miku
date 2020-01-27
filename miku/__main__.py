# import pygame
# import miku
# import miku.sprite
import sys
from PySide2.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsView, QOpenGLWidget
from PySide2.QtCore import Qt
from PySide2.QtGui import QPaintEvent, QPainter, QOpenGLWindow
from miku.objects import Miku


app = QApplication(sys.argv)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.miku = Miku()

    def paintEvent(self, event: QPaintEvent):
        renderer = QPainter(self)
        self.miku.update()
        self.miku.render(renderer)


if __name__ == "__main__":
    window = MainWindow()
    scene = QGraphicsScene(window)

    scene.

    view = QGraphicsView(scene)
    view.showFullScreen()
    #window.showFullScreen()
    sys.exit(app.exec_())
