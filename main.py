import os
import sys
import time
import threading as tr
from src.widgets.builder import BuilderWidget
from src.widgets.dataset import DatasetWidget
from src.widgets.monitor import MonitorWidget
from PyQt6.QtCore import QSize, QPoint, Qt, QTimer
from PyQt6.QtGui import QFont, QKeySequence, QShortcut
from src.styles.styles import tabStyle, selectedTabStyle
from PyQt6.QtWidgets import QApplication, QMainWindow, QFrame, QPushButton, QVBoxLayout
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import TensorBoard

class Main(QMainWindow):
    firstInput = None
    current = None
    name = "MainWindow"
    modelLayers = [Input(shape=[224, 224, 1])]
    def __init__(self):
        super().__init__()

        self.setMinimumWidth(1920)
        self.setMinimumHeight(1080)

        self.mainFrame = QFrame(self)

        self.builderWidget = BuilderWidget()
        self.builderWidget.setParent(self.mainFrame)
        self.builderWidget.move(2000, 1000)

        self.datasetWidget = DatasetWidget()
        self.datasetWidget.setParent(self.mainFrame)
        self.datasetWidget.move(2000, 1000)

        self.monitorWidget = MonitorWidget()
        self.monitorWidget.setParent(self.mainFrame)
        self.monitorWidget.move(2000, 1000)

        self.current = [self.builderWidget, self.datasetWidget, self.monitorWidget][0]
        self.current.move(0, 0)

        builderButton = QPushButton("Builder", self)
        builderButton.move(600, 950)
        builderButton.resize(250, 40)
        builderButton.setFont(QFont("Roboto mono", 11))
        builderButton.setStyleSheet((selectedTabStyle if self.current == self.builderWidget else tabStyle) % 20)
        builderButton.clicked.connect(self.initiateBuilderWidget)

        monitorButton = QPushButton("Monitor Training", self)
        monitorButton.move(1060, 950)
        monitorButton.resize(250, 40)
        monitorButton.setFont(QFont("Roboto mono", 11))
        monitorButton.setStyleSheet((selectedTabStyle if self.current == self.monitorWidget else tabStyle) % 20)
        monitorButton.clicked.connect(self.initiateMonitorWidget)

        datasetButton = QPushButton("Dataset", self)
        datasetButton.move(830, 950)
        datasetButton.resize(250, 40)
        datasetButton.setFont(QFont("Roboto mono", 11))
        datasetButton.setStyleSheet((selectedTabStyle if self.current == self.datasetWidget else tabStyle) % 0)
        datasetButton.clicked.connect(self.initiateDatasetWidget)

        self.tabsToButtons = {
            self.builderWidget: builderButton,
            self.datasetWidget: datasetButton,
            self.monitorWidget: monitorButton
        }

        self.setCentralWidget(self.mainFrame)
        closeShortCut = QShortcut(QKeySequence("ctrl+c"), self)
        closeShortCut.activated.connect(self.closeApplication)

    def simplePrint(self):
        print(self.name)

    def initiateBuilderWidget(self):
        if self.current == self.builderWidget:
            return
        self.current.move(2000, 1000)
        self.tabsToButtons[self.current].setStyleSheet(tabStyle % (0 if self.current == self.datasetWidget else 20))
        self.builderWidget.move(0, 0)
        self.current = self.builderWidget
        self.tabsToButtons[self.current].setStyleSheet(selectedTabStyle % 20)

    def initiateDatasetWidget(self):
        if self.current == self.datasetWidget:
            return
        self.current.move(2000, 1000)
        self.tabsToButtons[self.current].setStyleSheet(tabStyle % 20)
        self.datasetWidget.move(0, 0)
        self.current = self.datasetWidget
        self.tabsToButtons[self.current].setStyleSheet(selectedTabStyle % 0)

    def initiateMonitorWidget(self):
        if self.current == self.monitorWidget:
            return
        self.current.move(2000, 1000)
        self.tabsToButtons[self.current].setStyleSheet(tabStyle % (0 if self.current == self.datasetWidget else 20))
        self.monitorWidget.move(0, 0)
        self.current = self.monitorWidget
        self.tabsToButtons[self.current].setStyleSheet(selectedTabStyle % 20)
        self.monitorWidget.initiateTensorBoard()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.closeApplication()

    def closeApplication(self):
        print(self.modelLayers)
        self.destroy(True)
        exit(-1)


    def startModelTraining(self):
        print(self.firstInput)
        print("Model Training should start")
        print(self.modelLayers)
        self.trainThread = tr.Thread(target=self.startTraining, args=(self.modelLayers,))
        self.trainThread.start()

    def startTraining(self, layers):
        self.model = Sequential(self.modelLayers)
        self.model.summary()
        dataset = self.datasetWidget.imageDatasetFrame.datasetLoader.dataset
        epochs = int(self.builderWidget.parameterFrame.epochs.text())
        lr = float(self.builderWidget.parameterFrame.learningRate.text())
        self.model.compile(optimizer=Adam(learning_rate=lr), metrics=['accuracy'], loss="binary_crossentropy")

        tb = TensorBoard(log_dir=r"D:/logs")
        # os.chdir("components")
        # tbthread = tr.Thread(target=lambda : os.system('tensorboard.exe --logdir=D:/logs &'))
        # tbthread.start()

        self.model.fit(dataset, epochs=epochs, callbacks=[tb])



def main():
    app = QApplication(sys.argv)
    main = Main()
    main.showMaximized()
    app.exec()


if __name__ == '__main__':
    main()
