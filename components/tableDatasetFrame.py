from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QFrame, QVBoxLayout
from src.components.folderDropWidget import FolderDropWidget
from PyQt6.QtCore import Qt, QPropertyAnimation, QRect
from src.helpers.functions import propertyAnimation


class TableDatasetFrame(QWidget):
    def __init__(self, *args, **kwargs):
        pos = kwargs.pop("pos", None)
        size = (1580, 900)
        super().__init__(*args, **kwargs)

        self.mainFrame = QFrame(self)
        self.mainFrame.resize(*size)
        if pos:
            self.move(*pos)

        self.setStyleSheet("border: 1px solid rgb(92, 92, 92);")
        self.setGeometry(QRect(*pos, *size))

        sampleLabel = QLabel("Tabular Dataset Page", self)
        sampleLabel.resize(*size)
        sampleLabel.setStyleSheet("font-size:32px; border: none;")
        sampleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mainFrameOpenAnimation = propertyAnimation(self, 100, b"geometry", QRect(*pos, *size),
                                                        QRect(205, 20, *size))
        self.mainFrameCloseAnimation = propertyAnimation(self, 100, b"geometry", QRect(205, 20, *size),
                                                         QRect(*pos, *size))

    def openAnimation(self):
        self.mainFrameOpenAnimation.start()

    def closeAnimation(self):
        self.mainFrameCloseAnimation.start()
