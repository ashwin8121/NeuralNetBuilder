from PyQt6.QtCore import QSize, QPropertyAnimation, QRect, Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QFrame, QPushButton, QLabel, QComboBox, QLineEdit, QCheckBox
from src.components.parameterframe import QHLine
from src.styles import datasetParameterHeadStyle, bodyOpenButtonStyle, bodyOpenStyle

BODY_HEIGHT = 800

class DatasetParameters(QWidget):
    opened = True
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.setStyleSheet("border: 1px solid white;")

        # self.head = QFrame(self)

        # self.head.setGeometry(1250, 50, 300, 75)
        # self.head.setStyleSheet(datasetParameterHeadStyle)

        # bodyOpenButton = QPushButton(self.head)
        # bodyOpenButton.setIcon(QIcon("src/assets/icons-drop-down.png"))
        # bodyOpenButton.setIconSize(QSize(40, 40))
        # bodyOpenButton.setStyleSheet(bodyOpenButtonStyle)
        # bodyOpenButton.resize(45, 45)
        # bodyOpenButton.move(240, 15)
        # bodyOpenButton.clicked.connect(self.closeBody)

        self.body = QFrame(self)
        self.body.resize(300, BODY_HEIGHT)
        self.body.setStyleSheet(bodyOpenStyle)

        # self.bodyCloseAnimation = QPropertyAnimation(self.body, b"geometry")
        # self.bodyCloseAnimation.setStartValue(QRect(1250, 125, 300, BODY_HEIGHT))
        # self.bodyCloseAnimation.setEndValue(QRect(1250, 125, 300, 0))
        # self.bodyCloseAnimation.setDuration(300)
        #
        # self.bodyOpenAnimation = QPropertyAnimation(self.body, b"geometry")
        # self.bodyOpenAnimation.setStartValue(QRect(1250, 125, 300, 0))
        # self.bodyOpenAnimation.setEndValue(QRect(1250, 125, 300, BODY_HEIGHT))
        # self.bodyOpenAnimation.setDuration(300)
        #

        paramLabel = QLabel("Dataset Parameters", self.body)
        paramLabel.setStyleSheet("border: none; font-family: roboto mono; font-size: 24px; background-color: transparent; font-weight: bold;")
        paramLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        paramLabel.resize(300, 50)

        imageshapeLabel = QLabel("Select Image Shape ", self.body)
        imageshapeLabel.setStyleSheet("border: none; font-size: 16px; font-family: roboto mono;")
        imageshapeLabel.move(20, 60)

        self.imageShape1 = QLineEdit(self.body)
        self.imageShape1.setGeometry(20, 90, 60, 30)
        self.imageShape1.setStyleSheet("border-radius: none; font-size: 16px; font-family: roboto mono;")
        self.imageShape1.setText("224")
        self.imageShape1.textChanged.connect(lambda : self.imageShape2.setText(self.imageShape1.text()))

        xlabel = QLabel("X", self.body)
        xlabel.move(95, 93)
        xlabel.setStyleSheet("border-radius: none; font-size: 16px; font-family: roboto mono; border: none;")

        self.imageShape2 = QLineEdit(self.body)
        self.imageShape2.setText("224")
        self.imageShape2.setStyleSheet("border-radius: none; font-size: 16px; font-family: roboto mono;")
        self.imageShape2.setGeometry(120, 90, 60, 30)

        QHLine(self.body).move(10, 130)

        colorLabel = QLabel("Select Color Mode: ", self.body)
        colorLabel.setStyleSheet("border-radius: none; font-size: 16px; font-family: roboto mono; border: none;")
        colorLabel.move(20, 140)

        self.colorMode = QComboBox(self.body)
        self.colorMode.addItems(["RGB", "Grayscale"])
        self.colorMode.setStyleSheet("border-radius: none; font-size: 16px; font-family: roboto mono;")
        self.colorMode.move(20, 170)
        self.colorMode.resize(200, 30)

        QHLine(self.body).move(10, 210)

        classLabel = QLabel("Select Class Mode: ", self.body)
        classLabel.setStyleSheet("border-radius: none; font-size: 16px; font-family: roboto mono; border: none;")
        classLabel.move(20, 220)

        self.classMode = QComboBox(self.body)
        self.classMode.addItems(["Categorical", "Sparse", "Binary"][::-1])
        self.classMode.setStyleSheet("border-radius: none; font-size: 16px; font-family: roboto mono;")
        self.classMode.move(20, 250)
        self.classMode.resize(200, 30)

        QHLine(self.body).move(10, 290)

        classLabel = QLabel("Select Batch Size: ", self.body)
        classLabel.setStyleSheet("border-radius: none; font-size: 16px; font-family: roboto mono; border: none;")
        classLabel.move(20, 300)

        self.batchSize = QLineEdit(self.body)
        self.batchSize.setStyleSheet("border-radius: none; font-size: 16px; font-family: roboto mono;")
        self.batchSize.setText("32")
        self.batchSize.setGeometry(20, 330, 200, 30)

        QHLine(self.body).move(10, 370)

        self.shuffle = QCheckBox("Shuffle", self.body)
        self.shuffle.setChecked(True)
        self.shuffle.move(20, 383)
        self.shuffle.setStyleSheet("border: none; border-radius: none; font-size: 16px; font-family: roboto mono; ")
        self.shuffle.toggled.connect(lambda: self.seed.setDisabled(not self.shuffle.isChecked()))

        self.seed = QLineEdit(self.body)
        self.seed.move(120, 380)
        self.seed.resize(50, 30)
        self.seed.setStyleSheet("border-radius: none; font-family: roboto mono; font-size: 16px;")


    def getParams(self):
        params = {}
        params["imageSize"] = [int(self.imageShape1.text()), int(self.imageShape2.text())]
        params["batchSize"] = int(self.batchSize.text())
        params["colorMode"] = self.colorMode.currentText()
        params["classType"] = self.classMode.currentText()
        params["shuffle"] = self.shuffle.isChecked()
        params["seed"] = int(self.seed.text()) if self.seed.text() else None
        return params

    # def closeBody(self):
    #     if not self.opened:
    #         # self.opened = not self.opened
    #         self.openBody()
    #         return
    #     self.opened = not self.opened
    #     self.bodyCloseAnimation.start()
    #
    # def openBody(self):
    #     if self.opened:
    #         # self.opened = not self.opened
    #         self.closeBody()
    #         return
    #     self.opened = not self.opened
    #     self.bodyOpenAnimation.start()
