import pandas as pd
from itertools import combinations
from PySide6.QtWidgets import QFileDialog, QMessageBox
from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtGui import QFont

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QLabel, QHBoxLayout,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy, QTextEdit,
    QWidget, QDialog, QVBoxLayout, QTableWidget,QTableWidgetItem,QHeaderView)

class TapPhoBien(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
         # Thêm QLabel để hiển thị tên file (sẽ tạo động)
        self.file_name_label = QLabel(self)
        self.file_name_label.setGeometry(770, 90, 250, 20)  # Vị trí dưới nút
        self.file_name_label.setStyleSheet("font-size: 12px; color: black;")
        self.file_name_label.setText("")  # Đặt trống ban đầu
        self.file_name_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.file_name_label.hide()
        # Connect the "Import File" button to the choose_file function
        self.pushButton_ImportFile.clicked.connect(self.choose_file)
        self.pushButton_Solve.clicked.connect(self.solve)
        self.viewBtn.clicked.connect(self.view_file_data)

        self.tableWidget_XuatKetQua = QTableWidget(self.frame_XuatKetQua)
        self.tableWidget_XuatKetQua.setObjectName("tableWidget_XuatKetQua")
        self.tableWidget_XuatKetQua.setStyleSheet("border:none;")
        self.horizontalLayout.addWidget(self.tableWidget_XuatKetQua)    
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1046, 691)
        Form.setStyleSheet(u"font-family:roboto;")
        self.pushButton_Solve = QPushButton(Form)
        self.pushButton_Solve.setObjectName(u"pushButton_Solve")
        self.pushButton_Solve.setGeometry(QRect(414, 163, 101, 31))
        font = QFont()
        font.setFamilies([u"roboto"])
        font.setPointSize(11)
        font.setWeight(QFont.DemiBold)
        self.pushButton_Solve.setFont(font)
        self.pushButton_Solve.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid;\n"
"	border-radius:7px;\n"
"\n"
"	background-color: #a296ca;\n"
"}")
        self.frame_XuatKetQua = QFrame(Form)
        self.frame_XuatKetQua.setObjectName(u"frame_XuatKetQua")
        self.frame_XuatKetQua.setGeometry(QRect(20, 220, 1011, 451))
        font1 = QFont()
        font1.setFamilies([u"roboto"])
        font1.setWeight(QFont.Black)
        self.frame_XuatKetQua.setFont(font1)
        self.frame_XuatKetQua.setStyleSheet(u"QFrame { border: 1px solid;\n"
"}")
        self.frame_XuatKetQua.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_XuatKetQua.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_XuatKetQua)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(70, 80, 253, 22))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_MinSupport = QLabel(self.layoutWidget)
        self.label_MinSupport.setObjectName(u"label_MinSupport")
        self.label_MinSupport.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_MinSupport)

        self.doubleSpinBox_MinSupport = QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_MinSupport.setObjectName(u"doubleSpinBox_MinSupport")
        self.doubleSpinBox_MinSupport.setStyleSheet(u"border: 1px solid;")
        self.doubleSpinBox_MinSupport.setSingleStep(0.100000000000000)

        self.horizontalLayout_2.addWidget(self.doubleSpinBox_MinSupport)

        self.layoutWidget1 = QWidget(Form)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(70, 130, 277, 22))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_MinConfidence = QLabel(self.layoutWidget1)
        self.label_MinConfidence.setObjectName(u"label_MinConfidence")
        self.label_MinConfidence.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_MinConfidence)

        self.doubleSpinBox_MinConfidence = QDoubleSpinBox(self.layoutWidget1)
        self.doubleSpinBox_MinConfidence.setObjectName(u"doubleSpinBox_MinConfidence")
        self.doubleSpinBox_MinConfidence.setStyleSheet(u"border: 1px solid;")
        self.doubleSpinBox_MinConfidence.setSingleStep(0.100000000000000)

        self.horizontalLayout_3.addWidget(self.doubleSpinBox_MinConfidence)

        self.viewBtn = QPushButton(Form)
        self.viewBtn.setObjectName(u"viewBtn")
        self.viewBtn.setGeometry(QRect(920, 20, 111, 41))
        self.viewBtn.setFont(font)
        self.viewBtn.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid;\n"
"	border-radius:7px;\n"
"\n"
"	background-color: #a296ca;\n"
"}")
        self.pushButton_ImportFile = QPushButton(Form)
        self.pushButton_ImportFile.setObjectName(u"pushButton_ImportFile")
        self.pushButton_ImportFile.setGeometry(QRect(780, 20, 121, 41))
        self.pushButton_ImportFile.setFont(font)
        self.pushButton_ImportFile.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid;\n"
"	border-radius:7px;\n"
"\n"
"	background-color: #a296ca;\n"
"}")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_Solve.setText(QCoreApplication.translate("Form", u"X\u1eed l\u00fd", None))
        self.label_MinSupport.setText(QCoreApplication.translate("Form", u"Nh\u1eadp gi\u00e1 tr\u1ecb Min-Support:", None))
        self.label_MinConfidence.setText(QCoreApplication.translate("Form", u"Nh\u1eadp gi\u00e1 tr\u1ecb Min-Confidence:", None))
        self.viewBtn.setText(QCoreApplication.translate("Form", u"Xem File", None))
        self.pushButton_ImportFile.setText(QCoreApplication.translate("Form", u"T\u1ea3i file", None))
    # retranslateUi


    def choose_file(self):
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
    def solve(self):
        """Hàm xử lý khi người dùng nhấn nút 'Solve'."""
        if not hasattr(self, 'data'):
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn tệp trước.")
            return

        try:
            # Kiểm tra dữ liệu
            if self.data.shape[1] < 2:
                QMessageBox.warning(self, "Lỗi", "File phải chứa ít nhất hai cột dữ liệu.")
                return

            column1, column2 = self.data.columns[0], self.data.columns[1]
            transaction_data = self.data.pivot_table(index=column1, columns=column2, aggfunc='size', fill_value=0)
            transaction_data = transaction_data.map(lambda x: 1 if x > 0 else 0)

            minsupp = self.doubleSpinBox_MinSupport.value()
            minconf = self.doubleSpinBox_MinConfidence.value()
            num_transactions = len(transaction_data)

            def find_frequent_itemsets(transaction_data, minsupp):
                frequent_itemsets = {}
                item_support = (transaction_data.sum(axis=0) / num_transactions).to_dict()
                current_itemsets = {frozenset([item]): support for item, support in item_support.items() if support >= minsupp}
                frequent_itemsets.update(current_itemsets)
                k = 2
                while current_itemsets:
                    new_combinations = list(combinations(set().union(*current_itemsets.keys()), k))
                    itemset_counts = {frozenset(itemset): (transaction_data[list(itemset)].all(axis=1).sum()) for itemset in new_combinations}
                    current_itemsets = {itemset: count / num_transactions for itemset, count in itemset_counts.items() if count / num_transactions >= minsupp}
                    frequent_itemsets.update(current_itemsets)
                    k += 1
                return frequent_itemsets

            def find_maximal_itemsets(frequent_itemsets):
                return [itemset for itemset in frequent_itemsets if not any(itemset < other for other in frequent_itemsets)]

            def generate_association_rules(frequent_itemsets, minconf):
                rules = []
                for itemset, support in frequent_itemsets.items():
                    if len(itemset) > 1:
                        for consequence in itemset:
                            antecedent = itemset - frozenset([consequence])
                            if antecedent:
                                confidence = support / frequent_itemsets[antecedent]
                                if confidence >= minconf:
                                    rules.append((list(antecedent), [consequence], confidence))
                return rules

            # Tính toán kết quả
            frequent_itemsets = find_frequent_itemsets(transaction_data, minsupp)
            maximal_itemsets = find_maximal_itemsets(frequent_itemsets)
            association_rules = generate_association_rules(frequent_itemsets, minconf)

            # Hiển thị trong QTableWidget
            self.tableWidget_XuatKetQua.clear()
            self.tableWidget_XuatKetQua.setColumnCount(3)
            self.tableWidget_XuatKetQua.setHorizontalHeaderLabels(["Loại", "Nội dung", "Giá trị"])

            # Điền kết quả vào bảng
            rows = []

            # Tập phổ biến
            rows.append(["Tập phổ biến", "-", "-"])
            for itemset, support in frequent_itemsets.items():
                rows.append(["Tập phổ biến", f"{list(itemset)}", f"Support: {support:.2f}"])

            # Tập cực đại
            rows.append(["Tập cực đại", "-", "-"])
            for itemset in maximal_itemsets:
                rows.append(["Tập cực đại", f"{list(itemset)}", "-"])

            # Luật kết hợp
            rows.append(["Luật kết hợp", "-", "-"])
            for antecedent, consequence, confidence in association_rules:
                rows.append(["Luật kết hợp", f"{antecedent} --> {consequence}", f"Confidence: {confidence:.2f}"])

            # Thêm dữ liệu vào bảng
            self.tableWidget_XuatKetQua.setRowCount(len(rows))
            for row_idx, row_data in enumerate(rows):
                for col_idx, value in enumerate(row_data):
                    self.tableWidget_XuatKetQua.setItem(row_idx, col_idx, QTableWidgetItem(value))

            # Tùy chỉnh giao diện
            self.tableWidget_XuatKetQua.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.tableWidget_XuatKetQua.setStyleSheet("""
                QHeaderView::section {
                    background-color: #A8DADC;
                    font-weight: bold;
                    border: 1px solid #457B9D;
                }
            """)

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi tính toán: {str(e)}")

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
    
