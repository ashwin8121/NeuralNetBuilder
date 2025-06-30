import os.path
from PyQt6.QtWidgets import QWidget, QFrame, QLabel, QFileDialog
from PyQt6.QtCore import  QMimeData, Qt, QUrl
from src.styles.styles import folderDropWidgetStyle

class FolderDropWidget(QFrame):
    datasetURL = r"D:\Christ Files\7th Sem\Project\Project\dataset\PetImages"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.textLabel = QLabel("Browse \nor\n drag a folder here", self)
        self.textLabel.resize(500, 100)

        self.textLabel.setStyleSheet("border: none;font-size: 15px; color: rgba(220, 200, 200, 80);")
        self.textLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setAcceptDrops(True)
        self.resize(500, 100)
        self.setStyleSheet(folderDropWidgetStyle)


    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
            self.textLabel.setStyleSheet("border: none;font-size: 15px; color: rgba(220, 200, 200, 255);")
        else:
            event.ignore()

    def dragLeaveEvent(self, event):
        self.textLabel.setStyleSheet("border: none;font-size: 15px; color: rgba(220, 200, 200, 80);")

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        url = list(map(lambda x: x.toLocalFile(), urls))[0]
        self.datasetURL = url
        self.textLabel.setText(url)
        self.parent().parent().datasetSelected()
        if os.path.isdir(url):
            print(f"Folder selected: {url}")
        elif os.path.isfile(url):
            print(f"File selected: {url}")

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            url = QFileDialog.getExistingDirectory(self)
            if not url:
                return
            self.datasetURL = url
            self.textLabel.setText(self.datasetURL)
            self.textLabel.setStyleSheet("border: none;font-size: 15px; color: rgba(220, 200, 200, 255);")
            self.parent().parent().datasetSelected()

            # print(self.datasetURL)







