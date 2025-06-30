from PyQt6.QtWidgets import QWidget, QLabel
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import Qt, QUrl, QPoint
from requests import get
from threading import Thread

loadingHTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Loading Screen</title>
    <style>
        body, html {
            height: 100%;
            margin: 0;
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: rgb(35, 35, 35);
        }
        .loading-container {
            text-align: center;
        }
        .spinner {
            border: 16px solid rgb(19, 19, 19);
            border-radius: 50%;
            border-top: 16px solid #3498db;
            width: 80px;
            height: 80px;
            animation: spin 2s linear infinite;
            margin-bottom: 20px;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        .loading-text {
            font-size: 24px;
            color: #eee;
        }
    </style>
</head>
<body>
    <div class="loading-container">
        <div class="spinner"></div>
        <div class="loading-text">Loading...</div>
    </div>
</body>
</html>

"""

notTrainingHTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Model Training Status</title>
    <style>
        body, html {
            height: 100%;
            margin: 0;
            font-family: 'Comic Sans MS', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #333;
            color: white;
            transition: background-color 0.3s, color 0.3s;
        }
        .container {
            text-align: center;
        }
        .emoji {
            font-size: 120px;
            animation: blink 2s infinite;
        }
        @keyframes blink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }
        .text {
            font-size: 28px;
            margin-top: 20px;
        }
        .sassy-comment {
            font-size: 22px;
            margin-top: 10px;
            font-style: italic;
        }
        .snooze {
            font-size: 100px;
            margin-top: 30px;
            animation: bounce 1.5s infinite alternate;
        }
        @keyframes bounce {
            from {
                transform: translateY(0);
            }
            to {
                transform: translateY(-30px);
            }
        }
        .toggle-container {
            position: absolute;
            top: 20px;
            right: 20px;
            display: flex;
            align-items: center;
        }
        .toggle-label {
            font-size: 16px;
            margin-right: 10px;
        }
        .switch {
            position: relative;
            display: inline-block;
            width: 50px;
            height: 24px;
        }
        .switch input {
            display: none;
        }
        .slider {
            position: absolute;
            cursor: pointer;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: #ccc;
            transition: .4s;
            border-radius: 34px;
        }
        .slider:before {
            position: absolute;
            content: "";
            height: 18px;
            width: 18px;
            left: 4px;
            bottom: 3px;
            background-color: white;
            transition: .4s;
            border-radius: 50%;
        }
        input:checked + .slider {
            background-color: #3498db;
        }
        input:checked + .slider:before {
            transform: translateX(26px);
        }

        /* Light mode styles */
        .light-mode {
            background-color: #f0f8ff;
            color: #333;
        }
    </style>
</head>
<body class="dark-mode">
    <div class="container">
        <div class="emoji">😴</div>
        <div class="text">Model Training not yet started</div>
        <div class="sassy-comment">The model is probably snoozing... 💤</div>
        <div class="snooze">💤</div>
    </div>
</body>
</html>
"""

class MonitorWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.webView = QWebEngineView(self)
        self.webView.resize(1920, 1010)
        self.application = None
        self.webView.setHtml(loadingHTML)

    def initiateTensorBoard(self):
        print("Initiating Tensorboard")
        self.webView.setUrl(QUrl("http://127.0.0.1:6006"))


    def keyPressEvent(self, event):
        print(event.key())
        if event.key() == Qt.Key.Key_F5 or event.key() == Qt.Key.Key_R:
            self.webView.reload()
        if event.key() == Qt.Key.Key_B:
            self.webView.back()
        if event.key() == Qt.Key.Key_N:
            self.webView.forward()

