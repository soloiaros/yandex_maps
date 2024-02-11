import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from io import BytesIO
import requests
from PyQt5.QtGui import QPixmap
from get_image import get_image
from get_coords_from_address import coords_from_address
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/first_ui.ui', self)
        self.setWindowTitle('YandexMaps')
        self.map_is_displayed = False
        self.pushButton.clicked.connect(self.show_map)
        self.buttonGroup.buttonClicked.connect(self.change_appearance)
        self.pushButton_2.clicked.connect(self.address_search)
        self.mode = 'map'
        self.coords = None
        self.spn = 0.002

    def show_map(self, coords=None, point=False):
        self.map_is_displayed = True
        if not coords:
            self.coords = (self.lineEdit.text(), self.lineEdit_2.text())
        else:
            self.coords = coords
        get_image(self.coords, self.spn, self.mode, point=point)
        pixmap = QPixmap('data/map.png')
        self.label.setPixmap(pixmap)

    def update_map(self):
        get_image(self.coords, self.spn, self.mode)
        pixmap = QPixmap('data/map.png')
        self.label.setPixmap(pixmap)

    def address_search(self):
        address = self.lineEdit_3.text()
        self.show_map(coords_from_address(address), True)

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

    def change_appearance(self):
        if self.mapRButton.isChecked():
            self.mode = 'map'
        elif self.satRButton.isChecked():
            self.mode = 'sat'
        else:
            self.mode = 'skl'

        if self.map_is_displayed:
            self.update_map()


def exception_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.excepthook = exception_hook
    ex.show()
    sys.exit(app.exec_())