import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import *
from UI import Ui_MainWindow
import requests


class MyApplication(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.scale = '0.3'
        self.x_coords = 37.622504
        self.y_coords = 55.753215
        self.maps_api_server = "https://static-maps.yandex.ru/1.x/"
        self.painter = QPainter()
        #self.pushButton_Back.clicked.connect(self.back)
        #self.pushButton_Minus.clicked.connect(self.minus)
        #self.pushButton_Plus.clicked.connect(self.plus)
        #self.pushButton_Search.clicked.connect(self.search)
        self.update()

    def update(self):
        maps_params = {
            "ll": ','.join([str(self.x_coords), str(self.y_coords)]),
            "l": 'map',
            "spn": ','.join([self.scale, self.scale])
        }
        maps_response = requests.get(self.maps_api_server, params=maps_params)
        map_file = "map.png"
        try:
            with open(map_file, "wb") as file:
                file.write(maps_response.content)
        except IOError as ex:
            print("Ошибка записи временного файла:", ex)
            sys.exit(2)
        self.pixmap = QPixmap('map.png')
        self.label.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    application = MyApplication()
    application.show()
    sys.exit(app.exec_())
