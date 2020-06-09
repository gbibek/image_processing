from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage, qRed, qGreen, qBlue
import sys

image_name = "risk_math.jpg"


def GetChangedFormat(org_img, format):
    return org_img.convertToFormat(format)


def ShowPixel(img):

    for row in range(1, img.height()):
        line = img.constScanLine(row)
        for col in range(1, img.width()):
            print(line)
            exit()


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        # open image
        img = QImage(image_name)
        self.show_image(img, "histogram pic")
       # self.show_image(duplicate_img, "duplicate pic")

    def show_image(self, img, title):

        self.setWindowTitle(title)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        lay = QVBoxLayout(self.central_widget)
        label = QLabel(self)
        # displaying image
        duplicate_img = GetChangedFormat(img, QImage.Format_Grayscale8)
        # ShowPixel(duplicate_img)
        pixmap = QPixmap.fromImage(duplicate_img)
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())
        lay.addWidget(label)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    app.exec_()
    # sys.exit(app.exec_())
