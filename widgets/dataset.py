from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QFrame, QButtonGroup, QHBoxLayout, QStackedWidget, QComboBox
from PyQt6.QtCore import Qt, QPropertyAnimation, QRect, QSize
from src.components.folderDropWidget import FolderDropWidget
from src.components.imageDatasetFrame import ImageDatasetFrame
from src.components.tableDatasetFrame import TableDatasetFrame
from src.components.textDatasetFrame import TextDatasetFrame
from src.styles import sidebarButtonStyle, sidebarLabelStyle, selectedAnimatedButtonStyle, animatedButtonStyle
from src.styles.styles import datasetTypeButtonsStyle, sidebarStyle
from src.components.parameterframe import QHLine
from src.components.animationButton import AnimatedButton
from tensorflow.keras.datasets import mnist, cifar10, cifar100

class DatasetWidget(QWidget):

    datasetType = "IMAGE"

    sidebarOpened = True

    def __init__(self):
        super().__init__()

        bottomLine = QHLine(self)
        bottomLine.move(0, 942)
        bottomLine.resize(1920, 1)


        self.sidebar = QFrame(self)
        self.sidebar.setGeometry(0, 0, 300, 939)
        self.sidebar.setStyleSheet(sidebarStyle)

        sidebarButton = QPushButton(self.sidebar)
        sidebarButton.setIcon(QIcon("src/assets/menu-icon.png"))
        sidebarButton.setIconSize(QSize(30, 30))
        sidebarButton.resize(50, 50)
        sidebarButton.move(10, 10)
        sidebarButton.setStyleSheet(sidebarButtonStyle)
        sidebarButton.clicked.connect(self.sidebarToggle)

        self.sidebarLabel = QLabel("Dataset Types", self.sidebar)
        self.sidebarLabel.move(70, 22)
        self.sidebarLabel.setStyleSheet(sidebarLabelStyle)


        self.sidebarOpenAnimation = QPropertyAnimation(self.sidebar, b"geometry")
        self.sidebarCloseAnimation = QPropertyAnimation(self.sidebar, b"geometry")

        self.imageButton = AnimatedButton("  Image", self.sidebar, xy = [0, 70])
        self.imageButton.setIcon(QIcon(r"src/assets/imageicon.png"))
        self.imageButton.setIconSize(QSize(25, 25))
        self.imageButton.setFont(QFont("roboto mono", 14))
        self.imageButton.move(0, 70)
        self.imageButton.clicked.connect(self.imageTypeSelected)
        self.imageButton.setStyleSheet(selectedAnimatedButtonStyle)

        # self.textButton = AnimatedButton("  Text", self.sidebar, xy = [0, 120])
        # self.textButton.setIcon(QIcon(r"src/assets/texticon.png"))
        # self.textButton.setFont(QFont("roboto mono", 14))
        # self.textButton.setIconSize(QSize(25, 25))
        # self.textButton.move(0, 120)
        # self.textButton.clicked.connect(self.textTypeSelected)
        #
        # self.tableButton = AnimatedButton("  Tabular", self.sidebar, xy = [0, 170])
        # self.tableButton.setIcon(QIcon(r"src/assets/tableicon.png"))
        # self.tableButton.setFont(QFont("roboto mono", 14))
        # self.tableButton.setIconSize(QSize(25, 25))
        # self.tableButton.move(0, 170)
        # self.tableButton.clicked.connect(self.tableTypeSelected)

        self.imageDatasetFrame = ImageDatasetFrame(self, pos=[320, 20])
        # self.textDatasetFrame = TextDatasetFrame(self, pos=[320, 20])
        # self.textDatasetFrame.move(3000, 3000)
        # self.tableDatasetFrame = TableDatasetFrame(self, pos=[320, 20])
        # self.tableDatasetFrame.move(3000, 3000)


        self.current = self.imageDatasetFrame
        # self.imageDatasetFrame.move(320, 20)

        # datasetDropDown = QComboBox(self)
        # datasetDropDown.move(400, 100)
        # datasetDropDown.resize(200, 60)
        # datasetDropDown.addItems(["--select", "MNIST", "CIFAR10", "CIFAR100", "Custom"])
        # datasetDropDown.currentTextChanged.connect(self.datasetSelected)

    def datasetSelected(self, value):
        print(value)


    def imageTypeSelected(self):
        self.datasetType = "IMAGE"
        self.imageButton.setStyleSheet(selectedAnimatedButtonStyle)
        self.textButton.setStyleSheet(animatedButtonStyle)
        self.tableButton.setStyleSheet(animatedButtonStyle)
        self.setImageDataFrame()

    def setImageDataFrame(self):
        # if self.datasetType == "IMAGE":
        #     return
        pos = self.current.pos().x(), self.current.pos().y()
        self.current.move(3000, 3000)
        self.imageDatasetFrame.move(*pos)
        self.current = self.imageDatasetFrame

    def textTypeSelected(self):
        self.datasetType = "TEXT"
        self.imageButton.setStyleSheet(animatedButtonStyle)
        self.textButton.setStyleSheet(selectedAnimatedButtonStyle)
        self.tableButton.setStyleSheet(animatedButtonStyle)
        self.setTextDataFrame()

    def setTextDataFrame(self):
        # if self.datasetType == "TEXT":
        #     return
        pos = self.current.pos().x(), self.current.pos().y()
        self.current.move(3000, 3000)
        self.textDatasetFrame.move(*pos)
        self.current = self.textDatasetFrame


    def tableTypeSelected(self):
        self.datasetType = "TABLE"
        self.imageButton.setStyleSheet(animatedButtonStyle)
        self.textButton.setStyleSheet(animatedButtonStyle)
        self.tableButton.setStyleSheet(selectedAnimatedButtonStyle)
        self.setTableDataFrame()

    def setTableDataFrame(self):
        # if self.datasetType == "TABLE":
        #     return
        pos = self.current.pos().x(), self.current.pos().y()
        self.current.move(3000, 3000)
        self.tableDatasetFrame.move(*pos)
        self.current = self.tableDatasetFrame

    def sidebarToggle(self):
        if self.sidebarOpened:
            self.closeSidebar()
            self.current.openAnimation()
        else:
            self.openSidebar()
            self.current.closeAnimation()
        self.sidebarOpened = not self.sidebarOpened


    def closeSidebar(self):
        self.sidebarCloseAnimation.setDuration(100)
        self.sidebarCloseAnimation.setStartValue(QRect(0, 0, 300, 939))
        self.sidebarCloseAnimation.setEndValue(QRect(0, 0, 70, 939))
        self.sidebarCloseAnimation.start()

    def openSidebar(self):
        self.sidebarOpenAnimation.setDuration(100)
        self.sidebarOpenAnimation.setStartValue(QRect(0, 0, 70, 939))
        self.sidebarOpenAnimation.setEndValue(QRect(0, 0, 300, 939))
        self.sidebarOpenAnimation.start()
