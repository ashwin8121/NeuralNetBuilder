from pickletools import optimize

from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtWidgets import QFrame, QWidget, QApplication, QTableWidget, QTableWidgetItem, QSplashScreen, QVBoxLayout, \
    QLabel, QPushButton, QGridLayout
from PyQt6.QtTextToSpeech import QTextToSpeech
import os
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys
import pandas as pd

# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit,  QFormLayout
#
#
# class MainWindow(QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         self.setWindowTitle('Sign Up Form')
#
#         layout = QFormLayout()
#         print(layout.spacing())
#         layout.setSpacing(150)
#         self.setLayout(layout)
#
#         layout.addRow('Name:', QLineEdit(self))
#         layout.addRow('Email:', QLineEdit(self))
#         layout.addRow('Password:', QLineEdit(self, echoMode=QLineEdit.EchoMode.Password))
#         layout.addRow('Confirm Password:', QLineEdit(self, echoMode=QLineEdit.EchoMode.Password))
#         layout.addRow('Phone:', QLineEdit(self))
#
#         layout.addRow(QPushButton('Sign Up'))
#
#         # show the window
#         self.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     sys.exit(app.exec())

# import sys
# from PyQt6.QtCore import Qt, QPoint
# from PyQt6.QtGui import QPainter, QPen, QPixmap
# from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QFrame
#
#
# class PaintFrame(QFrame):
#     def __init__(self):
#         super().__init__()
#         self.setFrameStyle(QFrame.Shape.Box | QFrame.Shadow.Raised)
#         self.setMouseTracking(True)
#         self.is_drawing = False
#         self.last_point = QPoint()
#         self.image = QPixmap(self.size())  # Create an off-screen image to draw on
#         self.image.fill(Qt.GlobalColor.white)  # Start with a white background
#
#     def mousePressEvent(self, event):
#         if event.button() == Qt.MouseButton.LeftButton:
#             self.is_drawing = True
#             self.last_point = event.position().toPoint()
#
#     def mouseMoveEvent(self, event):
#         if self.is_drawing:
#             current_point = event.position().toPoint()
#
#             # Draw on the image
#             painter = QPainter(self.image)
#             painter.setPen(QPen(Qt.GlobalColor.black, 5, Qt.PenStyle.SolidLine))
#             painter.drawLine(self.last_point, current_point)
#
#             self.last_point = current_point
#             self.update()  # Trigger a repaint to display the image
#
#     def mouseReleaseEvent(self, event):
#         if event.button() == Qt.MouseButton.LeftButton:
#             self.is_drawing = False
#
#     def paintEvent(self, event):
#         # Paint the image onto the widget
#         painter = QPainter(self)
#         painter.drawPixmap(self.rect(), self.image)
#
#
# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         layout = QVBoxLayout()
#
#         # Label
#         self.label = QLabel('Draw by holding the left mouse button and moving the cursor.')
#         layout.addWidget(self.label)
#
#         # Frame for drawing
#         self.frame = PaintFrame()
#         layout.addWidget(self.frame)
#
#         self.setLayout(layout)
#         self.setWindowTitle('Paint on Frame Example')
#         self.setFixedSize(420, 450)  # Set window size
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())


# from PyQt6.QtWidgets import QApplication, QMainWindow, QFrame
# from PyQt6.QtGui import QPainter, QPen
# from PyQt6.QtCore import Qt
#
#
# class GridFrame(QFrame):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setStyleSheet("background-color: white;")
#
#     def paintEvent(self, event):
#         painter = QPainter(self)
#         pen = QPen(Qt.GlobalColor.black, 1, Qt.PenStyle.SolidLine)
#         painter.setPen(pen)
#
#         # Define grid size
#         grid_size = 50
#
#         # Draw horizontal lines
#         for i in range(0, self.width(), grid_size):
#             painter.drawLine(i, 0, i, self.height())
#
#         # Draw vertical lines
#         for j in range(0, self.height(), grid_size):
#             painter.drawLine(0, j, self.width(), j)
#
#         painter.end()
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         # Create a custom QFrame where the grid will be drawn
#         self.frame = GridFrame(self)
#
#         # Set the frame as the central widget
#         self.setCentralWidget(self.frame)
#
#
# # Run the application
# app = QApplication([])
# window = MainWindow()
# window.show()
# app.exec()


# import sys
#
# from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("My App")
#
#         button = QPushButton("Press me for a dialog!")
#         button.clicked.connect(self.button_clicked)
#         self.setCentralWidget(button)
#
#
#
#
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()



# class Main(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.mainFrame = QFrame(self)
#         self.mainFrame.setGeometry(20, 40, 1880, 950)
#         self.mainLayout = QVBoxLayout()
#
#         self.table = QTableWidget()
#         data = pd.read_csv(r"D:\Christ Files\Neuron Club\wine.csv")
#         print(data)
#
#
#         self.mainLayout.addWidget(self.table)
#         self.mainFrame.setLayout(self.mainLayout)
#         self.showMaximized()
#
#     def keyPressEvent(self, event):
#         if event.key() == Qt.Key.Key_Escape:
#             self.destroy(True)
#             exit(-1)
#
# app = QApplication([])
# e = Main()
# app.exec()



# class Main(QWidget):
#     clicked = False
#     doubleClicked = False
#     startX = 0
#     startY = 0
#     def __init__(self):
#         super().__init__()
#         self.clickcount = 0
#
#         self.selectFrame = QFrame(self)
#         self.selectFrame.setGeometry(QRect(self.startX, self.startY, 0, 0))
#         self.selectFrame.setStyleSheet("background-color: rgba(34, 101, 220, 80); border: 1px solid rgb(34, 101, 220);")
#         self.show()
#
#     def keyPressEvent(self, event):
#         if event.key() == Qt.Key.Key_Escape:
#             self.destroy(True)
#             exit(0)
#
#     def mouseDoubleClickEvent(self, event):
#         if event.button() == Qt.MouseButton.LeftButton:
#             self.doubleClicked = True
#             self.startX, self.startY = event.pos().x(), event.pos().y()
#             # print("Double Click Start Position:", event.pos().x(), event.pos().y())
#
#     def mousePressEvent(self, event):
#         if self.startX or self.startY:
#             return
#         if event.button() == Qt.MouseButton.LeftButton:
#             self.clicked = True
#             self.startX, self.startY = event.pos().x(), event.pos().y()
#             # print("Single Click Start Position:", event.pos().x(), event.pos().y())
#
#     def mouseMoveEvent(self, event):
#         if self.doubleClicked:
#             self.clearTerminal()
#             # print("Double Click Start Position:", self.startX, self.startY)
#             # print("Double Click and Drag event at: ", event.pos().x(), event.pos().y())
#         else:
#             self.clearTerminal()
#             # print("Single Click Start Position:", self.startX, self.startY)
#             # print("Single Click and Drag event at: ", event.pos().x(), event.pos().y())
#             self.selectFrame.setGeometry(self.startX, self.startY, event.pos().x() - self.startX, event.pos().y() - self.startY)
#
#     def mouseReleaseEvent(self, event):
#         self.doubleClicked = False
#         self.startX, self.startY = 0, 0
#         self.selectFrame.setGeometry(QRect(self.startX, self.startY, 0, 0))
#         self.clearTerminal()
#
#     @staticmethod
#     def clearTerminal():
#         # return
#         os.system("cls")


# class Main(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.button = QPushButton("Hello world", self)
#         self.button.setIcon(QIcon(r"D:\Christ Files\7th Sem\Project\Project\assets\close-button-image.png"))
#         self.button.setIconSize(QSize(30, 30))
#         self.button.clicked.connect(lambda : self.button.setText(""))
#         self.show()
#
#
#
# app = QApplication([])
# e = Main()
# app.exec()
#
#

# from PyQt6.QtCore import QTimer, QPoint, QEasingCurve
# from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout
# from PyQt6.QtGui import QTransform, QPainter
# import sys
#
# class RotatableButton(QPushButton):
#     def __init__(self, text):
#         super().__init__(text)
#         self.angle = 0
#
#     def rotate_button(self, angle):
#         self.angle = angle
#         self.update()
#
#     def paintEvent(self, event):
#         painter = QPainter(self)
#         transform = QTransform()
#         transform.translate(self.width() / 2, self.height() / 2)
#         transform.rotate(self.angle)
#         transform.translate(-self.width() / 2, -self.height() / 2)
#         painter.setTransform(transform)
#         super().paintEvent(event)
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Button Rotation Animation")
#         self.resize(300, 300)
#
#         self.button = RotatableButton("Rotate Me")
#         self.button.clicked.connect(self.start_animation)
#
#         layout = QVBoxLayout()
#         layout.addWidget(self.button)
#         self.setLayout(layout)
#
#         self.timer = QTimer()
#         self.timer.timeout.connect(self.animate_rotation)
#         self.duration = 1000  # Duration of the animation in milliseconds
#         self.start_angle = 0
#         self.end_angle = 360
#         self.current_time = 0
#         self.interval = 16  # Timer interval for smooth animation (60 FPS)
#         self.easing_curve = QEasingCurve(QEasingCurve.Type.InOutCubic)
#
#     def start_animation(self):
#         self.current_time = 0
#         self.timer.start(self.interval)
#
#     def animate_rotation(self):
#         # Calculate progress ratio
#         progress = self.current_time / self.duration
#         if progress >= 1.0:
#             # Stop the timer when the animation is done
#             self.timer.stop()
#             self.button.rotate_button(self.end_angle)
#             return
#
#         # Calculate the eased angle based on the progress
#         eased_progress = self.easing_curve.valueForProgress(progress)
#         angle = self.start_angle + eased_progress * (self.end_angle - self.start_angle)
#         self.button.rotate_button(angle)
#
#         # Increment current time by the timer interval
#         self.current_time += self.interval
#
# app = QApplication(sys.argv)
# window = Window()
# window.show()
# sys.exit(app.exec())


# import sys
# from PyQt6.QtCore import Qt, QThread, pyqtSignal
# from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QProgressBar
# from src.helpers.datasetLoader import getImageDatasetGenerator
#
#
# class LoadingScreen(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
#         self.setFixedSize(300, 100)
#         self.setStyleSheet("background-color: #2E2E2E; color: white;")
#
#         layout = QVBoxLayout()
#         label = QLabel("Loading dataset...")
#         label.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         layout.addWidget(label)
#
#         self.progress_bar = QProgressBar()
#         self.progress_bar.setRange(0, 0)  # Indeterminate progress
#         layout.addWidget(self.progress_bar)
#
#         self.setLayout(layout)
#
#
# class DatasetLoader(QThread):
#     """A QThread to load the dataset in the background."""
#     loading_finished = pyqtSignal()  # Signal to notify when loading is done
#
#     def run(self):
#         import time  # Simulate long-running task
#         # time.sleep(50)  # Simulating dataset loading
#         self.dataset = getImageDatasetGenerator(r"D:\Christ Files\7th Sem\Project\Project\dataset\PetImages")
#         self.loading_finished.emit()  # Emit signal when done
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("PyQt6 Loading Screen Example")
#         self.setGeometry(100, 100, 400, 300)
#
#         self.label = QLabel("Main Application", self)
#         self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         self.setCentralWidget(self.label)
#
#         loadbutton = QPushButton("Load Dataset", self)
#         loadbutton.clicked.connect(self.load_dataset)
#
#         # Show loading screen and start loading dataset
#         self.loading_screen = LoadingScreen()
#         # self.loading_screen.show()
#         # self.load_dataset()
#
#     def load_dataset(self):
#         """Start dataset loading in a separate thread."""
#         self.loading_screen.show()
#         self.thread = DatasetLoader()
#         self.thread.loading_finished.connect(self.on_loading_finished)
#         self.thread.start()
#
#
#     def on_loading_finished(self):
#         """Close the loading screen and proceed."""
#         self.loading_screen.close()
#         print(self.thread.dataset)
#         self.label.setText("Dataset Loaded!")
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())
#

# from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel
# from PyQt6.QtCore import Qt, QPropertyAnimation, pyqtProperty
# from PyQt6.QtGui import QTransform, QPixmap, QPainter
#
#
# class RotatingIconWidget(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.is_open = False
#
#         # Layout
#         self.layout = QVBoxLayout(self)
#         self.setLayout(self.layout)
#
#         # Button to toggle dropdown
#         self.toggle_button = QPushButton("Toggle Menu")
#         self.toggle_button.clicked.connect(self.toggle_menu)
#         self.layout.addWidget(self.toggle_button)
#
#         # Rotating icon (custom QLabel)
#         self.icon_label = RotatingLabel("↓")
#         self.layout.addWidget(self.icon_label)
#
#         # Dropdown menu (can be replaced with any widget)
#         self.dropdown_menu = QLabel("Menu Content")
#         self.dropdown_menu.setVisible(False)
#         self.layout.addWidget(self.dropdown_menu)
#
#         # Animation setup
#         self.animation = QPropertyAnimation(self.icon_label, b"rotation")
#         self.animation.setDuration(300)  # 300 ms animation duration
#
#     def toggle_menu(self):
#         self.is_open = not self.is_open
#         self.dropdown_menu.setVisible(self.is_open)
#
#         # Rotate icon
#         start_angle = 0 if self.is_open else 180
#         end_angle = 180 if self.is_open else 0
#         self.animation.setStartValue(start_angle)
#         self.animation.setEndValue(end_angle)
#         self.animation.start()
#
#
# class RotatingLabel(QLabel):
#     def __init__(self, text, parent=None):
#         super().__init__(text, parent)
#         self._rotation = 0
#
#     # Property for rotation
#     @pyqtProperty(float)
#     def rotation(self):
#         return self._rotation
#
#     @rotation.setter
#     def rotation(self, value):
#         self._rotation = value
#         self.update()
#
#     def paintEvent(self, event):
#         painter = QPainter(self)
#         transform = QTransform()
#         transform.translate(self.width() / 2, self.height() / 2)  # Center of rotation
#         transform.rotate(self._rotation)
#         transform.translate(-self.width() / 2, -self.height() / 2)  # Undo centering
#         painter.setTransform(transform)
#         super().paintEvent(event)
#
#
# if __name__ == "__main__":
#     from PyQt6.QtWidgets import QApplication
#
#     app = QApplication([])
#
#     # Main widget
#     widget = RotatingIconWidget()
#     widget.resize(200, 150)
#     widget.show()
#
#     app.exec()

# class Main(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.mainframe = QFrame(self)
#         self.mainframe.resize(640, 480)
#         self.mainframe.setStyleSheet("border: 1px solid white;")
#         self.layout = QGridLayout()
#         self.mainframe.setLayout(self.layout)
#         button = QPushButton("click Me", self)
#         button.clicked.connect(lambda : self.displayItems("asdfghjklkjhgf"))
#         button.move(270, 500)
#         self.resize(640, 550)
#         self.show()
#
#     def displayItems(self, labels=[]):
#         for i, item in enumerate(labels):
#             label = QLabel(item)
#             label.resize(120, 120)
#             label.setAlignment(Qt.AlignmentFlag.AlignCenter)
#             self.layout.addWidget(label, i // 3, i % 3)
#         print(self.layout.count())
#
#
#     def keyPressEvent(self, event):
#         if event.key() == Qt.Key.Key_Escape:
#             self.close()
#
#
# app = QApplication([])
# e = Main()
#
# sys.exit(app.exec())


# import tensorflow as tf
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import *
# from tensorflow.keras.optimizers import Adam
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from tensorflow.keras.callbacks import TensorBoard
# from tensorflow.keras.datasets import mnist
#
# (x_train, y_train), (x_test, y_test) = mnist.load_data()
# print(x_train.shape)
# x_train = x_train.reshape(-1, 784, 1)
#
#
# model =  Sequential([
#     Dense(64, activation="relu", input_shape=[784, 1]),
#     Dense(1, activation="softmax")
# ])
#
# model.compile(optimizer=Adam(learning_rate=1e-3), metrics=["accuracy"], loss="categorical_crossentropy")
#
# tb = TensorBoard(log_dir=r"D://logs")
#
# hist = model.fit(x_train, y_train, epochs=10, callbacks=[tb])

import tensorflow as tf
from tensorflow.keras.callbacks import TensorBoard
import os

# Load MNIST dataset
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

# Preprocess the data
# Normalize the pixel values to be between 0 and 1 by dividing by 255.0
train_images = train_images / 255.0
test_images = test_images / 255.0

# Reshape the data to include a single channel (grayscale)
train_images = train_images.reshape((train_images.shape[0], 28, 28, 1))
test_images = test_images.reshape((test_images.shape[0], 28, 28, 1))

# Create a model
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Set up a TensorBoard callback
log_dir = "D:/logs"
os.makedirs(log_dir, exist_ok=True)
tensorboard_callback = TensorBoard(log_dir=log_dir)

# Train the model with the TensorBoard callback
model.fit(train_images, train_labels, epochs=10,
          validation_data=(test_images, test_labels),
          callbacks=[tensorboard_callback])

# After training, TensorBoard will be logging the metrics

