from PyQt5.QtGui import qGray


def ShowPixelValue(img):

    # read image height and width
    img_height = img.height()
    img_width = img.width()

    # loop over and access each pixel's grey scale.
    for row in range(0, img_height):
        for col in range(0, img_width):
            gray_val = qGray(img.pixel(col, row))
            print("(", row, ",", col, ") = ", gray_val)


def GetChangedFormat(org_img, format):
    return org_img.convertToFormat(format)


def ConvertQImageTo2D(image):
    image_2d = []
    # loop over and access each pixel's grey scale.
    for row in range(0, image.height()):
        collect_intensity = []
        for col in range(0, image.width()):
            gray = qGray(image.pixel(col, row))
            collect_intensity.append(gray)
        image_2d.append(collect_intensity)
    return image_2d
