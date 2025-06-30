import os

import matplotlib.pyplot as plt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QFrame, QWidget, QVBoxLayout, QLabel, QProgressBar, QScrollArea, QGridLayout
from PyQt6.QtCore import Qt, QSize
from PIL.Image import fromarray
from PIL.ImageQt import toqpixmap, ImageQt
import random as rn
import numpy as np

class ImagesDisplayFrame(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setFixedSize(QSize(760, 760))
        # self.setStyleSheet("background-color: rgb(50, 50, 50); color: white; font-family: roboto mono; font-size: 14px;")

        self.frame = QFrame(self)
        self.frame.move(5, 5)
        self.frame.resize(750, 750)
        self.frame.setStyleSheet("border: 1px solid white; ")
        self.layout = QGridLayout()
        self.frame.setLayout(self.layout)

    def displayImages(self, images):
        savedImages = []
        for i, img in enumerate(images[:9]):
            img = img.astype(np.uint8)
            imgName = f"C:\\Users\\ashwi\AppData\\Local\\Temp\\{''.join([str(rn.randint(0, 9)) for _ in range(7)]) + '.jpg'}"
            # savedImages.append((imgName))
            if img.shape[2] == 1:
                img = img.reshape(*img.shape[:2]) #
                plt.imsave(imgName, img, cmap="grey")
            else:
                plt.imsave(imgName, img)

            label = QLabel()
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            label.setPixmap(QPixmap(imgName))
            label.resize(240, 240)
            label.setStyleSheet("border: none;")
            self.layout.addWidget(label, i // 3, i % 3)
            # img = img / 255
            # plt.imshow(img)
            # plt.show()
            # p
            os.remove(imgName)
        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()

