from PySide6.QtWidgets import QWidget, QLabel, QFileDialog, QMessageBox,QTableWidget,QDialog,QTableWidgetItem
from PySide6.QtGui import QFont

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)
import numpy as np
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class Konohen(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.data = None
        self.weights = None
        
        self.importBtn.clicked.connect(self.import_data)
        self.runBtn.clicked.connect(self.run_algorithm)
        self.runBtn.clicked.connect(self.visualize_data)
        self.viewBtn.clicked.connect(self.view_file_data)


    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1032, 759)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.executeTab = QWidget()
        self.executeTab.setObjectName(u"executeTab")
        self.executeTab.setStyleSheet(u"")
        self.label_2 = QLabel(self.executeTab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 60, 141, 31))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.executeTab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(130, 90, 141, 16))
        font1 = QFont()
        font1.setItalic(True)
        self.label_3.setFont(font1)
        self.noiThucThi = QScrollArea(self.executeTab)
        self.noiThucThi.setObjectName(u"noiThucThi")
        self.noiThucThi.setGeometry(QRect(10, 250, 991, 451))
        self.noiThucThi.setStyleSheet(u"border:1px solid;")
        self.noiThucThi.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 989, 449))
        self.noiThucThi.setWidget(self.scrollAreaWidgetContents)
        self.runBtn = QPushButton(self.executeTab)
        self.runBtn.setObjectName(u"runBtn")
        self.runBtn.setGeometry(QRect(150, 200, 121, 24))
        self.runBtn.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid;\n"
"	\n"
"}")
        self.widget = QWidget(self.executeTab)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(510, 70, 120, 80))
        self.widget1 = QWidget(self.executeTab)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(30, 121, 164, 71))
        self.verticalLayout = QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.widget1)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(self.widget1)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.widget2 = QWidget(self.executeTab)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(210, 120, 135, 74))
        self.verticalLayout_2 = QVBoxLayout(self.widget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.epochs = QLineEdit(self.widget2)
        self.epochs.setObjectName(u"epochs")
        self.epochs.setStyleSheet(u"border: 1px solid;")

        self.verticalLayout_2.addWidget(self.epochs)

        self.R = QLineEdit(self.widget2)
        self.R.setObjectName(u"R")
        self.R.setStyleSheet(u"border: 1px solid;")

        self.verticalLayout_2.addWidget(self.R)

        self.a = QLineEdit(self.widget2)
        self.a.setObjectName(u"a")
        self.a.setStyleSheet(u"border: 1px solid;")

        self.verticalLayout_2.addWidget(self.a)

        self.widget3 = QWidget(self.executeTab)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(29, 30, 332, 26))
        self.horizontalLayout_2 = QHBoxLayout(self.widget3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget3)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(11)
        self.label.setFont(font2)

        self.horizontalLayout_2.addWidget(self.label)

        self.importBtn = QPushButton(self.widget3)
        self.importBtn.setObjectName(u"importBtn")
        self.importBtn.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid;\n"
"	\n"
"}")
        self.importBtn.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.importBtn)

        self.viewBtn = QPushButton(self.widget3)
        self.viewBtn.setObjectName(u"viewBtn")
        self.viewBtn.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid;\n"
"	\n"
"}")
        self.viewBtn.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.viewBtn)

        self.tabWidget.addTab(self.executeTab, "")
        self.visualizeTab = QWidget()
        self.visualizeTab.setObjectName(u"visualizeTab")
        self.tabWidget.addTab(self.visualizeTab, "")

        self.horizontalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Ch\u1ea1y Thu\u1eadt to\u00e1n", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Nh\u1eadp c\u00e1c gi\u00e1 tr\u1ecb c\u1ea7n thi\u1ebft:", None))
        self.runBtn.setText(QCoreApplication.translate("Form", u"Th\u1ef1c hi\u1ec7n ph\u00e2n c\u1ee5m", None))
        self.label_4.setText(QCoreApplication.translate("Form", u" Nh\u1eadp s\u1ed1 l\u1ea7n l\u1eb7p Epochs:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u" Nh\u1eadpb\u00e1n k\u00ednh v\u00f9ng l\u00e2n c\u1eadn R:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u" Nh\u1eadp t\u1ed1c \u0111\u1ed9 h\u1ecdc a:", None))
        self.label.setText(QCoreApplication.translate("Form", u"H\u00e3y import data c\u1ee7a b\u1ea1n:", None))
        self.importBtn.setText(QCoreApplication.translate("Form", u"Import", None))
        self.viewBtn.setText(QCoreApplication.translate("Form", u"Xem d\u1eef li\u1ec7u", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.executeTab), QCoreApplication.translate("Form", u"Ch\u1ea1y Thu\u1eadt To\u00e1n", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.visualizeTab), QCoreApplication.translate("Form", u"Tr\u1ef1c Quan ", None))
    # retranslateUi

    import pandas as pd

    def import_data(self):
        # Import file Excel
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx *.xls)")
        if file_path:
            try:
                # Đọc dữ liệu từ file Excel
                df = pd.read_excel(file_path)
                self.data = df.to_numpy()  # Chuyển DataFrame sang NumPy array
                QMessageBox.information(self, "Success", "Data imported successfully!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not load data: {e}")
        else:
            QMessageBox.warning(self, "Warning", "No file selected.")
    def run_algorithm(self):
        # Kiểm tra xem dữ liệu đã được nhập chưa
        if self.data is None:
            QMessageBox.warning(self, "Warning", "Please import data first!")
            return

        try:
            # Lấy thông tin từ giao diện
            epochs_text = self.epochs.text()
            R_text = self.R.text()
            a_text = self.a.text()

            if not epochs_text or not R_text or not a_text:
                raise ValueError("Missing input values!")

            self.epochs = int(epochs_text)
            self.R = float(R_text)
            self.alpha = float(a_text)
        except ValueError:
            QMessageBox.warning(self, "Warning", "Please enter valid numeric values!")
            return

        # Khởi tạo trọng số ban đầu
        num_features = self.data.shape[1]
        num_neurons = 3  # Số lượng neuron
        self.weights = np.random.rand(num_neurons, num_features)

        # Log bước khởi tạo
        self.log_to_scroll_area("Khởi tạo trọng số ban đầu:")
        for i, weight in enumerate(self.weights, 1):
            self.log_to_scroll_area(f"  Neuron {i}: {weight}")

        # Chạy thuật toán Kohonen SOM
        for epoch in range(self.epochs):
            self.log_to_scroll_area(f"\nEpoch {epoch + 1}:")
            for i, x in enumerate(self.data):
                # Tính khoảng cách từ x đến các trọng số
                distances = np.linalg.norm(self.weights - x, axis=1)
                winner_idx = np.argmin(distances)  # Tìm neuron chiến thắng

                # Log thông tin khoảng cách
                self.log_to_scroll_area(f"  Dữ liệu {i + 1}: {x}")
                self.log_to_scroll_area(f"    Khoảng cách đến các neuron: {distances}")
                self.log_to_scroll_area(f"    Neuron chiến thắng: Neuron {winner_idx + 1}")

                # Cập nhật trọng số của neuron chiến thắng
                old_weights = self.weights[winner_idx].copy()
                self.weights[winner_idx] += self.alpha * (x - self.weights[winner_idx])
                self.log_to_scroll_area(f"    Trọng số cũ: {old_weights}")
                self.log_to_scroll_area(f"    Trọng số mới: {self.weights[winner_idx]}")

        QMessageBox.information(self, "Success", "Clustering completed!")
        

    def visualize_data(self):
        if self.data is None:
            QMessageBox.warning(self, "Warning", "Please import data first!")
            return

        # Hiển thị dữ liệu gốc và trọng số
        figure = Figure()
        canvas = FigureCanvas(figure)
        ax = figure.add_subplot(111, projection="3d")

        # Dữ liệu gốc
        ax.scatter(self.data[:, 0], self.data[:, 1], self.data[:, 2], c='blue', label='Data Points')

        # Trọng số sau khi huấn luyện
        if self.weights is not None:
            ax.scatter(self.weights[:, 0], self.weights[:, 1], self.weights[:, 2], c='red', marker='X', s=200, label='Weights')

        ax.set_title("Data Visualization")
        ax.set_xlabel("Feature 1")
        ax.set_ylabel("Feature 2")
        ax.set_zlabel("Feature 3")
        ax.legend()

        # Thêm vào tab "Trực Quan"
        layout = QVBoxLayout(self.visualizeTab)
        layout.addWidget(canvas)
        self.visualizeTab.setLayout(layout)
    def view_file_data(self):
        if self.data is None:
            QMessageBox.warning(self, "Warning", "No data to display! Please import data first.")
            return

        # Hiển thị dữ liệu trong hộp thoại
        dialog = DataDialog(self.data, self)
        dialog.exec()
    def log_to_scroll_area(self, message):
        # Tạo QLabel để hiển thị từng bước
        label = QLabel(message, self.scrollAreaWidgetContents)
        label.setWordWrap(True)  # Để nội dung tự động xuống dòng
        label.setStyleSheet("margin: 5px;")
        
        # Thêm label vào layout của scrollAreaWidgetContents
        layout = self.scrollAreaWidgetContents.layout()
        if not layout:
            layout = QVBoxLayout(self.scrollAreaWidgetContents)
            self.scrollAreaWidgetContents.setLayout(layout)
        layout.addWidget(label)
        
        # Cuộn đến cuối để xem nội dung mới
        self.noiThucThi.verticalScrollBar().setValue(self.noiThucThi.verticalScrollBar().maximum())

class DataDialog(QDialog):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Dữ Liệu Gốc")
        self.resize(600, 400)

        layout = QVBoxLayout(self)

        # Tạo bảng dữ liệu
        table = QTableWidget(self)
        rows, cols = data.shape
        table.setRowCount(rows)
        table.setColumnCount(cols)

        # Đặt tiêu đề cột
        headers = ["Số màu", "Số đường nét", "Số hình khối"]
        table.setHorizontalHeaderLabels(headers[:cols])

        # Thêm dữ liệu vào bảng
        for i in range(rows):
            for j in range(cols):
                table.setItem(i, j, QTableWidgetItem(str(data[i, j])))

        layout.addWidget(table)
