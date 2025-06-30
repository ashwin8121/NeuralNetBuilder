from PyQt6.QtCore import QPropertyAnimation
from PyQt6.QtWidgets import QWidget


def propertyAnimation(widget: QWidget, duration: int, property: bytes, startVal=None, endVal=None):
    anim = QPropertyAnimation(widget, property)
    anim.setDuration(duration)
    anim.setStartValue(startVal)
    anim.setEndValue(endVal)
    return anim

