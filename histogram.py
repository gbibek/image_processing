from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication, QWidget, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QPixmap, QImage, qRed, qGreen, qBlue, qGray, QColor
import sys

image_name = "test_img.jpg"


def GetChangedFormat(org_img, format):
    return org_img.convertToFormat(format)


def ShowPixel(img):

    # read image height and width
    img_height = img.height()
    img_width = img.width()

    # loop over and access each pixel's grey scale.
    for row in range(0, img_height):
        for col in range(0, img_width):
            gray_val = qGray(img.pixel(col, row))
            print("(", row, ",", col, ") = ", gray_val)


def ManipulatePixel(img):
    ret_img = QImage(img)
    # read image height and width
    img_height = ret_img.height()
    img_width = ret_img.width()

    # loop over and access each pixel's grey scale.
    for row in range(0, img_height):
        for col in range(0, img_width):
            gray = qGray(img.pixel(col, row))*3.0
            ret_img.setPixel(col, row, QColor(gray, gray, gray).rgb())
    return ret_img


class Menu(QWidget):
    def __init__(self):
        super().__init__()
        # open image
        initial_image = QImage(image_name)
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.setGeometry(50, 50, 320, 200)
        self.show_image(initial_image, "display_pic")

    def show_image(self, initial_image, title):
        im2 = GetChangedFormat(initial_image, QImage.Format_Grayscale8)
        im3 = ManipulatePixel(im2)
        self.add_image_to_widget(initial_image, 1, 1)
        self.add_image_to_widget(im2, 2, 1)
        self.add_image_to_widget(im3, 1, 2)

        self.setWindowTitle(title)
        self.show()

    def add_image_to_widget(self, img, x, y):
        label = QLabel()
        label.setPixmap(QPixmap.fromImage(img))
        self.grid.addWidget(label, x, y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    app.exec_()
    # sys.exit(app.exec_())
