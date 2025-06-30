from PyQt6.QtWidgets import QWidget, QFrame, QPushButton, QLabel, QComboBox, QSpinBox, QFormLayout
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont, QIcon
from seaborn import stripplot
from src.helpers.layerProperties import properties
from src.styles.styles import propertyWindowCloseButtonStyle

from tensorflow.keras.layers import *

class PropertyFrame(QWidget):

    inFrame = None

    def __init__(self, parent, properties=[]):
        super().__init__()
        self.setParent(parent)
        self.mainFrame = QFrame(self)
        closeWindowButton = QPushButton(self.mainFrame)
        closeWindowButton.setIcon(QIcon(r"D:\Christ Files\7th Sem\Project\Project\src\assets\close-button-image.png"))
        closeWindowButton.setIconSize(QSize(12, 12))
        closeWindowButton.setStyleSheet(propertyWindowCloseButtonStyle)
        closeWindowButton.clicked.connect(self.closeWindow)
        closeWindowButton.resize(40, 40)
        closeWindowButton.move(250, 10)
        configurationLabel = QLabel("CONFIGURATION", self)

        configurationLabel.resize(200, 60)
        configurationLabel.move(-5, 0)
        configurationLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        configurationLabel.setFont(QFont("Roboto mono", 14, 10))


        self.formFrame = QFrame(self)
        self.formLayout = QFormLayout()
        self.formFrame.setLayout(self.formLayout)
        self.formFrame.move(15, 60)
        self.formFrame.resize(275, 600)

        self.saveButton = QPushButton("Save", self.mainFrame)
        self.saveButton.resize(200, 60)
        self.saveButton.setFont(QFont("Roboto mono", 14, 10))
        self.saveButton.move(10, 800)
        self.saveButton.clicked.connect(self.saveParams)
        # self.formFrame.setStyleSheet("border: 1px solid rgb(15, 15, 15);")
        self.mainFrame.resize(300, 870)

    def saveParams(self):
        app = self.parent().parent().parent()
        print(app.modelLayers)
        print("From SaveParams Func")
        print(self.layerText)

        match self.layerText:
            case "CONV2D":
                print(self.formLayout.count())
                paramlist = []
                for i in range(0, self.formLayout.count(), 2):
                    label = self.formLayout.itemAt(i).widget().text()
                    widget = self.formLayout.itemAt(i+1).widget()
                    ret = self.getConvValues(label, widget)
                    paramlist.append(ret)
                lay = Conv2D(**dict(paramlist))
                # print(lay)
                app.modelLayers.append(lay)

            case "DENSE":
                print(self.formLayout.count())
                paramlist = []
                for i in range(0, self.formLayout.count(), 2):
                    label = self.formLayout.itemAt(i).widget().text()
                    widget = self.formLayout.itemAt(i + 1).widget()
                    ret = self.getDenseValues(label, widget)
                    paramlist.append(ret)
                lay = Dense(**dict(paramlist))
                # print(lay)
                app.modelLayers.append(lay)

            case "FLATTEN":
                lay = Flatten()
                app.modelLayers.append(lay)

            case "MAXPOOLING2D":
                # print(self.formLayout.count())
                # paramlist = []
                # for i in range(0, self.formLayout.count(), 2):
                #     label = self.formLayout.itemAt(i).widget().text()
                #     widget = self.formLayout.itemAt(i + 1).widget()
                #     ret = self.getDenseValues(label, widget)
                #     paramlist.append(ret)
                lay = MaxPooling2D(strides=2)
                # print(lay)
                app.modelLayers.append(lay)


        print("END of SaveParams Func")

    def closeWindow(self):
        self.parent().closePropertyWindow()
        self.inFrame = False

    def evaluateProperties(self, layerName, properties) -> dict:
        opts = []
        types = []
        values = []
        for name, type, options in properties:
            opts.append(name)
            types.append(type)
            values.append(options.get("values", None))
        config = {"name": layerName, "options": opts, "types": types, "values": values}
        return config

    def setConfigurations(self, layer):
        self.layerText = layer.layerText
        while self.formLayout.count():
            self.formLayout.removeWidget(self.formLayout.itemAt(0).widget())
        props = properties.get(self.layerText, None)
        if not props:
            return
        config = self.evaluateProperties(self.layerText, props)

        layerName = config["name"]
        for optn, type, val in zip(config["options"], config["types"], config["values"]):
            if type == "int":
                widget = QSpinBox()
            elif type == "combobox":
                print(optn, val)
                widget = QComboBox()
                widget.addItems(val)
            else:

                continue
            self.formLayout.addRow(optn, widget)


    def getConvValues(self, param, widget):
        match param:
            case "Filters":
                return "filters", widget.value()
            case "Kernel Size":
                return "kernel_size", int(widget.currentText())
            case "Strides":
                return "strides", (int(widget.value()), int(widget.value()))
            case "Padding":
                return "padding", widget.currentText().lower()
            case "Activation":
                return "activation", widget.currentText().lower()

    def getDenseValues(self, param, widget):
        print(param, widget)
        match param:
            case "Units":
                return "units", widget.value()
            case "Activation":
                return "activation", widget.currentText().lower()