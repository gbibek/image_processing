from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from PyQt5.QtGui import QImage
from IntensityTransformation import *
from ManipulatePixel import *
from CollectQImage import *
from Util import *

image_name = "test_img.jpg"

test = "log_"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # open image
    org_image = QImage(image_name)
    # grey image
    grey_img = GetChangedFormat(org_image, QImage.Format_Grayscale8)
    # collect images for displaying
    display_images = [org_image, grey_img]
    # negative
    display_images.append(ManipulatePixel(
        grey_img).GetManipulatedPixel(Negative))
    if test == "log":
        # log
        display_images.append(ManipulatePixel(
            grey_img).GetManipulatedPixel(Log, 10))
        display_images.append(ManipulatePixel(
            grey_img).GetManipulatedPixel(Log, 25))
        display_images.append(ManipulatePixel(
            grey_img).GetManipulatedPixel(Log, 50))
        display_images.append(ManipulatePixel(
            grey_img).GetManipulatedPixel(Log, 70))
        display_images.append(ManipulatePixel(
            grey_img).GetManipulatedPixel(Log, 100))
        # show image
        collect_image = CollectQImage()
        collect_image.add_images_to_layout(display_images)
        collect_image.dispaly(org_image.width())
    elif test == "power":
        # power
        display_images.append(ManipulatePixel(grey_img).GetManipulatedPixel(
            Power, 10))
        # tends to be brigher
        display_images.append(ManipulatePixel(grey_img).GetManipulatedPixel(
            Power, 50, 0.04))
        # closer to tmp_img
        display_images.append(ManipulatePixel(grey_img).GetManipulatedPixel(
            Power, 1, 1))
        # tends to be darker
        display_images.append(ManipulatePixel(grey_img).GetManipulatedPixel(
            Power, 50, 2.5))
        # show image
        collect_image = CollectQImage()
        collect_image.add_images_to_layout(display_images)
        collect_image.display(org_image.width())
    else:
        # show image
        collect_image = CollectQImage()
        collect_image.add_images_to_layout(display_images)
        collect_image.display(org_image.width())
    sys.exit(app.exec_())
