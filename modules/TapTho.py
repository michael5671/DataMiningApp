from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtGui import QFont

class TapTho(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        label = QLabel("Tập Thô", self)
        label.setGeometry(50, 50, 300, 50)
        label.setFont(QFont("Arial", 16))
