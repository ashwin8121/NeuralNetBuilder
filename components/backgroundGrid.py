from PyQt6.QtWidgets import QWidget, QFrame, QLabel
from PyQt6.QtCore import Qt


class BackgroundGrid(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setParent(parent)
        self.gridLabel = QLabel(self)
        self.gridLabel.setStyleSheet("background-color: white")