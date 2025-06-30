from time import sleep
from PIL import ImageQt
from PIL.Image import fromarray
from collections import Counter

from src.components.imagesDisplayFrame import ImagesDisplayFrame
from src.styles import folderDropWidgetStyle
from src.helpers.datasetLoader import DatasetLoader
from src.helpers.functions import propertyAnimation
from PyQt6.QtCore import Qt, QPropertyAnimation, QRect
from src.components.loadingScreen import LoadingScreen
from src.components.folderDropWidget import FolderDropWidget
from src.components.datasetParameter import DatasetParameters
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QFrame, QVBoxLayout, QGridLayout, QToolTip, QButtonGroup

#todo: Implement Data Augmentation Techniques
#todo: Visualize the dataset in some kind of way

class ImageDatasetFrame(QWidget):
    def __init__(self, *args, **kwargs):

        pos = kwargs.pop("pos", None)
        size = (1580, 900)
        super().__init__(*args, **kwargs)

        self.mainFrame = QFrame(self)
        self.mainFrame.resize(*size)
        if pos:
            self.move(*pos)

        # self.setStyleSheet("border: 1px solid rgb(92, 92, 92);")
        self.setGeometry(QRect(*pos, *size))

        self.folderDropWidget = FolderDropWidget(self.mainFrame)
        self.folderDropWidget.move(390, 40)

        # selectButton = QPushButton("Select", self.mainFrame)
        # selectButton.resize(200, 60)
        # selectButton.move(800, 150)
        # selectButton.clicked.connect(self.datasetSelected)
        #
        # clearButton = QPushButton("Clear", self.mainFrame)
        # clearButton.resize(200, 60)
        # clearButton.move(790, 250)

        self.datasetParameter = DatasetParameters(self.mainFrame)
        self.datasetParameter.move(1250, 40)
        # self.datasetParameter.setStyleSheet("border: 2px solid white;")

        self.mainFrameOpenAnimation = propertyAnimation(self, 100, b"geometry", QRect(*pos, *size), QRect(205, 20, *size))
        self.mainFrameCloseAnimation = propertyAnimation(self, 100, b"geometry", QRect(205, 20, *size), QRect(*pos, *size))

        self.loadingScreen = LoadingScreen()

        self.classesFrame = QFrame(self.mainFrame)
        self.classesFrame.move(340, 155)
        self.classesFrame.resize(600, 300)
        self.classesFrame.setStyleSheet("border: 1px solid rgb(92, 92, 92); border-radius: 20px;")

        self.classesLayout = QGridLayout(self.classesFrame)

        self.imgdisp = ImagesDisplayFrame()

        self.noofclasses = QLabel(self.classesFrame)
        self.noofclasses.resize(600, 30)
        self.noofclasses.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.noofclasses.move(0, 20)
        self.noofclasses.setStyleSheet("font-size: 14px; font-family: roboto mono; border: none;")




    def datasetSelected(self):
        # dataset = getImageDatasetGenerator(self.folderDropWidget.datasetURL)
        params = self.datasetParameter.getParams()
        self.loadingScreen.show()
        self.datasetLoader = DatasetLoader()
        self.datasetLoader.getImageDataset(self.folderDropWidget.datasetURL, params=params)
        self.datasetLoader.start()
        self.datasetLoader.loading_completed.connect(self.datasetLoaded)

    def datasetLoaded(self):
        self.loadingScreen.close()
        self.dataset = self.datasetLoader.dataset
        classes = self.dataset.class_indices
        self.indexClasses = dict([(v, k) for (k, v) in classes.items()])
        labelCounts = Counter(self.dataset.classes)
        labelWidgets = []

        self.noofclasses.setText(f"{len(classes)} classes were found in the uploaded dataset")



        self.classButtonGroup = QButtonGroup()
        self.classButtonGroup.idClicked.connect(self.classButtonClicked)
        for i, (className, index) in enumerate(classes.items()):
            classButton = QPushButton(className)
            classButton.setStyleSheet("font-size: 14px; font-family: roboto mono; border-radius: 10px; ")
            classButton.setMinimumHeight(40)
            classButton.setToolTip(f"Number of Images found\nfor class {className}: {labelCounts[index]}")
            self.classButtonGroup.addButton(classButton, i)
            self.classesLayout.addWidget(classButton, i // 2, i % 2)

    def classButtonClicked(self, id):
        images = []
        for img, y in zip(self.dataset[0][0], self.dataset[0][1]):
            if y == id:
                print(img.shape)
                images.append(img)
        self.imgdisp.displayImages(images)


    def openAnimation(self):
        self.mainFrameOpenAnimation.start()

    def closeAnimation(self):
        self.mainFrameCloseAnimation.start()
