import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from io import BytesIO
import requests
from PyQt5.QtGui import QPixmap
from get_image import get_image
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/first_ui.ui', self)
        self.setWindowTitle('YandexMaps')
        self.pushButton.clicked.connect(self.show_map)
        self.coords = None
        self.spn = 0.002

    def show_map(self):
        coords = (self.lineEdit.text(), self.lineEdit_2.text())
        self.coords = coords
        get_image(self.coords, self.spn)
        pixmap = QPixmap('data/map.png')
        self.label.setPixmap(pixmap)

    def update_map(self):
        get_image(self.coords, self.spn)
        pixmap = QPixmap('data/map.png')
        self.label.setPixmap(pixmap)

    def keyPressEvent(self, event):
        # Приближение/отдаление
        if event.key() == Qt.Key_PageUp:
            self.spn = max([0.002, self.spn - 0.005])
            self.update_map()
        if event.key() == Qt.Key_PageDown:
            self.spn = min([0.050, self.spn + 0.005])
            self.update_map()

        # Перемещение по карте (Alt+стрелка)
        if int(event.modifiers()) == Qt.AltModifier:
            if event.key() == Qt.Key_Up:
                self.coords = (self.coords[0], str(float(self.coords[1]) + 0.0005))
                self.update_map()
            if event.key() == Qt.Key_Down:
                self.coords = (self.coords[0], str(float(self.coords[1]) - 0.0005))
                self.update_map()
            if event.key() == Qt.Key_Left:
                self.coords = (str(float(self.coords[0]) - 0.0005), self.coords[1])
                self.update_map()
            if event.key() == Qt.Key_Right:
                self.coords = (str(float(self.coords[0]) + 0.0005), self.coords[1])
                self.update_map()


def exception_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.excepthook = exception_hook
    ex.show()
    sys.exit(app.exec_())