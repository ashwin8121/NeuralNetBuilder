from PyQt6.QtWidgets import QWidget, QFrame, QPushButton, QLabel, QComboBox, QSpinBox, QFormLayout, QLineEdit, \
    QCheckBox, QButtonGroup
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont, QIcon
from src.helpers.layerProperties import properties
from src.styles.styles import propertyWindowCloseButtonStyle, parameterLabelStyle

class QHLine(QFrame):
    def __init__(self, parent, ishead=False):
        super(QHLine, self).__init__(parent)
        self.setFrameShape(QFrame.Shape.HLine)
        self.setFrameShadow(QFrame.Shadow.Sunken)
        if not ishead:
            self.setStyleSheet("background-color: white")
        else:
            self.setStyleSheet("background-color: rgba(255, 255, 255, 80)")
        self.resize(280, 1)

class ParameterFrame(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        self.mainFrame = QFrame(self)

        parameterLabel = QLabel("TRAINING PARAMETERS", self)
        parameterLabel.setStyleSheet(parameterLabelStyle)
        parameterLabel.resize(250, 60)
        parameterLabel.move(45, 0)
        parameterLabel.setFont(QFont("Roboto mono", 14, 10))

        QHLine(self, True).move(10, 90)

        optimizerLabel = QLabel("Select Optimization Algorithm", self)
        optimizerLabel.setFont(QFont("Roboto mono", 11))
        optimizerLabel.move(12, 100)

        self.optimizer = QComboBox(self)
        self.optimizer.addItems(["--select--", "Adam", "SGD", "Adagrad", "RMSProp", "Adadelta", "Nadam", "Adamax"])
        self.optimizer.move(12, 135)
        self.optimizer.resize(250, 30)
        self.optimizer.setStyleSheet("border: 1px solid #eee; border-radius: 0;")

        QHLine(self, True).move(10, 180)
        #
        lossFuncLabel = QLabel("Select Loss Function", self)
        lossFuncLabel.setFont(QFont("Roboto mono", 11))
        lossFuncLabel.move(12, 190)

        self.lossFunction = QComboBox(self)
        self.lossFunction.addItems(["--select--", "RMS", "Categorical Cross Entropy", "Sparse Catgorical Cross Entropy", "Binary Cross Entropy"])
        self.lossFunction.move(12, 220)
        self.lossFunction.resize(250, 30)
        self.lossFunction.setStyleSheet("border: 1px solid #eee; border-radius: 0;")

        QHLine(self, True).move(10, 262)

        epochsLabel = QLabel("Enter Number of Epochs: ", self)
        epochsLabel.move(12, 270)
        epochsLabel.setFont(QFont("Roboto mono", 11))

        self.epochs = QLineEdit(self)
        self.epochs.setPlaceholderText("10")
        self.epochs.move(12, 300)
        self.epochs.resize(250, 30)
        self.epochs.setFont(QFont("Roboto mono", 11))
        self.epochs.setStyleSheet("border: 1px solid #eee; border-radius: 0;")

        QHLine(self, True).move(10, 342)

        batchSizeLabel = QLabel("Enter Batch Size: ", self)
        batchSizeLabel.move(12, 350)
        batchSizeLabel.setFont(QFont("Roboto mono", 11))

        self.batchSize = QLineEdit(self)
        self.batchSize.setPlaceholderText("32")
        self.batchSize.move(12, 380)
        self.batchSize.resize(250, 30)
        self.batchSize.setFont(QFont("Roboto mono", 11))
        self.batchSize.setStyleSheet("border: 1px solid #eee; border-radius: 0;")

        QHLine(self, True).move(10, 425)

        learnignRateLabel = QLabel("Enter Learning Rate: ", self)
        learnignRateLabel.move(12, 430)
        learnignRateLabel.setFont(QFont("Roboto mono", 11))

        self.learningRate = QLineEdit(self)
        self.learningRate.setPlaceholderText("0.001")
        self.learningRate.move(12, 460)
        self.learningRate.resize(250, 30)
        self.learningRate.setFont(QFont("Roboto mono", 11))
        self.learningRate.setStyleSheet("border: 1px solid #eee; border-radius: 0;")

        QHLine(self, True).move(10, 505)

        metricsLabel = QLabel("Select Necessary Metrics: ", self)
        metricsLabel.move(12, 512)
        metricsLabel.setFont(QFont("Roboto mono", 11))

        # accuracy, loss, recall, precision, f1 score, roc
        self.accuracyCheckBox = QCheckBox("Accuracy", self)
        self.accuracyCheckBox.move(20, 540)
        self.accuracyCheckBox.setFont(QFont("Roboto mono", 10))

        self.lossCheckBox = QCheckBox("Loss Value", self)
        self.lossCheckBox.move(20, 570)
        self.lossCheckBox.setFont(QFont("Roboto mono", 10))

        self.recallCheckBox = QCheckBox("Recall", self)
        self.recallCheckBox.move(20, 600)
        self.recallCheckBox.setFont(QFont("Roboto mono", 10))

        self.precisionCheckBox = QCheckBox("Precision", self)
        self.precisionCheckBox.move(150, 540)
        self.precisionCheckBox.setFont(QFont("Roboto mono", 10))

        self.f1scoreCheckBox = QCheckBox("F1 Score", self)
        self.f1scoreCheckBox.move(150, 570)
        self.f1scoreCheckBox.setFont(QFont("Roboto mono", 10))

        self.rocCheckBox = QCheckBox("ROC", self)
        self.rocCheckBox.move(150, 600)
        self.rocCheckBox.setFont(QFont("Roboto mono", 10))

        QHLine(self, True).move(10, 630)

        callbacksLabel = QLabel("Select Necessary Callbacks: ", self)
        callbacksLabel.move(12, 640)
        callbacksLabel.setFont(QFont("Roboto mono", 11))

        self.lrSchedulerCheckBox = QCheckBox("Learning Rate Scheduler", self)
        self.lrSchedulerCheckBox.move(20, 670)
        self.lrSchedulerCheckBox.setFont(QFont("Roboto mono", 10))

        self.earlyStoppingCheckBox = QCheckBox("Early Stopping", self)
        self.earlyStoppingCheckBox.move(20, 700)
        self.earlyStoppingCheckBox.setFont(QFont("Roboto mono", 10))

        self.modelCheckPoingCheckBox = QCheckBox("Model Check Point", self)
        self.modelCheckPoingCheckBox.move(20, 730)
        self.modelCheckPoingCheckBox.setFont(QFont("Roboto mono", 10))

        self.csvLoggerCheckBox = QCheckBox("CSVLogger", self)
        self.csvLoggerCheckBox.move(20, 760)
        self.csvLoggerCheckBox.setFont(QFont("Roboto mono", 10))

        self.reduceLRonPlCheckBox = QCheckBox("Reduce LR on Platue", self)
        self.reduceLRonPlCheckBox.move(20, 790)
        self.reduceLRonPlCheckBox.setFont(QFont("Roboto mono", 10))

        QHLine(self, True).move(10, 820)

        self.metrics = [self.accuracyCheckBox, self.lossCheckBox, self.recallCheckBox, self.precisionCheckBox, self.rocCheckBox, self.f1scoreCheckBox]
        self.callbacks = [self.lrSchedulerCheckBox, self.earlyStoppingCheckBox, self.modelCheckPoingCheckBox, self.csvLoggerCheckBox, self.reduceLRonPlCheckBox]

        self.metricsGroup = QButtonGroup()
        for metric in self.metrics:
            self.metricsGroup.addButton(metric)

        self.callbacksGroup = QButtonGroup()
        for callback in self.callbacks:
            self.callbacksGroup.addButton(callback)

        self.mainFrame.resize(300, 870)
        self.resize(300, 870)

