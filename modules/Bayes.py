from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtGui import QFont

class Bayes(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        label = QLabel("Naive Bayes", self)
        label.setGeometry(50, 50, 300, 50)
        label.setFont(QFont("Arial", 16))
