from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtGui import QFont

class TienXuLy(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        # Ví dụ giao diện cơ bản
        label = QLabel("Trang Tiền Xử Lý Dữ Liệu", self)
        label.setGeometry(100, 100, 300, 50)
        label.setFont(QFont("Arial", 16))
