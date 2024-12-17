from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QTabWidget, QWidget)
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtWidgets import (QApplication, QPushButton, QWidget, QFileDialog, QMessageBox, QTableWidget, QTableWidgetItem, QVBoxLayout, QHeaderView,QDialog)


class TienXuLy(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.data = None
        # Thêm QLabel để hiển thị tên file
        self.file_name_label = QLabel(self.tab)
        self.file_name_label.setGeometry(770, 60, 250, 20)
        self.file_name_label.setStyleSheet("font-size: 12px; color: black;")
        self.file_name_label.setText("")
        self.file_name_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.file_name_label.hide()
        # Tạo bảng để hiển thị kết quả
        self.result_table = QTableWidget(self.tab)
        self.result_table.setGeometry(20, 200, 1000, 300)
        self.result_table.setColumnCount(2)
        self.result_table.setHorizontalHeaderLabels(["Tên bước tính", "Giá trị"])
        self.result_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.result_table.verticalHeader().setVisible(False)
        self.result_table.verticalHeader().setDefaultSectionSize(40)
        # Thiết lập header có màu và kích thước lớn
        self.result_table.setStyleSheet("""
            QHeaderView::section {
                background-color: #A8DADC; /* Màu xanh nhạt */
                color: #1D3557; /* Màu chữ đậm */
                font-size: 14px; /* Cỡ chữ lớn hơn */
                font-weight: bold; /* Chữ đậm */
                padding: 6px; /* Khoảng cách padding */
                height: 30px; /* Độ cao cho header */
            }
            QTableWidget {
                font-size: 14px; /* Cỡ chữ mặc định cho bảng */
            }
        """)
        steps = [
            "Giá trị trung bình của X",
            "Giá trị trung bình của Y",
            "Phương sai của X",
            "Phương sai của Y",
            "Hiệp phương sai",
            "Hệ số b1",
            "Hệ số tương quan r"
        ]
        self.result_table.setRowCount(len(steps))
        self.adjust_table_size()
        for i, step in enumerate(steps):
            # Cột tên bước tính (căn giữa)
            step_item = QTableWidgetItem(step)
            step_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.result_table.setItem(i, 0, step_item)

            # Cột giá trị ban đầu để trống (căn giữa)
            empty_item = QTableWidgetItem("")  # Cột giá trị trống
            empty_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.result_table.setItem(i, 1, empty_item)
        
        # Kết nối các nút với hàm xử lý
        self.importBtn.clicked.connect(self.import_data)
        self.viewBtn.clicked.connect(self.view_file_data)
        self.importBtn_2.clicked.connect(self.calculate_correlation)
        self.importBtn_3.clicked.connect(self.switch_to_visualization_tab) 
        

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1042, 687)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QSize(1046, 16777215))
        Form.setStyleSheet(u"font-family:roboto;")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.thuoctinh1cb = QComboBox(self.tab)
        self.thuoctinh1cb.addItem("")
        self.thuoctinh1cb.setObjectName(u"thuoctinh1cb")
        self.thuoctinh1cb.setGeometry(QRect(120, 60, 141, 22))
        self.thuoctinh1cb.setStyleSheet(u"background-color:#FFE6E6;")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 151, 21))
        font = QFont()
        font.setFamilies([u"roboto"])
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.thuoctinh1cb_2 = QComboBox(self.tab)
        self.thuoctinh1cb_2.addItem("")
        self.thuoctinh1cb_2.setObjectName(u"thuoctinh1cb_2")
        self.thuoctinh1cb_2.setGeometry(QRect(460, 60, 141, 22))
        self.thuoctinh1cb_2.setStyleSheet(u"background-color:#FFE6E6;")
        self.importBtn = QPushButton(self.tab)
        self.importBtn.setObjectName(u"importBtn")
        self.importBtn.setGeometry(QRect(780, 10, 121, 41))
        font1 = QFont()
        font1.setFamilies([u"roboto"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.importBtn.setFont(font1)
        self.importBtn.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid;\n"
"	border-radius:7px;\n"
"\n"
"	background-color: #a296ca;\n"
"}")
        self.importBtn.setCheckable(True)
        self.viewBtn = QPushButton(self.tab)
        self.viewBtn.setObjectName(u"viewBtn")
        self.viewBtn.setGeometry(QRect(920, 10, 111, 41))
        self.viewBtn.setFont(font1)
        self.viewBtn.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid;\n"
"	border-radius:7px;\n"
"	background-color: #a296ca;\n"
"}")
        self.viewBtn.setCheckable(True)
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 60, 91, 16))
        self.label_2.setFont(font1)
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(360, 60, 91, 16))
        self.label_3.setFont(font1)
        self.importBtn_2 = QPushButton(self.tab)
        self.importBtn_2.setObjectName(u"importBtn_2")
        self.importBtn_2.setGeometry(QRect(20, 110, 121, 31))
        self.importBtn_2.setFont(font1)
        self.importBtn_2.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid;\n"
"	border-radius:7px;\n"
"	background-color: #a296ca;}")
        self.importBtn_2.setCheckable(True)
        self.importBtn_3 = QPushButton(self.tab)
        self.importBtn_3.setObjectName(u"importBtn_3")
        self.importBtn_3.setGeometry(QRect(160, 110, 121, 31))
        self.importBtn_3.setFont(font1)
        self.importBtn_3.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid;\n"
"	border-radius:7px;\n"
"	background-color: #a296ca;\n"
"}")
        self.importBtn_3.setCheckable(True)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.thuoctinh1cb.setItemText(0, QCoreApplication.translate("Form", u"<ch\u1ecdn thu\u1ed9c t\u00ednh>", None))

        self.label.setText(QCoreApplication.translate("Form", u"Ch\u1ecdn 2 thu\u1ed9c t\u00ednh", None))
        self.thuoctinh1cb_2.setItemText(0, QCoreApplication.translate("Form", u"<ch\u1ecdn thu\u1ed9c t\u00ednh>", None))

        self.importBtn.setText(QCoreApplication.translate("Form", u"T\u1ea3i file ", None))
        self.viewBtn.setText(QCoreApplication.translate("Form", u"Xem d\u1eef li\u1ec7u", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Thu\u1ed9c t\u00ednh X", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Thu\u1ed9c t\u00ednh Y", None))
        self.importBtn_2.setText(QCoreApplication.translate("Form", u"Th\u1ef1c thi", None))
        self.importBtn_3.setText(QCoreApplication.translate("Form", u"Tr\u1ef1c quan", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"Ch\u1ea1y thu\u1eadt to\u00e1n ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Tr\u1ef1c quan", None))
    # retranslateUi
    def import_data(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx *.xls)")
        if file_path:
            try:
                self.data = pd.read_excel(file_path)  # Lưu dữ liệu gốc dạng DataFrame
                file_name = file_path.split("/")[-1]
                self.file_name_label.setText(f"Tên file: {file_name}")
                self.file_name_label.show()

                # Cập nhật comboBox
                columns = self.data.columns.tolist()
                self.thuoctinh1cb.clear()
                self.thuoctinh1cb_2.clear()
                self.thuoctinh1cb.addItems(["<chọn thuộc tính>"] + columns)
                self.thuoctinh1cb_2.addItems(["<chọn thuộc tính>"] + columns)

            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not load data: {e}")
    def calculate_correlation(self):
        if self.data is None:
            QMessageBox.warning(self, "Warning", "Vui lòng tải dữ liệu trước!")
            return

        # Lấy thuộc tính từ comboBox
        attr_x = self.thuoctinh1cb.currentText()
        attr_y = self.thuoctinh1cb_2.currentText()

        # Kiểm tra xem thuộc tính đã được chọn chưa
        if attr_x == "<chọn thuộc tính>" or attr_y == "<chọn thuộc tính>":
            QMessageBox.warning(self, "Warning", "Vui lòng chọn cả hai thuộc tính!")
            return

        # Kiểm tra thuộc tính tồn tại trong dataframe
        if attr_x not in self.data.columns or attr_y not in self.data.columns:
            QMessageBox.critical(self, "Error", "Thuộc tính không tồn tại trong dữ liệu!")
            return

        try:
            x = self.data[attr_x]
            y = self.data[attr_y]

            # Tính các bước
            n = len(x)
            mean_x, mean_y = x.mean(), y.mean()
            variance_x = x.var(ddof=0)
            variance_y = y.var(ddof=0)
            covariance = ((x - mean_x) * (y - mean_y)).sum() / n
            b1 = covariance / variance_x
            r = covariance / (variance_x**0.5 * variance_y**0.5)

            # Hiển thị kết quả dưới dạng bảng
            results = [
                ["Giá trị trung bình của X", mean_x],
                ["Giá trị trung bình của Y", mean_y],
                ["Phương sai của X", variance_x],
                ["Phương sai của Y", variance_y],
                ["Hiệp phương sai", covariance],
                ["Hệ số b1", b1],
                ["Hệ số tương quan r", r]
            ]
            self.show_correlation_table(results)
            
            # Trực quan hóa bằng biểu đồ hồi quy tuyến tính
            self.plot_regression(x, y, b1, mean_x, mean_y)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Lỗi trong tính toán: {e}")


    def show_correlation_table(self, results):
        # Ghi kết quả vào cột thứ 2 của bảng
        for i, (_, value) in enumerate(results):
            value_item = QTableWidgetItem(f"{value:.5f}" if isinstance(value, float) else str(value))
            value_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # Căn giữa giá trị
            self.result_table.setItem(i, 1, value_item)

    def plot_regression(self, x, y, b1, mean_x, mean_y):
        """Vẽ biểu đồ hồi quy tuyến tính"""
        # Kiểm tra và tạo layout cho tab "Trực quan" nếu chưa có
        if not self.tab_2.layout():
            self.tab_2.setLayout(QVBoxLayout())
        
        # Xóa nội dung cũ trên tab "Trực quan"
        layout = self.tab_2.layout()
        while layout.count():
            widget_to_remove = layout.takeAt(0).widget()
            if widget_to_remove:
                widget_to_remove.setParent(None)

        # Tạo biểu đồ
        figure = Figure()
        canvas = FigureCanvas(figure)
        ax = figure.add_subplot(111)

        # Dữ liệu gốc
        ax.scatter(x, y, color="blue", label="Data Points")

        # Đường hồi quy
        regression_line = mean_y + b1 * (x - mean_x)
        ax.plot(x, regression_line, color="red", label="Regression Line")

        # Cài đặt nhãn
        ax.set_title("Hồi quy tuyến tính")
        ax.set_xlabel(x.name)
        ax.set_ylabel(y.name)
        ax.legend()

        # Thêm biểu đồ vào tab "Trực quan"
        layout.addWidget(canvas)


    def view_file_data(self):
        """Hàm hiển thị dữ liệu đã tải."""
        if self.data is None:
            QMessageBox.warning(self, "Warning", "Không có dữ liệu để hiển thị! Vui lòng tải dữ liệu trước.")
            return

        # Tạo hộp thoại hiển thị dữ liệu
        dialog = DataDialog(self.data, self)
        dialog.show()
    def switch_to_visualization_tab(self):
        """Chuyển sang tab trực quan"""
        self.tabWidget.setCurrentIndex(1)
    def adjust_table_size(self):
        row_height = self.result_table.verticalHeader().defaultSectionSize()  # Chiều cao mặc định mỗi dòng
        column_widths = [self.result_table.columnWidth(i) for i in range(self.result_table.columnCount())]  # Lấy chiều rộng cột

        # Chiều cao = (số hàng * chiều cao hàng) + chiều cao của tiêu đề cột
        total_height = row_height * self.result_table.rowCount() + self.result_table.horizontalHeader().height()

        # Chiều rộng = tổng chiều rộng các cột + chiều rộng tiêu đề hàng
        total_width = sum(column_widths) + self.result_table.verticalHeader().width()

        # Cập nhật kích thước bảng
        self.result_table.setFixedHeight(total_height)
        self.result_table.setFixedWidth(total_width)
class DataDialog(QDialog):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Dữ Liệu Gốc")
        self.resize(800, 600)

        # Tạo bố cục chính
        layout = QVBoxLayout(self)

        # Tạo bảng hiển thị dữ liệu
        table = QTableWidget(self)
        rows, cols = data.shape
        table.setRowCount(rows)
        table.setColumnCount(cols)

        # Đặt tiêu đề cột
        headers = list(data.columns)
        table.setHorizontalHeaderLabels(headers)

        # Điền dữ liệu vào bảng
        for i in range(rows):
            for j in range(cols):
                table.setItem(i, j, QTableWidgetItem(str(data.iloc[i, j])))

        # Tự động dãn các cột để hiển thị đầy đủ nội dung
        table.horizontalHeader().setStretchLastSection(True)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setStyleSheet("""
            QHeaderView::section {
                background-color: #E6E6FA; /* Màu tím nhạt */
                color: black; /* Màu chữ */
                border: 1px solid #8A2BE2; /* Viền */
                font-size: 13px;
                font-weight: bold;
                padding: 4px;
            }
        """)
        # Thêm bảng vào bố cục
        layout.addWidget(table)

        # Tạo nút đóng
        close_button = QPushButton("Đóng", self)
        close_button.setFixedSize(100, 30)
        close_button.setStyleSheet("""
            QPushButton {
                background-color: #E6E6FA; /* Màu tím nhạt */
                border: 2px solid #8A2BE2; /* Đường viền màu tím */
                border-radius: 5px; /* Bo tròn góc */
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #D8BFD8; /* Màu tím đậm hơn khi hover */
            }
        """)
        close_button.clicked.connect(self.close)

        # Thêm nút vào bố cục
        layout.addWidget(close_button)
        layout.setAlignment(close_button, Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)
    
