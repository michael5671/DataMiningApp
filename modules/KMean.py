
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTabWidget, QWidget)
from PySide6.QtWidgets import (QApplication, QPushButton, QWidget, QFileDialog, QMessageBox, QTableWidget, QTableWidgetItem, QVBoxLayout, QHeaderView, QDialog, QLabel,QComboBox,QFrame, QScrollArea)
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class KMean(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.importBtn.clicked.connect(self.import_data)
        self.viewBtn.clicked.connect(self.view_file_data)
        self.importBtn_2.clicked.connect(self.execute_kmeans)
        self.trucQuanBtn.clicked.connect(self.show_visualization)
        self.file_name_label = QLabel(self.tab)
        self.file_name_label.setGeometry(770, 90, 250, 20)  # Vị trí dưới nút
        self.file_name_label.setStyleSheet("font-size: 12px; color: black;")
        self.file_name_label.setText("")  # Đặt trống ban đầu
        self.file_name_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.file_name_label.hide()
        self.data = None
        self.centroids = None
        self.iteration = 0
        self.kmeans_results = []

        self.result_layout = QVBoxLayout(self.ketQua)
        self.result_layout.setContentsMargins(0, 0, 0, 0)  # Không có lề
        self.result_layout.setSpacing(10)  # Khoảng cách giữa các mục
        self.ketQua.setLayout(self.result_layout)
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1046, 691)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(1046, 691))
        self.tabWidget.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(12)
        font.setWeight(QFont.DemiBold)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(u"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.tab.setFont(font1)
        self.importBtn = QPushButton(self.tab)
        self.importBtn.setObjectName(u"importBtn")
        self.importBtn.setGeometry(QRect(780, 20, 121, 41))
        font2 = QFont()
        font2.setFamilies([u"roboto"])
        font2.setPointSize(11)
        font2.setWeight(QFont.DemiBold)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        self.importBtn.setFont(font2)
        self.importBtn.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid;\n"
"	border-radius:7px;\n"
"\n"
"	background-color: #a296ca;\n"
"}")
        self.importBtn.setCheckable(True)
        self.viewBtn = QPushButton(self.tab)
        self.viewBtn.setObjectName(u"viewBtn")
        self.viewBtn.setGeometry(QRect(920, 20, 111, 41))
        self.viewBtn.setFont(font2)
        self.viewBtn.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid;\n"
"	border-radius:7px;\n"
"	background-color: #a296ca;\n"
"}")
        self.viewBtn.setCheckable(True)
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 40, 191, 21))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        self.label.setFont(font3)
        self.importBtn_2 = QPushButton(self.tab)
        self.importBtn_2.setObjectName(u"importBtn_2")
        self.importBtn_2.setGeometry(QRect(20, 100, 121, 31))
        self.importBtn_2.setFont(font2)
        self.importBtn_2.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid;\n"
"	border-radius:7px;\n"
"\n"
"	background-color: #a296ca;\n"
"}")
        self.importBtn_2.setCheckable(True)
        self.lineEdit = QLineEdit(self.tab)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(140, 40, 71, 22))
        self.lineEdit.setStyleSheet(u"border: 1px solid black;")
        self.trucQuanBtn = QPushButton(self.tab)
        self.trucQuanBtn.setObjectName(u"trucQuanBtn")
        self.trucQuanBtn.setGeometry(QRect(150, 100, 121, 31))
        self.trucQuanBtn.setFont(font2)
        self.trucQuanBtn.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid;\n"
"	border-radius:7px;\n"
"\n"
"	background-color: #a296ca;\n"
"}")
        self.trucQuanBtn.setCheckable(True)
        self.scrollArea = QScrollArea(self.tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(20, 160, 1001, 491))
        self.scrollArea.setMaximumSize(QSize(1041, 491))
        self.scrollArea.setWidgetResizable(True)
        self.ketQua = QWidget()
        self.ketQua.setObjectName(u"ketQua")
        self.ketQua.setGeometry(QRect(0, 0, 999, 489))
        self.scrollArea.setWidget(self.ketQua)
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
        self.importBtn.setText(QCoreApplication.translate("Form", u"T\u1ea3i file ", None))
        self.viewBtn.setText(QCoreApplication.translate("Form", u"Xem d\u1eef li\u1ec7u", None))
        self.label.setText(QCoreApplication.translate("Form", u"Nh\u1eadp s\u1ed1 c\u1ee5m:", None))
        self.importBtn_2.setText(QCoreApplication.translate("Form", u"Th\u1ef1c thi", None))
        self.trucQuanBtn.setText(QCoreApplication.translate("Form", u"Tr\u1ef1c quan", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"Ch\u1ea1y thu\u1eadt to\u00e1n ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Tr\u1ef1c quan", None))
    # retranslateUi

    def import_data(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx *.xls)")
        if file_path:
            try:
                self.data = pd.read_excel(file_path)  # Lưu dữ liệu gốc dạng DataFrame
                # Hiển thị tên file dưới nút
                file_name = file_path.split("/")[-1]  # Lấy tên file từ đường dẫn
                self.file_name_label.setText(f"Tên file: {file_name}")
                self.file_name_label.show()  # Hiển thị label
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not load data: {e}")

    def view_file_data(self):
        """Hàm hiển thị dữ liệu đã tải."""
        if self.data is None:
            QMessageBox.warning(self, "Warning", "Không có dữ liệu để hiển thị! Vui lòng tải dữ liệu trước.")
            return

        # Tạo hộp thoại hiển thị dữ liệu
        dialog = DataDialog(self.data, self)
        dialog.show()
    def execute_kmeans(self):
        if self.data is None:
            QMessageBox.warning(self, "Cảnh báo", "Không có dữ liệu để phân cụm.")
            return
        try:
            k = int(self.lineEdit.text())
            if k <= 0:
                raise ValueError("Số cụm phải lớn hơn 0.")
            data_points = self.data.select_dtypes(include=[np.number]).values
            if data_points.shape[1] < 2:
                QMessageBox.warning(self, "Cảnh báo", "Dữ liệu cần ít nhất 2 cột số để phân cụm.")
                return

            # Reset layout kết quả
            for i in reversed(range(self.result_layout.count())):
                widget = self.result_layout.takeAt(i).widget()
                if widget:
                    widget.deleteLater()

            # Khởi tạo tâm cụm
            np.random.seed(0)
            self.centroids = data_points[np.random.choice(len(data_points), k, replace=False)]
            self.iteration = 0

            # Gọi hàm kmeans_iteration
            self.kmeans_iteration(data_points, k)
        except ValueError as ve:
            QMessageBox.critical(self, "Lỗi", str(ve))

    def kmeans_iteration(self, data_points, k):
        while True:
            self.iteration += 1
            clusters = [[] for _ in range(k)]
            distances = []

            # Phân cụm
            for point in data_points:
                dists = [np.linalg.norm(point - centroid) for centroid in self.centroids]
                cluster_idx = np.argmin(dists)
                clusters[cluster_idx].append(point)
                distances.append(dists)

            # Tạo kết quả cho phân hoạch hiện tại
            result = pd.DataFrame({
                'x1': data_points[:, 0],
                'x2': data_points[:, 1],
                **{f'Khoảng cách đến C{i+1}': [d[i] for d in distances] for i in range(k)},
                'Cluster': [int(np.argmin(d) + 1) for d in distances]  # Ép kiểu Cluster về int
            })
            # Hiển thị kết quả
            self.display_iteration_result(result, clusters, self.iteration)

            # Cập nhật tâm cụm
            new_centroids = np.array([np.mean(cluster, axis=0) if cluster else self.centroids[i] for i, cluster in enumerate(clusters)])
            if np.allclose(self.centroids, new_centroids):
                final_label = QLabel("=== Hội tụ: Tâm cụm không thay đổi, thuật toán dừng ===")
                final_label.setStyleSheet("font-weight: bold; color: green;")   
                self.result_layout.addWidget(final_label)
                break
            self.centroids = new_centroids


    def display_iteration_result(self, result, clusters, iteration):
        # Add iteration header
        iteration_header = QLabel(f"Phân hoạch U_{iteration}")
        iteration_header.setStyleSheet("font-size: 14px; font-weight: bold;")
        self.result_layout.addWidget(iteration_header)

        # Add table with results
        table = QTableWidget()
        table.setColumnCount(len(result.columns))
        table.setRowCount(len(result))
        table.setHorizontalHeaderLabels(result.columns)
        for col in range(len(result.columns)):
            table.setColumnWidth(col, 150)  # Thiết lập độ rộng cột lớn hơn (150px)
        # Làm tròn số trong DataFrame trước khi hiển thị
        rounded_result = result.round(2)
        for row in range(len(rounded_result)):
            for col in range(len(rounded_result.columns)):
                value = rounded_result.iloc[row, col]
                if isinstance(value, float) and value.is_integer():
                    value = int(value)  # Ép giá trị float thành int nếu là số nguyên
                table.setItem(row, col, QTableWidgetItem(str(value)))
        table.horizontalHeader().setStyleSheet("""
        QHeaderView::section {
            background-color: #A8DADC; /* Màu nền */
            color: black;              /* Màu chữ */
            font-size: 14px;           /* Cỡ chữ */
            font-weight: bold;         /* In đậm */
            padding: 5px;              /* Khoảng cách */
            border: 1px solid #457B9D; /* Viền */
        }
    """)
       
        self.result_layout.addWidget(table)
    
        # Add centroids
        centroids_label = QLabel("Tâm cụm mới:\n" + "\n".join(
            [f"Tâm cụm {i+1}: [{', '.join(f'{val:.2f}' for val in centroid)}]" 
            for i, centroid in enumerate(self.centroids)]
        ))
        centroids_label.setStyleSheet("font-size: 12px;")
        self.result_layout.addWidget(centroids_label)
    def show_visualization(self):
        if self.data is None or self.centroids is None:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng thực thi KMeans trước khi trực quan hóa.")
            return

        # Chuyển sang tab trực quan
        self.tabWidget.setCurrentIndex(1)

        # Kiểm tra và khởi tạo layout nếu chưa có
        if not self.tab_2.layout():
            layout = QVBoxLayout(self.tab_2)
            self.tab_2.setLayout(layout)

        # Xóa các widget cũ trong tab trực quan
        for i in reversed(range(self.tab_2.layout().count())):
            widget = self.tab_2.layout().takeAt(i).widget()
            if widget:
                widget.deleteLater()

        # Dữ liệu cần thiết
        data_points = self.data.select_dtypes(include=[np.number]).values
        clusters = [np.argmin([np.linalg.norm(point - centroid) for centroid in self.centroids]) for point in data_points]
        centroids = np.array(self.centroids)

        # Chuẩn bị màu sắc cho các cụm
        colors = ['blue', 'green', 'orange', 'purple', 'cyan', 'pink']

        # Tạo Figure và vẽ biểu đồ
        fig = Figure()
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)

        # Vẽ các điểm dữ liệu theo từng cụm
        for cluster_idx in range(len(self.centroids)):
            cluster_points = data_points[np.array(clusters) == cluster_idx]
            color = colors[cluster_idx % len(colors)]  # Lặp lại màu nếu số cụm > số màu
            ax.scatter(cluster_points[:, 0], cluster_points[:, 1], color=color, label=f'Cụm {cluster_idx + 1}', s=50)

        # Vẽ tâm cụm
        ax.scatter(centroids[:, 0], centroids[:, 1], color='red', marker='x', s=200, label='Tâm cụm')

        # Thiết lập tiêu đề và nhãn
        ax.set_title("KMeans Clustering Visualization")
        ax.set_xlabel("X1")
        ax.set_ylabel("X2")
        ax.legend()
        ax.grid(True)

        # Thêm biểu đồ vào tab
        self.tab_2.layout().addWidget(canvas)


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