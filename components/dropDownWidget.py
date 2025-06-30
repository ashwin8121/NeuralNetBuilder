from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QDialog, QFrame, QPushButton
from .draggable import DraggableButton
from PyQt6.QtCore import Qt, QSize, QPoint
from PyQt6.QtGui import QColor, QIcon
from src.styles.styles import draggableButtonStyle, draggableButtonStyleInsideDialog, dropDownCloseButtonStyle


class DropDownWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setParent(parent)
        self.mainFrame = QFrame(self)
        self.mainFrame.resize(QSize(200, 500))
        self.widgetsLayout = QVBoxLayout()
        dropDownCloseButton = QPushButton(self)
        dropDownCloseButton.setIcon(QIcon(r"assets/close-button-image.png"))
        dropDownCloseButton.setIconSize(QSize(12, 12))
        dropDownCloseButton.move(160, 10)
        dropDownCloseButton.resize(30, 30)
        dropDownCloseButton.clicked.connect(self.closeDropDownWidget)
        dropDownCloseButton.setStyleSheet(dropDownCloseButtonStyle)

    def closeDropDownWidget(self):
        self.parent().closeDropDownWidget()

    def addWidgetsToDropDown(self, widgets=[]):
        self.mainFrame.resize(200, self.heightVal)
        while self.widgetsLayout.count():
            self.widgetsLayout.removeWidget(self.widgetsLayout.itemAt(0).widget())
        lenWidgets = len(widgets)
        for widget in widgets:
            widget.setStyleSheet(draggableButtonStyleInsideDialog)
            self.widgetsLayout.addWidget(widget)
        self.mainFrame.setLayout(self.widgetsLayout)









