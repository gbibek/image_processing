from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication, QWidget, QVBoxLayout, QGridLayout, QScrollArea
from PyQt5.QtGui import QPixmap, QImage, qRed, qGreen, qBlue, qGray, QColor
import sys
from IntensityTransformation import *

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
    def __init__(self, image):
        super().__init__()
        self.img_intensity = []

        # open image
        self.initial_image = image
        self.img_height = self.initial_image.height()
        self.img_width = self.initial_image.width()

        # create scroll object
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        # create widget and set grid layout to it
        self.my_widget = QWidget()
        self.my_grid = QGridLayout()
        self.my_widget.setLayout(self.my_grid)
        # set my_widget to scroll
        self.scroll.setWidget(self.my_widget)

        img = GetChangedFormat(self.initial_image, QImage.Format_Grayscale8)
        self.CollectImageGreyIntensity()
        img_neg = self.ManipulatePixel(img, Negative)
        intensity_tranformation = "power"
        if intensity_tranformation == "log":
            img_log_10 = self.ManipulatePixel(img, Log, 10)
            img_log_25 = self.ManipulatePixel(img, Log, 25)
            img_log_50 = self.ManipulatePixel(img, Log, 50)
            img_log_75 = self.ManipulatePixel(img, Log, 70)
            img_log_100 = self.ManipulatePixel(img, Log, 100)
            self.show_image(
                self.initial_image, img, img_neg,
                img_log_10, img_log_25, img_log_50,
                img_log_75, img_log_100)
        if intensity_tranformation == "power":
            tmp_img = self.ManipulatePixel(img, Log, 10)
            # tends to be brigher
            img_log_10 = self.ManipulatePixel(tmp_img, Power, 50, 0.04)
            # closer to tmp_img
            img_log_25 = self.ManipulatePixel(tmp_img, Power, 1, 1)
            # tends to be darker
            img_log_50 = self.ManipulatePixel(tmp_img, Power, 50, 2.5)
            #img_log_75 = self.ManipulatePixel(img, Power, 50, 5)
            self.show_image(
                self.initial_image, tmp_img,
                img_log_10, img_log_25, img_log_50)
        layout = QVBoxLayout(self)
        layout.addWidget(self.scroll)

    def show_image(self, *images):
        index_x = 1
        index_y = 1
        for image in images:
            self.add_image_to_widget(image, index_x, index_y)
            index_y += 1
            if index_y > 2:
                index_x += 1
                index_y = 1

    def add_image_to_widget(self, img, x, y):
        label = QLabel()
        label.setPixmap(QPixmap.fromImage(img))
        self.my_grid.addWidget(label, x, y)

    def ManipulatePixel(self, img, func,  *scale):
        ret_img = QImage(img)
        computed_intensity = []
        # loop over and access each pixel's grey scale.
        if len(scale) == 0:
            computed_intensity = func(self.img_intensity)
        elif len(scale) == 1:
            computed_intensity = func(self.img_intensity, scale[0])
        elif len(scale) == 2:
            computed_intensity = func(self.img_intensity, scale[0], scale[1])

        for row in range(len(computed_intensity)):
            for col in range(len(computed_intensity[row])):
                val = computed_intensity[row][col]
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
    # open image
    img = QImage(image_name)

    window = Menu(img)
    window.setGeometry(500, 100, img.width() + 100, 500)
    window.setWindowTitle("Display process images")
    window.show()
    sys.exit(app.exec_())
    # sys.exit(app.exec_())
