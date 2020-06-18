from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication, QWidget, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QPixmap, QImage, qRed, qGreen, qBlue, qGray, QColor
import sys
from IntensityTransformation import Negative

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


class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.img_intensity = []

        # open image
        self.initial_image = QImage(image_name)
        self.img_height = self.initial_image.height()
        self.img_width = self.initial_image.width()

        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.setGeometry(50, 50, 320, 200)
        img = GetChangedFormat(self.initial_image, QImage.Format_Grayscale8)
        self.CollectImageGreyIntensity()
        img_neg = self.ManipulatePixel(img)
        self.show_image("display_image", self.initial_image, img, img_neg)

    def show_image(self, title, *images):
        index_x = 1
        index_y = 1
        for image in images:
            self.add_image_to_widget(image, index_x, index_y)
            index_y += 1
            if index_y > 2:
                index_x += 1
                index_y = 1

        self.show()

    def add_image_to_widget(self, img, x, y):
        label = QLabel()
        label.setPixmap(QPixmap.fromImage(img))
        self.grid.addWidget(label, x, y)

    def ManipulatePixel(self, img):
        ret_img = QImage(img)
        # loop over and access each pixel's grey scale.
        neg_intensity = Negative(self.img_intensity)
        for row in range(len(neg_intensity)):
            for col in range(len(neg_intensity[row])):
                val = neg_intensity[row][col]
                ret_img.setPixel(col, row, QColor(val, val, val).rgb())
        return ret_img

    def CollectImageGreyIntensity(self):
        # loop over and access each pixel's grey scale.
        img = GetChangedFormat(self.initial_image, QImage.Format_Grayscale8)
        for row in range(0, self.img_height):
            collect_intensity = []
            for col in range(0, self.img_width):
                gray = qGray(img.pixel(col, row))
                collect_intensity.append(gray)
            self.img_intensity.append(collect_intensity)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    app.exec_()
    # sys.exit(app.exec_())
