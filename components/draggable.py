from PyQt6.QtWidgets import QWidget, QPushButton, QComboBox
from PyQt6.QtGui import QDrag, QPixmap, QFont
from PyQt6.QtCore import QMimeData, Qt
from src.styles.styles import draggableButtonStyle


class DraggableObject(QWidget):
    insideDragDropArea = False
    def mouseMoveEvent(self, event):
        # print("Called")
        if not event.buttons() == Qt.MouseButton.LeftButton:
            return
        drag = QDrag(self)
        mime = QMimeData()
        drag.setMimeData(mime)
        pixmap = QPixmap(self.size())
        self.render(pixmap)
        drag.setPixmap(pixmap)
        prevStyleSheeet = self.styleSheet()
        drag.exec(Qt.DropAction.MoveAction)
        if self.insideDragDropArea:
            self.setStyleSheet(prevStyleSheeet)


class DraggableButton(QPushButton, DraggableObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet(draggableButtonStyle)


