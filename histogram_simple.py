from PyQt5.QtGui import QImage, qGray

# read jpg image and convert it to grey scale.
grey_img = QImage("test_img.jpg").convertToFormat(QImage.Format_Grayscale8)

# print the pixel value of each pixel form the grey scale image.
img_height = grey_img.height()
img_width = grey_img.width()
print("height = ", img_height)
print("width  = ", img_width)

for row in range(0, img_height):
    for col in range(0, img_width):
        # works
        # gray_val = qGray(grey_img.pixel(col, row))
        # I have image of
        # height =  394
        # width  =  700
        # gives out of range error
        # QImage::pixel: coordinate (179,482) out of range
        gray_val = qGray(grey_img.pixel(row, col))
