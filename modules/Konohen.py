from PySide6.QtWidgets import QWidget, QLabel, QFileDialog, QMessageBox,QTableWidget,QDialog,QTableWidgetItem,QVBoxLayout,QComboBox
from PySide6.QtGui import QFont

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QTabWidget, QWidget)
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
        self.runBtn.clicked.connect(self.run_and_visualize)
        self.viewBtn.clicked.connect(self.view_file_data)

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1046, 691)
        Form.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"roboto"])
        Form.setFont(font)
        Form.setStyleSheet(u"font-family: roboto;")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(931, 691))
        self.tabWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tabWidget.setStyleSheet(u"")
        self.executeTab = QWidget()
        self.executeTab.setObjectName(u"executeTab")
        self.executeTab.setStyleSheet(u"")
        self.runBtn = QPushButton(self.executeTab)
        self.runBtn.setObjectName(u"runBtn")
        self.runBtn.setGeometry(QRect(480, 170, 151, 31))
        font1 = QFont()
        font1.setFamilies([u"roboto"])
        font1.setBold(True)
        self.runBtn.setFont(font1)
        self.runBtn.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid;\n"
"	border-radius:7px;\n"
"}")
        self.line = QFrame(self.executeTab)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(550, 240, 2, 421))
        font2 = QFont()
        font2.setFamilies([u"roboto"])
        font2.setBold(False)
        self.line.setFont(font2)
        self.line.setAutoFillBackground(False)
        self.line.setStyleSheet(u"background-color:black;")
        self.line.setFrameShadow(QFrame.Shadow.Plain)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.label_7 = QLabel(self.executeTab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(730, 210, 61, 31))
        font3 = QFont()
        font3.setFamilies([u"roboto"])
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setItalic(False)
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u";")
        self.frame = QFrame(self.executeTab)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(19, 240, 501, 421))
        self.frame.setStyleSheet(u"QFrame {\n"
"	border: 1px solid black;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.noiThucThi = QScrollArea(self.frame)
        self.noiThucThi.setObjectName(u"noiThucThi")
        self.noiThucThi.setStyleSheet(u"")
        self.noiThucThi.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 497, 417))
        self.scrollAreaWidgetContents.setStyleSheet(u"border:none;\n"
"font-size: 13px;\n"
"font-family:roboto;\n"
"color: #4c1c46;")
        self.noiThucThi.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.noiThucThi)

        self.label_8 = QLabel(self.executeTab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(200, 200, 71, 31))
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u";")
        self.label_3 = QLabel(self.executeTab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 20, 191, 31))
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u";")
        self.label_4 = QLabel(self.executeTab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(23, 67, 191, 31))
        font4 = QFont()
        font4.setFamilies([u"roboto"])
        font4.setPointSize(11)
        font4.setBold(True)
        self.label_4.setFont(font4)
        self.label_6 = QLabel(self.executeTab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(23, 140, 151, 31))
        self.label_6.setFont(font4)
        self.label_5 = QLabel(self.executeTab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(23, 103, 241, 31))
        self.label_5.setFont(font4)
        self.R = QLineEdit(self.executeTab)
        self.R.setObjectName(u"R")
        self.R.setGeometry(QRect(280, 110, 61, 21))
        self.R.setStyleSheet(u"border: 1px solid;")
        self.a = QLineEdit(self.executeTab)
        self.a.setObjectName(u"a")
        self.a.setGeometry(QRect(280, 150, 61, 21))
        self.a.setStyleSheet(u"border: 1px solid;")
        self.epochs = QLineEdit(self.executeTab)
        self.epochs.setObjectName(u"epochs")
        self.epochs.setGeometry(QRect(280, 69, 61, 21))
        self.epochs.setStyleSheet(u"border: 1px solid;")
        self.importBtn = QPushButton(self.executeTab)
        self.importBtn.setObjectName(u"importBtn")
        self.importBtn.setGeometry(QRect(770, 20, 121, 41))
        self.importBtn.setFont(font1)
        self.importBtn.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid;\n"
"	border-radius:7px;\n"
"}")
        self.importBtn.setCheckable(True)
        self.viewBtn = QPushButton(self.executeTab)
        self.viewBtn.setObjectName(u"viewBtn")
        self.viewBtn.setGeometry(QRect(910, 20, 111, 41))
        self.viewBtn.setFont(font1)
        self.viewBtn.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid;\n"
"	border-radius:7px;\n"
"}")
        self.viewBtn.setCheckable(True)
        self.tabWidget.addTab(self.executeTab, "")
        self.visualizeTab = QWidget()
        self.visualizeTab.setObjectName(u"visualizeTab")
        self.tabWidget.addTab(self.visualizeTab, "")

        self.horizontalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
        # Trong setupUi
        self.dimensionLabel = QLabel(self.executeTab)
        self.dimensionLabel.setText("Chọn số chiều:")
        self.dimensionLabel.setGeometry(QRect(20, 180, 120, 30))
        self.dimensionLabel.setFont(font4)

        self.dimensionCombo = QComboBox(self.executeTab)
        self.dimensionCombo.setGeometry(QRect(150, 180, 100, 30))
        self.dimensionCombo.addItems(["2D", "3D"])
        self.executeTabLayout = QVBoxLayout(self.executeTab)
        self.executeTab.setLayout(self.executeTabLayout)

        # Khởi tạo các combobox
        self.attributeCombos = []
        for i in range(3):  # Tối đa 3 chiều
            combo = QComboBox(self.executeTab)
            combo.setVisible(False)  # Mặc định ẩn
            self.attributeCombos.append(combo)
            self.executeTabLayout.addWidget(combo)  # Thêm vào layout

        self.dimensionCombo.currentIndexChanged.connect(self.update_attribute_combos)


    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.runBtn.setText(QCoreApplication.translate("Form", u"Th\u1ef1c hi\u1ec7n ph\u00e2n c\u1ee5m", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"K\u1ebft qu\u1ea3 ", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Qu\u00e1 tr\u00ecnh", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Nh\u1eadp c\u00e1c gi\u00e1 tr\u1ecb c\u1ea7n thi\u1ebft:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u" Nh\u1eadp s\u1ed1 l\u1ea7n l\u1eb7p Epochs:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u" Nh\u1eadp t\u1ed1c \u0111\u1ed9 h\u1ecdc a:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u" Nh\u1eadp b\u00e1n k\u00ednh v\u00f9ng l\u00e2n c\u1eadn R:", None))
        self.importBtn.setText(QCoreApplication.translate("Form", u"T\u1ea3i file ", None))
        self.viewBtn.setText(QCoreApplication.translate("Form", u"Xem d\u1eef li\u1ec7u", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.executeTab), QCoreApplication.translate("Form", u"Ch\u1ea1y Thu\u1eadt To\u00e1n", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.visualizeTab), QCoreApplication.translate("Form", u"Tr\u1ef1c Quan ", None))
    # retranslateUi


    import pandas as pd
    def update_attribute_combos(self):
        if self.data is None:
            QMessageBox.warning(self, "Warning", "Hãy tải dữ liệu trước!")
            return

        selected_dim = self.dimensionCombo.currentText()
        num_dims = 2 if selected_dim == "2D" else 3

        # Hiển thị đúng số combobox
        for i, combo in enumerate(self.attributeCombos):
            if i < num_dims:
                combo.setVisible(True)
            else:
                combo.setVisible(False)

        # Cập nhật danh sách các thuộc tính trong combobox
        columns = list(self.data.columns)  # Lấy tên cột từ DataFrame
        for combo in self.attributeCombos:
            combo.clear()
            combo.addItems(columns)
    def process_selected_attributes(self):
        if self.data is None:
            QMessageBox.warning(self, "Warning", "Hãy tải dữ liệu trước!")
            return

        selected_columns = [combo.currentText() for combo in self.attributeCombos if combo.isVisible()]
        if len(selected_columns) < 2:
            QMessageBox.warning(self, "Warning", "Hãy chọn ít nhất 2 thuộc tính!")
            return

        # Lọc dataset chỉ với các thuộc tính được chọn
        self.filtered_data = self.data[selected_columns].to_numpy()

        QMessageBox.information(self, "Success", f"Đã chọn các thuộc tính: {', '.join(selected_columns)}")

    def import_data(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx *.xls)")
        if file_path:
            try:
                self.data = pd.read_excel(file_path)  # Lưu dữ liệu gốc dạng DataFrame
                self.update_attribute_combos()  # Cập nhật combobox
                self.filePathLabel.setText(f"File: {file_path}")  # Hiển thị đường dẫn file
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not load data: {e}")


    

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

        if self.weights is None:
            QMessageBox.warning(self, "Warning", "Please run the SOM algorithm first!")
            return

        # Tạo figure cho plot 3D
        figure = Figure()
        canvas = FigureCanvas(figure)
        ax = figure.add_subplot(111, projection='3d')

        # Vẽ dữ liệu gốc
        ax.scatter(
            self.data[:, 0], self.data[:, 1], self.data[:, 2],
            c='blue', label='Data Points'
        )

        # Vẽ trọng số (weights)
        ax.scatter(
            self.weights[:, 0], self.weights[:, 1], self.weights[:, 2],
            c='red', marker='X', s=200, label='Weights (Neurons)'
        )

        # Thiết lập tiêu đề và nhãn
        ax.set_title("3D Visualization of SOM")
        ax.set_xlabel("Số màu")
        ax.set_ylabel("Số đường nét")
        ax.set_zlabel("Số hình khối")
        ax.legend()

        # Xóa layout cũ nếu có
        if self.visualizeTab.layout():
            for i in reversed(range(self.visualizeTab.layout().count())):
                self.visualizeTab.layout().itemAt(i).widget().setParent(None)
        else:
            self.visualizeTab.setLayout(QVBoxLayout())

        # Thêm plot 3D vào giao diện
        self.visualizeTab.layout().addWidget(canvas)
    def run_and_visualize(self):
        # Chạy thuật toán Kohonen SOM
        self.run_algorithm()

        # Hiển thị kết quả trực quan
        self.visualize_data()

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
