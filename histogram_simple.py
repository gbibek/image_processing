from PyQt5.QtGui import QImage, qGray

# read jpg image and convert it to grey scale.
grey_img = QImage("test_img.jpg").convertToFormat(QImage.Format_Grayscale8)

# read image height and width
img_height = grey_img.height()
img_width = grey_img.width()

# loop over and access each pixel's grey scale.
for row in range(0, img_height):
    for col in range(0, img_width):
        gray_val = qGray(grey_img.pixel(col, row))
