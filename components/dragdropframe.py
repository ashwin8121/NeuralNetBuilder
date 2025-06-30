import os

from PyQt6.QtWidgets import QFrame, QScrollArea, QWidget
from PyQt6.QtCore import Qt, QRect
from PyQt6.QtGui import QCursor, QPainter, QPen, QColor, QPainterPath, QFont
from .draggable import DraggableButton
from .layerobject import LayerObject
from random import randint, random


class DragDropFrame(QFrame):
    clickCount = 0
    prevMousePosition = None
    doubleClicked = False
    name = "DragDropFrame"
    lines = []
    startx = 0
    starty = 0
    r = g = b = 0

    updated = False
    modelLayers = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAcceptDrops(True)
        self.application = self.parent().parent()

        self.application.selections = set()
        self.selections = self.application.selections
        self.selectFrame = QFrame(self.application)
        self.selectFrame.setGeometry(QRect(self.startx, self.starty, 0, 0))
        self.selectFrame.setStyleSheet("background-color: rgba(34, 101, 220, 16); border: 1px solid rgb(34, 101, 220);")

    def dragEnterEvent(self, event):
        if self.application.running:
            return
        event.accept()

    def dropEvent(self, e):
        # s
        pos = e.position()
        x, y = int(pos.x()) + 10, int(pos.y()) + 10
        widget = e.source()

        if widget.insideDragDropArea:
            widget.move(x, y)
            e.accept()
            return

        text = widget.text()
        layerName = self.application.getLayerName(text)
        layerobject = LayerObject(text, layerName)

        layerobject.setParent(self)
        layerobject.insideDragDropArea = True
        layerobject.move(x, y)
        layerobject.show()
        e.accept()
        if text.lower() == "input":
            # print(widget)
            self.parent().parent().parent().parent().firstInput = widget
        if text.lower() in ["input", "dense", "dropout", "flatten"]:
            return
        self.parent().parent().closeDropDownWidget()

    @staticmethod
    def getPosition(event):
        return [event.pos().x(), event.pos().y()]

    @staticmethod
    def getMousePositionDifference(position1, position2):
        return [position2[0] - position1[0], position2[1] - position1[1]]

    @staticmethod
    def getMousePositionSum(position1, position2):
        return [position2[0] + position1[0], position2[1] + position1[1]]

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.doubleClicked = True

    def mousePressEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.startx, self.starty = event.pos().x(), event.pos().y()

    def inSelectRect(self, widget: QWidget):
        # print(widget)
        rect = self.selectFrame.rect()
        return rect.contains(widget.pos())

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and self.doubleClicked:
            self.setCursor(QCursor(Qt.CursorShape.ClosedHandCursor))
            if not self.prevMousePosition:
                self.prevMousePosition = self.getPosition(event)
                return
            else:
                currpos = self.getPosition(event)
                diff = self.getMousePositionDifference(self.prevMousePosition, currpos)
                for child in self.children():
                    child.move(*self.getMousePositionSum([child.x(), child.y()], diff))
                self.prevMousePosition = currpos
        elif event.buttons() == Qt.MouseButton.LeftButton and not self.doubleClicked:
            self.selectFrame.setGeometry(min(self.startx, event.pos().x()), min(self.starty, event.pos().y()), abs(event.pos().x() - self.startx), abs(event.pos().y() - self.starty))
            for child in self.children():
                inside = self.inSelectRect(child)
                if inside:
                    self.selections.add(child.layerName)
                if child in self.selections and not inside:
                    self.selections.remove(child.layerName)
            print(self.selections)

    def mouseReleaseEvent(self, a0):
        self.prevMousePosition = None
        self.doubleClicked = False
        self.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.selectFrame.setGeometry(0, 0, 0, 0)
        self.startx, self.starty = 0, 0

    def paintEvent(self, event):
        self.clickCount -= 1
        mainFrame = self.parent().parent()
        # print(mainFrame.connections)
        painter = QPainter(self)
        darkPen = QPen(QColor(80, 80, 80, 180), 1, Qt.PenStyle.SolidLine)
        lightPen = QPen(QColor(80, 80, 80, 70), 1, Qt.PenStyle.SolidLine)
        gridSize = 12
        for i in range(0, self.width(), gridSize):
            if i % 60 == 0:
                painter.setPen(darkPen)
            else:
                painter.setPen(lightPen)
            painter.drawLine(i, 0, i, self.height())
        for j in range(0, self.height(), gridSize):
            if j % 60 == 0:
                painter.setPen(darkPen)
            else:
                painter.setPen(lightPen)
            painter.drawLine(0, j, self.width(), j)

        linePen = QPen(QColor(35, 120, 215), 2, Qt.PenStyle.DashLine)
        if mainFrame.running:
            # self.r, self.g, self.b = (35, 120, 215) if self.clickCount % 10 == 0 else (255, 255, 255)
            self.r, self.g, self.b = randint(0, 255), randint(0, 255), randint(0, 255)
            linePen = QPen(QColor(self.r, self.g, self.b), 2, Qt.PenStyle.CustomDashLine)
        painter.setPen(linePen)
        for layerObject1, layerObject2 in mainFrame.connections:
            lo1w = layerObject1.width()
            lo1h = layerObject1.height()
            lo1x = layerObject1.pos().x()
            lo1y = layerObject1.pos().y()
            lo2w = layerObject2.width()
            lo2x = layerObject2.pos().x()
            lo2y = layerObject2.pos().y()
            painter.drawLine(lo1x + lo1w // 2, lo1y + lo1h, lo2x + lo2w // 2, lo2y)
        self.update()
        painter.end()

    @staticmethod
    def clearTerminal():
        os.system("cls")
