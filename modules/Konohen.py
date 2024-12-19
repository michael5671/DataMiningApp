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
from PySide6.QtWidgets import (QApplication, QPushButton, QWidget, QFileDialog, QMessageBox, QTableWidget, QTableWidgetItem, QVBoxLayout, QHeaderView, QDialog, QLabel,QComboBox,QFrame)
import numpy as np
import pandas as pd
from minisom import MiniSom
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib import cm
class Konohen(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.data = None
        self.weights = None
        
        self.importBtn.clicked.connect(self.import_data)
        self.runBtn.clicked.connect(self.run_algorithm)
        self.viewBtn.clicked.connect(self.view_file_data)
        self.runBtn_2.clicked.connect(self.switch_to_visualize_tab)


         # Thêm QLabel để hiển thị tên file (sẽ tạo động)
        self.file_name_label = QLabel(self.executeTab)
        self.file_name_label.setGeometry(770, 90, 250, 20)  # Vị trí dưới nút
        self.file_name_label.setStyleSheet("font-size: 12px; color: black;")
        self.file_name_label.setText("")  # Đặt trống ban đầu
        self.file_name_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.file_name_label.hide()

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
        font1 = QFont()
        font1.setFamilies([u"roboto"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.tabWidget.setFont(font1)
        self.tabWidget.setStyleSheet(u"")
        self.executeTab = QWidget()
        self.executeTab.setObjectName(u"executeTab")
        font2 = QFont()
        font2.setFamilies([u"roboto"])
        font2.setPointSize(9)
        font2.setBold(False)
        self.executeTab.setFont(font2)
        self.executeTab.setStyleSheet(u"")
        self.runBtn = QPushButton(self.executeTab)
        self.runBtn.setObjectName(u"runBtn")
        self.runBtn.setGeometry(QRect(360, 170, 161, 41))
        self.runBtn.setFont(font1)
        self.runBtn.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid;\n"
"	border-radius:7px;\n"
"\n"
"	background-color: #a296ca;\n"
"}")
        self.line = QFrame(self.executeTab)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(550, 240, 2, 421))
        font3 = QFont()
        font3.setFamilies([u"roboto"])
        font3.setBold(False)
        self.line.setFont(font3)
        self.line.setAutoFillBackground(False)
        self.line.setStyleSheet(u"background-color:black;")
        self.line.setFrameShadow(QFrame.Shadow.Plain)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.label_7 = QLabel(self.executeTab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(740, 200, 61, 31))
        font4 = QFont()
        font4.setFamilies([u"roboto"])
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setItalic(False)
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u";")
        self.frameQuaTrinh = QFrame(self.executeTab)
        self.frameQuaTrinh.setObjectName(u"frameQuaTrinh")
        self.frameQuaTrinh.setGeometry(QRect(19, 240, 501, 411))
        self.frameQuaTrinh.setStyleSheet(u"")
        self.frameQuaTrinh.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameQuaTrinh.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frameQuaTrinh)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.executeTab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(200, 200, 71, 31))
        self.label_8.setFont(font4)
        self.label_8.setStyleSheet(u";")
        self.label_3 = QLabel(self.executeTab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 15, 191, 31))
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u";")
        self.label_4 = QLabel(self.executeTab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(13, 62, 191, 31))
        self.label_4.setFont(font1)
        self.label_6 = QLabel(self.executeTab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(13, 135, 151, 31))
        self.label_6.setFont(font1)
        self.label_5 = QLabel(self.executeTab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(13, 98, 241, 31))
        self.label_5.setFont(font1)
        self.R = QLineEdit(self.executeTab)
        self.R.setObjectName(u"R")
        self.R.setGeometry(QRect(270, 105, 51, 21))
        self.R.setStyleSheet(u"border: 1px solid;")
        self.a = QLineEdit(self.executeTab)
        self.a.setObjectName(u"a")
        self.a.setGeometry(QRect(270, 145, 51, 21))
        self.a.setStyleSheet(u"border: 1px solid;")
        self.epochs = QLineEdit(self.executeTab)
        self.epochs.setObjectName(u"epochs")
        self.epochs.setGeometry(QRect(270, 64, 51, 21))
        self.epochs.setStyleSheet(u"border: 1px solid;")
        self.importBtn = QPushButton(self.executeTab)
        self.importBtn.setObjectName(u"importBtn")
        self.importBtn.setGeometry(QRect(770, 20, 121, 41))
        font5 = QFont()
        font5.setFamilies([u"roboto"])
        font5.setPointSize(11)
        font5.setWeight(QFont.DemiBold)
        self.importBtn.setFont(font5)
        self.importBtn.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid;\n"
"	border-radius:7px;\n"
"\n"
"	background-color: #a296ca;\n"
"}")
        self.importBtn.setCheckable(True)
        self.viewBtn = QPushButton(self.executeTab)
        self.viewBtn.setObjectName(u"viewBtn")
        self.viewBtn.setGeometry(QRect(910, 20, 111, 41))
        self.viewBtn.setFont(font5)
        self.viewBtn.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid;\n"
"	border-radius:7px;\n"
"\n"
"	background-color: #a296ca;\n"
"}")
        self.viewBtn.setCheckable(True)
        self.frameKetQua = QFrame(self.executeTab)
        self.frameKetQua.setObjectName(u"frameKetQua")
        self.frameKetQua.setGeometry(QRect(570, 240, 461, 411))
        self.frameKetQua.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameKetQua.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.executeTab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(450, 75, 111, 16))
        self.label.setFont(font1)
        self.label_9 = QLabel(self.executeTab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(450, 95, 61, 31))
        self.label_9.setFont(font1)
        self.label_10 = QLabel(self.executeTab)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(450, 125, 61, 31))
        self.label_10.setFont(font1)
        self.n_rows = QLineEdit(self.executeTab)
        self.n_rows.setObjectName(u"n_rows")
        self.n_rows.setGeometry(QRect(530, 100, 51, 21))
        self.n_rows.setStyleSheet(u"border: 1px solid;")
        self.n_columns = QLineEdit(self.executeTab)
        self.n_columns.setObjectName(u"n_columns")
        self.n_columns.setGeometry(QRect(530, 130, 51, 21))
        self.n_columns.setStyleSheet(u"border: 1px solid;")
        self.runBtn_2 = QPushButton(self.executeTab)
        self.runBtn_2.setObjectName(u"runBtn_2")
        self.runBtn_2.setGeometry(QRect(540, 170, 141, 41))
        self.runBtn_2.setFont(font1)
        self.runBtn_2.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid;\n"
"	border-radius:7px;\n"
"\n"
"	background-color: #a296ca;\n"
"}")
        self.tabWidget.addTab(self.executeTab, "")
        self.visualizeTab = QWidget()
        self.visualizeTab.setObjectName(u"visualizeTab")
        font6 = QFont()
        font6.setFamilies([u"roboto"])
        font6.setPointSize(9)
        self.visualizeTab.setFont(font6)
        self.tabWidget.addTab(self.visualizeTab, "")

        self.horizontalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
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
        self.label.setText(QCoreApplication.translate("Form", u"K\u00edch th\u01b0\u1edbc l\u01b0\u1edbi", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"S\u1ed1 h\u00e0ng", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"S\u1ed1 c\u1ed9t", None))
        self.runBtn_2.setText(QCoreApplication.translate("Form", u"Tr\u1ef1c Quan", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.executeTab), QCoreApplication.translate("Form", u"Ch\u1ea1y Thu\u1eadt To\u00e1n", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.visualizeTab), QCoreApplication.translate("Form", u"Tr\u1ef1c Quan ", None))
    # retranslateUi


    import pandas as pd
    
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

    def run_algorithm(self):
        if self.data is None:
            QMessageBox.warning(self, "Warning", "Vui lòng tải dữ liệu trước!")
            return

        try:
            epochs = int(self.epochs.text()) if self.epochs.text() else 100
            n_rows = int(self.n_rows.text()) if self.n_rows.text() else 5
            n_columns = int(self.n_columns.text()) if self.n_columns.text() else 5
            alpha = float(self.a.text()) if self.a.text() else 0.5
            radius = int(self.R.text()) if self.R.text() else 2

            if epochs <= 0 or n_rows <= 0 or n_columns <= 0 or alpha <= 0:
                raise ValueError("Các giá trị nhập phải lớn hơn 0!")
        except ValueError as e:
            QMessageBox.warning(self, "Warning", f"Giá trị nhập không hợp lệ! {e}")
            return

        # Chuẩn bị dữ liệu và SOM
        data_matrix = self.data.values
        self.num_features = self.data.shape[1]
        self.som = MiniSom(n_rows, n_columns, self.num_features, sigma=radius, learning_rate=alpha)
        self.som.random_weights_init(data_matrix)
        self.setup_process_table()

        self.add_process_log("Bắt đầu thuật toán Kohonen SOM...")
        
        # Chạy thuật toán
        for epoch in range(epochs):
            for idx, x in enumerate(data_matrix):
                distances = np.linalg.norm(self.som._weights - x, axis=-1)
                winner = np.unravel_index(np.argmin(distances), distances.shape)
                distance_to_winner = distances[winner]
                # Ghi log neuron thắng trước khi cập nhật
                self.add_process_log(f"Epoch {epoch + 1}, Vector {idx + 1}: Neuron thắng tại ({winner[0]}, {winner[1]}), Khoảng cách: {distance_to_winner:.4f}")

                # Ghi log trọng số trước khi cập nhật
                #self.add_process_log(f"Trọng số trước khi cập nhật: {self.som._weights[winner[0], winner[1]]}")

                # Cập nhật trọng số
                self.update_neighborhood(winner, x, alpha, radius)

                # Ghi log trọng số sau khi cập nhật
                # self.add_process_log(f"Trọng số sau khi cập nhật: {self.som._weights[winner[0], winner[1]]}")

            # Giảm tốc độ học và bán kính
            alpha *= 0.9
            radius = max(radius * 0.9, 0)
            self.add_process_log(f"Epoch {epoch + 1} kết thúc: Tốc độ học = {alpha:.4f}, Bán kính = {radius:.2f}")

        self.display_clustering_results(data_matrix)
        self.visualize_data()


    # def visualize_scatter_plot(self, data_matrix):
    #     from sklearn.decomposition import PCA
    #     # Giảm chiều dữ liệu về 2D bằng PCA
    #     pca = PCA(n_components=2)
    #     reduced_data = pca.fit_transform(data_matrix)

    #     # Gán nơ-ron thắng cho từng điểm
    #     winners = [self.som.winner(x) for x in data_matrix]
    #     clusters = [winner[0] * self.som._weights.shape[1] + winner[1] for winner in winners]

    #     # Vẽ biểu đồ scatter
    #     figure, ax = plt.subplots(figsize=(8, 8))
    #     scatter = ax.scatter(reduced_data[:, 0], reduced_data[:, 1], c=clusters, cmap='viridis', edgecolor='k')
    #     legend1 = ax.legend(*scatter.legend_elements(), title="Cụm")
    #     ax.add_artist(legend1)

    #     ax.set_title("Scatter Plot - Biểu diễn dữ liệu và phân cụm SOM")
    #     ax.set_xlabel("PCA Component 1")
    #     ax.set_ylabel("PCA Component 2")

    #     # Hiển thị trong tab Trực quan
    #     if not self.visualizeTab.layout():
    #         self.visualizeTab.setLayout(QVBoxLayout())
    #     else:
    #         for i in reversed(range(self.visualizeTab.layout().count())):
    #             self.visualizeTab.layout().itemAt(i).widget().setParent(None)

    #     canvas = FigureCanvas(figure)
    #     self.visualizeTab.layout().addWidget(canvas)

    def update_neighborhood(self, winner, x, alpha, radius):
        """
        Cập nhật vùng lân cận của neuron chiến thắng và ghi lại giá trị trọng số trước và sau khi cập nhật.
        """
        weights = self.som._weights
        before_update = weights.copy()  # Lưu lại trạng thái trọng số trước khi cập nhật

        # Duyệt qua tất cả các neuron và cập nhật trong bán kính
        for i in range(weights.shape[0]):
            for j in range(weights.shape[1]):
                distance = np.linalg.norm(np.array([i, j]) - np.array(winner))
                if distance <= radius:
                    weights[i, j] += alpha * (x - weights[i, j])
                    # Ghi lại thông tin
                    self.add_process_log(f"Neuron tại ({i}, {j}): Trọng số trước: {before_update[i, j]} --> Trọng số sau: {weights[i, j]}")

    def add_process_log(self, description):
        """
        Thêm thông tin log vào bảng Quá trình.
        """
        row_position = self.process_table.rowCount()
        self.process_table.insertRow(row_position)
        self.process_table.setItem(row_position, 0, QTableWidgetItem(description))


    def display_step(self, description):
        row_position = self.process_table.rowCount()
        self.process_table.insertRow(row_position)
        self.process_table.setItem(row_position, 0, QTableWidgetItem(description))



    def visualize_data(self):
        if self.data is None or self.som is None:
            QMessageBox.warning(self, "Warning", "Vui lòng chạy thuật toán trước!")
            return

        # Tạo U-Matrix từ trọng số
        weights = self.som.get_weights()
        u_matrix = np.zeros((weights.shape[0], weights.shape[1]))

        for i in range(weights.shape[0]):
            for j in range(weights.shape[1]):
                neighbors = []
                if i > 0: neighbors.append(weights[i-1, j])
                if i < weights.shape[0] - 1: neighbors.append(weights[i+1, j])
                if j > 0: neighbors.append(weights[i, j-1])
                if j < weights.shape[1] - 1: neighbors.append(weights[i, j+1])
                u_matrix[i, j] = np.mean([np.linalg.norm(weights[i, j] - neighbor) for neighbor in neighbors])

        # Vẽ Heatmap
        figure, ax = plt.subplots(figsize=(8, 8))
        cax = ax.imshow(u_matrix, cmap=cm.coolwarm, interpolation='none')

        for x in self.data.values:
            winner = self.som.winner(x)
            ax.text(winner[1], winner[0], 'X', color='black', ha='center', va='center', fontsize=12)

        ax.set_title("Heatmap SOM - U-Matrix with Winning Neurons")
        figure.colorbar(cax)

        # Hiển thị trong tab trực quan
        if not self.visualizeTab.layout():
            self.visualizeTab.setLayout(QVBoxLayout())
        else:
            for i in reversed(range(self.visualizeTab.layout().count())):
                self.visualizeTab.layout().itemAt(i).widget().setParent(None)

        canvas = FigureCanvas(figure)
        self.visualizeTab.layout().addWidget(canvas)

    
    def display_clustering_results(self, data_matrix):
        # Kiểm tra và tạo layout nếu chưa có
        if not self.frameKetQua.layout():
            self.frameKetQua.setLayout(QVBoxLayout())
        else:
            for i in reversed(range(self.frameKetQua.layout().count())):
                self.frameKetQua.layout().itemAt(i).widget().setParent(None)

        # Tính toán neuron chiến thắng và gán vào các cụm
        winners = [self.som.winner(x) for x in data_matrix]
        clusters = {i: [] for i in range(self.som._weights.shape[0] * self.som._weights.shape[1])}

        for idx, winner in enumerate(winners):
            cluster_id = winner[0] * self.som._weights.shape[1] + winner[1]
            clusters[cluster_id].append(f"Mẫu {idx + 1}")

        # Tạo bảng kết quả
        table = QTableWidget(len(clusters), 2)
        table.setHorizontalHeaderLabels(["Cụm", "Các Mẫu"])
        row = 0
        for cluster_id, samples in clusters.items():
            if samples:
                table.setItem(row, 0, QTableWidgetItem(f"Cụm {cluster_id}"))
                table.setItem(row, 1, QTableWidgetItem(", ".join(samples)))
                row += 1

        table.horizontalHeader().setStretchLastSection(True)
        table.setStyleSheet("""
        QHeaderView::section {
            background-color: #FFB6C1; /* Màu hồng nhạt */
            color: black; /* Màu chữ */
            font-weight: bold; /* In đậm */
            border: 1px solid #FF69B4; /* Viền */
            padding: 4px;
        }
    """)
        self.frameKetQua.layout().addWidget(table)

    def setup_process_table(self):
        if self.frameQuaTrinh.layout():
            for i in reversed(range(self.frameQuaTrinh.layout().count())):
                self.frameQuaTrinh.layout().itemAt(i).widget().setParent(None)
        else:
            self.frameQuaTrinh.setLayout(QVBoxLayout())

        # Thiết lập bảng chỉ với 1 cột
        self.process_table = QTableWidget()
        self.process_table.setRowCount(0)
        self.process_table.setColumnCount(1)
        self.process_table.setHorizontalHeaderLabels(["Mô tả"])  # Chỉ có cột "Mô tả"
        self.process_table.horizontalHeader().setStretchLastSection(True)
        self.process_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.process_table.setStyleSheet("""
        QHeaderView::section {
            background-color: #A8DADC; /* Màu xanh dương nhạt */
            color: black; /* Màu chữ */
            font-weight: bold; /* In đậm */
            border: 1px solid #5F9EA0; /* Viền */
            padding: 4px;
        }
    """)
        self.frameQuaTrinh.layout().addWidget(self.process_table)


    def view_file_data(self):
        if self.data is None:
            QMessageBox.warning(self, "Warning", "No data to display! Please import data first.")
            return

        # Hiển thị dữ liệu trong hộp thoại
        dialog = DataDialog(self.data, self)
        dialog.exec()
    def switch_to_visualize_tab(self):
        """
        Chuyển sang tab Trực Quan khi nhấn nút Trực Quan.
        """
        self.tabWidget.setCurrentIndex(1)  # Chỉ số 1 tương ứng với tab Trực Quan


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
