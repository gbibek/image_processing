from PyQt5.QtGui import QImage, QColor
from Util import *


class ManipulatePixel:
    def __init__(self, image):
        super().__init__()

        self.image = image
        self.image_2d = ConvertQImageTo2D(self.image)
        self.img_height = image.height()
        self.img_width = image.width()

    def GetManipulatedPixel(self, func,  *scale):
        ret_img = QImage(self.image)
        computed_intensity = []
        # loop over and access each pixel's grey scale.
        if len(scale) == 0:
            computed_intensity = func(self.image_2d)
        elif len(scale) == 1:
            computed_intensity = func(self.image_2d, scale[0])
        elif len(scale) == 2:
            computed_intensity = func(self.image_2d, scale[0], scale[1])
        # convert 2d array version of image to QImage
        for row in range(len(computed_intensity)):
            for col in range(len(computed_intensity[row])):
                val = computed_intensity[row][col]
                ret_img.setPixel(col, row, QColor(val, val, val).rgb())
        return ret_img
