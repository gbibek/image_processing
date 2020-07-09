from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout, QGridLayout, QScrollArea
from PyQt5.QtGui import QPixmap


class CollectQImage(QWidget):
    def __init__(self):
        super().__init__()
        # create scroll object
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        # create widget and set grid layout to it
        self.my_widget = QWidget()
        self.my_grid = QGridLayout()
        self.my_widget.setLayout(self.my_grid)
        # set my_widget to scroll
        self.scroll.setWidget(self.my_widget)

    def add_images_to_layout(self, images):
        index_x = 1
        index_y = 1
        for image in images:
            self.add_image_to_widget(image, index_x, index_y)
            index_y += 1
            if index_y > 2:
                index_x += 1
                index_y = 1
        layout = QVBoxLayout(self)
        layout.addWidget(self.scroll)

    def dispaly(self, width):
        self.setGeometry(500, 100, width + 100, 500)
        self.setWindowTitle("Display process images")
        self.show()

    def add_image_to_widget(self, img, x, y):
        label = QLabel()
        label.setPixmap(QPixmap.fromImage(img))
        self.my_grid.addWidget(label, x, y)
