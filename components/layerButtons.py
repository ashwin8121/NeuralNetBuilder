from PyQt6.QtWidgets import QFrame, QHBoxLayout, QWidget, QVBoxLayout, QGraphicsDropShadowEffect, QComboBox, QLabel, QPushButton, QDialog
from .draggable import DraggableButton
from PyQt6.QtGui import QColor, QHoverEvent, QPixmap, QIcon
from PyQt6.QtCore import QSize, Qt, QPropertyAnimation, QPoint
from src.styles.styles import nonDraggableButtonStyle, convolutionDialogStyle, draggableButtonStyle, runButtonStyle, draggableButtonStyleInsideDialog
from .dropDownWidget import DropDownWidget
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import *
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.keras.datasets import mnist
import os
import threading as tr
def train():
    # (x_train, y_train), (x_test, y_test) = mnist.load_data()
    # print(x_train.shape)
    # x_train = x_train.reshape(-1, 28, 28, 1)
    #
    #
    # model =  Sequential([
    #     Conv2D(32, kernel_size=3, activation="relu", padding="same", input_shape=(28, 28, 1)),
    #     MaxPooling2D(pool_size=2, strides=2),
    #     Conv2D(48, kernel_size=3, activation="relu", padding="same"),
    #     MaxPooling2D(pool_size=2, strides=2),
    #     Flatten(),
    #     Dense(64, activation="relu"),
    #     Dense(1, activation="softmax")
    # ])
    #
    # model.compile(optimizer=Adam(learning_rate=1e-3), metrics=["accuracy"], loss="categorical_crossentropy")
    #
    # tb = TensorBoard(log_dir=r"D://logs")
    # tbthread = tr.Thread(target=lambda : os.system('tensorboard.exe --logdir "D:\logs" &'))
    # tbthread.start()
    #
    # print("Tensorboard Started")
    # hist = model.fit(x_train, y_train, epochs=10, callbacks=[tb])
    pass

class ButtonsFrame(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.shadowEffect = QGraphicsDropShadowEffect()
        self.shadowEffect.setBlurRadius(25)
        self.shadowEffect.setColor(QColor(35, 35, 35))
        if parent:
            self.setParent(parent)
        self.mainLayout = QVBoxLayout()
        self.buttonsframe = QFrame()
        self.buttonsframe.setStyleSheet("background-color: rgb(19, 20, 22); border-radius: 25%; padding: 10px;")

        buttonsLayout = QHBoxLayout()

        inputLayerButton = DraggableButton("INPUT")
        buttonsLayout.addWidget(inputLayerButton)

        self.convLayerButton = QPushButton("CONVOLUTION")
        self.convLayerButton.clicked.connect(self.convLayerButtonClicked)
        self.convLayerButton.setStyleSheet(nonDraggableButtonStyle)
        buttonsLayout.addWidget(self.convLayerButton)


        self.poolingLayerButton = QPushButton("POOLING")
        self.poolingLayerButton.setStyleSheet(nonDraggableButtonStyle)
        self.poolingLayerButton.clicked.connect(self.poolingLayerButtonClicked)
        buttonsLayout.addWidget(self.poolingLayerButton)

        flattenLayerButton = DraggableButton("FLATTEN")
        buttonsLayout.addWidget(flattenLayerButton)

        denseLayerButton = DraggableButton("DENSE")
        buttonsLayout.addWidget(denseLayerButton)

        dropoutLayerButton = DraggableButton("DROPOUT")
        buttonsLayout.addWidget(dropoutLayerButton)

        otherLayersButton = QPushButton("OTHERS")
        otherLayersButton.setStyleSheet(nonDraggableButtonStyle)
        otherLayersButton.clicked.connect(self.otherLayersButtonClicked)
        buttonsLayout.addWidget(otherLayersButton)

        runButton = QPushButton()
        runButton.setStyleSheet(runButtonStyle)
        runButton.clicked.connect(self.startRunning)
        runButton.setIcon(QIcon("src/assets/play-button.png"))
        runButton.setIconSize(QSize(30, 30))
        buttonsLayout.addWidget(runButton)

        self.buttonsframe.setLayout(buttonsLayout)
        self.mainLayout.addWidget(self.buttonsframe)
        self.setLayout(self.mainLayout)
        self.buttonsframe.setGraphicsEffect(self.shadowEffect)

    def startRunning(self):
        app = self.parent().parent().parent()
        main = app.parent().parent()

        app.running = not app.running
        tr1 = tr.Thread(target=train)
        tr1.start()
        main.startModelTraining()


    def convLayerButtonClicked(self):
        app = self.parent().parent().parent()
        conv1dDraggable = DraggableButton("CONV1D")
        conv2dDraggable = DraggableButton("CONV2D")
        conv3dDraggable = DraggableButton("CONV3D")
        depthwiseconv1d = DraggableButton("DepthWiseConv1D")
        depthwiseconv2d = DraggableButton("DepthWiseConv2D")
        app.openDropDownWidget(position=[280, 120], height=450, widgets=[conv1dDraggable, conv2dDraggable, conv3dDraggable,
                                                                         depthwiseconv1d, depthwiseconv2d])

    def poolingLayerButtonClicked(self):
        app = self.parent().parent().parent()
        maxpool1dDraggable = DraggableButton("MAXPOOLING1D")
        maxpool2dDraggable = DraggableButton("MAXPOOLING2D")
        maxpool3dDraggable = DraggableButton("MAXPOOLING3D")
        avgpool1dDraggable = DraggableButton("AVGPOOLING1D")
        avgpool2dDraggable = DraggableButton("AVGPOOLING2D")
        avgpool3dDraggable = DraggableButton("AVGPOOLING3D")

        app.openDropDownWidget(position=[510, 120], height=500, widgets=[maxpool1dDraggable, maxpool2dDraggable, maxpool3dDraggable,
                                                             avgpool1dDraggable, avgpool2dDraggable, avgpool3dDraggable])

    def otherLayersButtonClicked(self):
        app = self.parent().parent().parent()
        concatenateDraggable = DraggableButton("Concatenate")
        addLayerDraggable = DraggableButton("Add")
        subtractLayerDraggable = DraggableButton("Subtract")
        lambdaLayerDraggable = DraggableButton("Lambda")
        randomCropLayerDraggable = DraggableButton("Random Corop")
        randomFlipLayerDraggable = DraggableButton("Random Flip")

        app.openDropDownWidget(position=[1390, 120], height=500,
                               widgets=[concatenateDraggable, addLayerDraggable, subtractLayerDraggable,
                                        lambdaLayerDraggable, randomCropLayerDraggable, randomFlipLayerDraggable])





