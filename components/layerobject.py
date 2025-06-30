from PyQt6.QtWidgets import (QWidget, QLabel, QCheckBox, QVBoxLayout, QFrame, QGraphicsDropShadowEffect)
from .draggable import DraggableObject
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QFont, QColor, QMoveEvent, QMouseEvent, QCursor
from src.helpers.layerProperties import properties
from src.styles.styles import layerObjectStyle, layerObjectSelectedStyle

# def print(*args, **kwargs):
#     pass

class LayerObject(QFrame, DraggableObject):
    selected = False
    prevMousePosition = None

    def __init__(self, layerText, layerName):
        super().__init__()
        self.layerName = layerName
        self.layerText = layerText
        self.config = {}
        self.mainLayout = QVBoxLayout()
        self.layerLabel = QLabel(layerText)
        self.layerLabel.setStyleSheet(layerObjectStyle)
        self.layerLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(self.layerLabel)
        self.setLayout(self.mainLayout)

    def openPropertyWindow(self):
        mainFrame = self.parent().parent().parent()
        mainFrame.openPropertyWindow(self)

    def mousePressEvent(self, event):
        if event.buttons() == Qt.MouseButton.RightButton :
            self.openPropertyWindow()

    def createConnection(self, layerObject1, layerObject2):
        mainFrame = self.parent().parent().parent()
        if (layerObject1, layerObject2) in mainFrame.connections:
            mainFrame.connections.remove((layerObject1, layerObject2))
            layerObject1.selected = False
            layerObject1.layerLabel.setStyleSheet(layerObjectStyle)
            layerObject2.selected = False
            layerObject2.layerLabel.setStyleSheet(layerObjectStyle)
            mainFrame.selection1 = None
            mainFrame.selection2 = None
            return

        mainFrame.connections.add((layerObject1, layerObject2))
        layerObject1.selected = False
        layerObject1.layerLabel.setStyleSheet(layerObjectStyle)
        layerObject2.selected = False
        layerObject2.layerLabel.setStyleSheet(layerObjectStyle)
        mainFrame.selection1 = None
        mainFrame.selection2 = None
        self.deselectionExecuted()



    def selectionExecuted(self):

        mainFrame = self.parent().parent().parent()
        if mainFrame.selection1 and mainFrame.selection2:
            print(1)
            return
        elif not mainFrame.selection1 and not mainFrame.selection2:
            print(2)
            mainFrame.selection1 = self  # if both are not selected, selection1 = self
        elif not mainFrame.selection1 and mainFrame.selection2:
            print(3)
            mainFrame.selection1 = mainFrame.selection2
            mainFrame.selection2 = None
        elif mainFrame.selection1 and not mainFrame.selection2:
            print(4)
            mainFrame.selection2 = self # if only selection1 is not selected, selection2 = self
            self.createConnection(mainFrame.selection1, mainFrame.selection2)
        else:
            print(5)



    def deselectionExecuted(self):
        # print(mainFrame.selection1, mainFrame.selection2)

        mainFrame = self.parent().parent().parent()
        if mainFrame.selection1 == self:
            mainFrame.selection1 = None
        if mainFrame.selection2 == self:
            mainFrame.selection2 = None

    def mouseReleaseEvent(self, event):

        if self.prevMousePosition:
            self.prevMousePosition = None
            return 
        mainFrame = self.parent().parent().parent()
        if mainFrame.selection1 and mainFrame.selection2:
            return
        if event.button() == Qt.MouseButton.LeftButton:
            if self.selected:
                self.layerLabel.setStyleSheet(layerObjectStyle)
                self.deselectionExecuted()
            else:
                self.layerLabel.setStyleSheet(layerObjectSelectedStyle)
                self.selectionExecuted()
            self.selected = not self.selected
        print(mainFrame.selection1.layerText if mainFrame.selection1 else None, mainFrame.selection2.layerText if mainFrame.selection2 else None)


    def deleteYourself(self):
        mainFrame = self.parent().parent().parent()
        mainFrame.selection1 = None
        self.deleteLater()

    def mouseMoveEvent(self, event):
        if not self.prevMousePosition:
            self.prevMousePosition = event.globalPosition().toPoint() - self.pos() - self.parent().mapToGlobal(self.parent().pos())
            return
        self.move(event.globalPosition().toPoint() - self.parent().mapToGlobal(self.parent().pos()) - self.prevMousePosition)


