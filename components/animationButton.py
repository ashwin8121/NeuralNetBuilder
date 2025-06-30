from PyQt6.QtCore import QPropertyAnimation, QRect, Qt, QEasingCurve
from PyQt6.QtWidgets import QPushButton
from src.styles import animatedButtonStyle

class AnimatedButton(QPushButton):
    def __init__(self, *args, **kwargs):
        self.xy = kwargs.pop("xy")
        super().__init__(*args, **kwargs)
        self.resize(300, 50)
        self.setStyleSheet(animatedButtonStyle)
        self.buttonOpenAnimation = QPropertyAnimation(self, b"geometry")
        self.buttonCloseAnimation = QPropertyAnimation(self, b"geometry")
        self.originalText = self.text()

    def openAnimation(self):
        return
        # self.setText(self.originalText)
        self.buttonOpenAnimation.setDuration(100)
        self.buttonOpenAnimation.setStartValue(QRect(*self.xy, 70, 50))
        self.buttonOpenAnimation.setEndValue(QRect(*self.xy, 300, 50))
        self.buttonOpenAnimation.start()

    def closeAnimation(self):
        return
        self.buttonCloseAnimation.setDuration(100)
        self.buttonCloseAnimation.setStartValue(QRect(*self.xy, 300, 50))
        self.buttonCloseAnimation.setEndValue(QRect(*self.xy, 70, 50))
        self.buttonCloseAnimation.start()
        # self.setText("")
