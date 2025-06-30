import sys
from src.helpers.constants import *
from src.helpers import constants
from collections import defaultdict
from src.components.layerobject import LayerObject
from PyQt6.QtGui import QDrag, QPixmap, QColor
from src.components.layerButtons import ButtonsFrame
from src.components.propertyFrame import PropertyFrame
from src.components.dragdropframe import DragDropFrame
from src.components.dropDownWidget import DropDownWidget
from src.components.parameterframe import ParameterFrame
from src.components.draggable import DraggableObject, DraggableButton
from PyQt6.QtCore import QMimeData, Qt, QPropertyAnimation, QRect
from src.styles.styles import propertyWindowStyle, dropDownWidgetStyle, parameterFrameStyle
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QFrame, QVBoxLayout, QMainWindow, QLabel, QScrollArea, QGraphicsDropShadowEffect, QMessageBox

# todo: increase font size in property frame
# todo: some way to show direction in the connection lines
# todo: one bug in selection needed to be figured out
# todo: property frame completion
# todo:   1: increase font size
# todo:   2: set default config setting as values in feilds
# todo: Widgets Tab at the bottom [Builder, Dataset, Tensorboard]
# todo: search Bar at the left of the  buttons frame
# todo: move Dropout to others
# todo: add validation split in dataset tab


class BuilderWidget(QWidget):
    usedLayerNames = defaultdict(int)
    selection1 = None
    selection2 = None

    connections = set()

    running = False

    def __init__(self):
        super().__init__()

        self.x, self.y = 10, 10
        self.mainFrame = QFrame(self)
        # self.mainFrame.setStyleSheet()
        self.mainFrame.name = "MAIN FRAME"
        self.mainFrame.resize(1920, 1080)

        self.dragDropFrame = DragDropFrame(self.mainFrame)
        self.dragDropFrame.setStyleSheet("background-color: rgb(45, 46, 50)")
        # self.dragDropFrame.move(-10, -10)
        self.dragDropFrame.resize(1920, 1009)

        horizontalFrame = QFrame(self.mainFrame)
        horizontalFrame.setStyleSheet("background-color: transparent")
        horizontalFrame.move(0, 0)
        horizontalFrame.resize(1920, 130)
        horizontalLayout = QVBoxLayout()
        buttonFrame = ButtonsFrame()
        buttonFrame.setMaximumHeight(100)
        horizontalLayout.addWidget(buttonFrame)
        horizontalFrame.setLayout(horizontalLayout)

        self.parameterFrame = ParameterFrame(self)
        self.parameterFrame.move(1600, 120)
        self.parameterFrame.setStyleSheet(parameterFrameStyle)
        shadowEffect = QGraphicsDropShadowEffect()
        shadowEffect.setBlurRadius(25)
        shadowEffect.setColor(QColor(15, 15, 15))
        self.parameterFrame.setGraphicsEffect(shadowEffect)


        self.propertyFrame = PropertyFrame(self)
        self.propertyFrame.setGeometry(QRect(1950, 120, PROPERTY_FRAME_WIDTH, PROPERTY_FRAME_HEIGHT))
        self.propertyFrameopenAnimation = QPropertyAnimation(self.propertyFrame, b"geometry")
        self.propertyFramecloseAnimation = QPropertyAnimation(self.propertyFrame, b"geometry")

        self.dropDownWidget = DropDownWidget(self)
        self.dropDownWidget.setGeometry(QRect(0, 0, 0, 0))
        self.dropDownWidgetOpenAnimation = QPropertyAnimation(self.dropDownWidget, b"geometry")
        self.dropDownWidgetCloseAnimation = QPropertyAnimation(self.dropDownWidget, b"geometry")

    def keyPressEvent(self, e):
        if e.key() == Qt.Key.Key_Escape:
            if self.propertyFrame.inFrame:
                self.closePropertyWindow()
                self.propertyFrame.inFrame = False
                return
            self.destroy(True)
            # print([f"{layer[0].layerName}->{layer[1].layerName}" for layer in self.connections])
            exit(-1)
        if e.key() == Qt.Key.Key_Delete:
            if self.selection1 and not self.selection2:
                for conn in self.connections:
                    if self.selection1 in conn:
                        self.showConnectionWarning()
                        return
                if self.running:
                    return self.modelRunningWarning()
                    return
                self.deletePressed(self.selection1)

    def modelRunningWarning(self):
        dlg = QMessageBox(self)
        dlg.setText("Model Traning currently. Cannot Change architecture")
        button = dlg.exec()

    def showConnectionWarning(self):
        dlg = QMessageBox(self)
        dlg.setText("Remove the existing connections\nwith the layer to delete the layer")
        button = dlg.exec()


    def deletePressed(self, layer):
        dlg = QMessageBox(self)
        dlg.setText("Do you want to delete the Layer")
        dlg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        button = dlg.exec()
        if button == QMessageBox.StandardButton.Ok:
            layer.deleteYourself()

    def openPropertyWindow(self, layer):
        # print(layer.layerName)
        if self.propertyFrame.inFrame  == layer.layerName:
            self.closePropertyWindow()
            self.propertyFrame.inFrame = False
            return

        self.propertyFrame.inFrame = layer.layerName
        self.propertyFrame.setConfigurations(layer)
        self.propertyFrame.setStyleSheet(propertyWindowStyle)
        self.propertyFrameopenAnimation.setDuration(PROPERTY_ANIMATION_DURATION)
        self.propertyFrameopenAnimation.setStartValue(QRect(PROPERTY_WINDOW_ANIMATION_START_X, PROPERTY_WINDOW_ANIMATION_START_y, PROPERTY_FRAME_WIDTH, PROPERTY_FRAME_HEIGHT))
        self.propertyFrameopenAnimation.setEndValue(QRect(PROPERTY_WINDOW_ANIMATION_END_X, PROPERTY_WINDOW_ANIMATION_END_y, PROPERTY_FRAME_WIDTH, PROPERTY_FRAME_HEIGHT))
        self.propertyFrameopenAnimation.start()
        shadowEffect = QGraphicsDropShadowEffect()
        shadowEffect.setBlurRadius(25)
        shadowEffect.setColor(QColor(15, 15, 15))
        self.propertyFrame.setGraphicsEffect(shadowEffect)


    def closePropertyWindow(self):
        self.propertyFramecloseAnimation.setDuration(PROPERTY_ANIMATION_DURATION)
        self.propertyFramecloseAnimation.setStartValue(QRect(PROPERTY_WINDOW_ANIMATION_END_X, PROPERTY_WINDOW_ANIMATION_END_y, PROPERTY_FRAME_WIDTH, PROPERTY_FRAME_HEIGHT))
        self.propertyFramecloseAnimation.setEndValue(QRect(PROPERTY_WINDOW_ANIMATION_START_X, PROPERTY_WINDOW_ANIMATION_START_y, PROPERTY_FRAME_WIDTH, PROPERTY_FRAME_HEIGHT))
        self.propertyFramecloseAnimation.start()

    def getLayerName(self, layerName):
        self.usedLayerNames[layerName] += 1
        return f"{layerName}_{self.usedLayerNames[layerName]}"

    def openDropDownWidget(self, position, height=500, widgets=[]):
        # print(widgets)
        self.dropDownWidget.position = position
        self.dropDownWidget.heightVal = height
        self.dropDownWidget.addWidgetsToDropDown(widgets)
        self.dropDownWidget.setStyleSheet(dropDownWidgetStyle)
        self.dropDownWidgetOpenAnimation.setDuration(250)
        self.dropDownWidget.resize(200, height)
        self.dropDownWidgetOpenAnimation.setStartValue(QRect(*position, 200, 25))
        self.dropDownWidgetOpenAnimation.setEndValue(QRect(*position, 200, height))
        self.dropDownWidgetOpenAnimation.start()
        shadowEffect = QGraphicsDropShadowEffect()
        shadowEffect.setBlurRadius(25)
        shadowEffect.setColor(QColor(15, 15, 15))
        self.dropDownWidget.setGraphicsEffect(shadowEffect)

    def closeDropDownWidget(self):
        self.dropDownWidgetCloseAnimation.setDuration(250)
        self.dropDownWidgetCloseAnimation.setStartValue(QRect(*self.dropDownWidget.position, 200, self.dropDownWidget.heightVal))
        self.dropDownWidgetCloseAnimation.setEndValue(QRect(QRect(*self.dropDownWidget.position, 200, 0)))
        self.dropDownWidgetCloseAnimation.start()
