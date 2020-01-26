# import pygame
# import miku
# import miku.sprite
import sys
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtCore import Qt
from PySide2.QtGui import QPaintEvent, QPainter


app = QApplication(sys.argv)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)

    def paintEvent(self, event: QPaintEvent):
        renderer = QPainter()
        # TODO: render group


if __name__ == "__main__":
    window = MainWindow()
    window.showFullScreen()
    sys.exit(app.exec_())
