import sys
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QProgressBar, QApplication
from PyQt6.QtCore import Qt, QSize


class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setFixedSize(QSize(300, 100))
        self.setStyleSheet("background-color: rgb(50, 50, 50); color: white; font-family: roboto mono; font-size: 14px;")

        layout = QVBoxLayout()

        label = QLabel("Loading Dataset... Please Wait")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        self.progressbar = QProgressBar()
        self.progressbar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progressbar.setRange(0, 0)
        layout.addWidget(self.progressbar)

        self.setLayout(layout)
