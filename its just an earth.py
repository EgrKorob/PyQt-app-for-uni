import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Настройте графический интерфейс приложения."""
        self.setGeometry(300, 300, 1000, 500)
        self.setWindowTitle("Пример QLabel")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        hello_label = QLabel(self)
        hello_label.setText('Hello. \nIt is just an Earth')
        hello_label.move(105, 15)
        itsme_label = QLabel(self)
        itsme_label.setText('And we are just human')
        itsme_label.move(800, 20)
        image = 'images/pngwing.com.png'
        try:
            with open(image):
                world_label = QLabel(self)
                pixmap = QPixmap(image)
                world_label.setPixmap(pixmap)
                world_label.move(0, 0)
        except FileNotFoundError as error:
            print(f'Image not found.\nError:{error}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())