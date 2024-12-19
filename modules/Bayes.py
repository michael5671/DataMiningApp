from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QLabel, QTextEdit,QMessageBox,QDialog,QTableWidget,QTableWidgetItem,QHeaderView
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QPushButton, QTabWidget, QComboBox,
    QSizePolicy, QWidget)

class Bayes(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.data = None
        self.attributes = {}
        self.dynamic_widgets_bayes = []
        self.dynamic_widgets_laplace = [] 
         # Thêm QLabel để hiển thị tên file (sẽ tạo động)
        self.file_name_label = QLabel(self)
        self.file_name_label.setGeometry(770, 100, 250, 20)  # Vị trí dưới nút
        self.file_name_label.setStyleSheet("font-size: 12px; color: black;")
        self.file_name_label.setText("")  # Đặt trống ban đầu
        self.file_name_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.file_name_label.hide()
        # Kết nối các nút với hàm xử lý
        # Connect signals
        self.pushButton_chooseFile.clicked.connect(self.choose_file)
        self.pushButton_RunBayes.clicked.connect(self.run_bayes)
        self.pushButton_RunLaplace.clicked.connect(self.run_laplace)
        self.comboBox_Select.currentIndexChanged.connect(self.update_bayes_tab)
        self.comboBox.currentIndexChanged.connect(self.update_laplace_tab)
        self.viewBtn.clicked.connect(self.view_file_data)
        self.viewBtn_2.clicked.connect(self.view_file_data)
        self.pushButton_chooseFile_2.clicked.connect(self.choose_file)
        # Thêm bảng QTableWidget cho kết quả Bayes
        self.tableWidget_XuatKetQuaBayes = QTableWidget(self.tab_2)
        self.tableWidget_XuatKetQuaBayes.setGeometry(QRect(40, 300, 981, 340))
        self.tableWidget_XuatKetQuaBayes.setObjectName("tableWidget_XuatKetQuaBayes")

        # Thiết lập header và giao diện bảng Bayes
        self.tableWidget_XuatKetQuaBayes.setColumnCount(4)
        self.tableWidget_XuatKetQuaBayes.setHorizontalHeaderLabels(["Bước", "Mô tả", "Giá trị", "Kết quả"])
        self.tableWidget_XuatKetQuaBayes.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_XuatKetQuaBayes.setStyleSheet("""
    QTableWidget {
        border: 2px solid black; /* Đường viền màu tím đậm */
        border-radius: 5px; /* Bo góc đường viền */
        gridline-color: black; /* Màu đường lưới */
    }
    QHeaderView::section {
        background-color: #A8DADC; /* Màu nền tiêu đề */
        color: black; /* Màu chữ */
        border: 1px solid #8A2BE2; /* Đường viền tiêu đề */
        font-size: 13px;
        font-weight: bold;
    }
""")
        

        # Tương tự cho bảng Laplace
        self.tableWidget_XuatKetQuaLaplace = QTableWidget(self.tab_3)
        self.tableWidget_XuatKetQuaLaplace.setGeometry(QRect(40, 300, 981, 340))
        self.tableWidget_XuatKetQuaLaplace.setObjectName("tableWidget_XuatKetQuaLaplace")
        self.tableWidget_XuatKetQuaLaplace.setColumnCount(4)
        self.tableWidget_XuatKetQuaLaplace.setHorizontalHeaderLabels(["Bước", "Mô tả", "Giá trị", "Kết quả"])
        self.tableWidget_XuatKetQuaLaplace.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_XuatKetQuaLaplace.setStyleSheet("""
    QTableWidget {
        border: 2px solid black; /* Đường viền màu tím đậm */
        border-radius: 5px; /* Bo góc đường viền */
        gridline-color: black; /* Màu đường lưới */
    }
    QHeaderView::section {
        background-color: #A8DADC; /* Màu nền tiêu đề */
        color: black; /* Màu chữ */
        border: 1px solid #8A2BE2; /* Đường viền tiêu đề */
        font-size: 13px;
        font-weight: bold;
    }
""")

        self.tableWidget_XuatKetQuaBayes.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget_XuatKetQuaBayes.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.tableWidget_XuatKetQuaLaplace.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget_XuatKetQuaLaplace.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        column_widths = [100, 300, 200, 150]  # Độ rộng cho các cột "Bước", "Mô tả", "Giá trị", "Kết quả"
        for col_idx, width in enumerate(column_widths):
            self.tableWidget_XuatKetQuaBayes.setColumnWidth(col_idx, width)
            self.tableWidget_XuatKetQuaLaplace.setColumnWidth(col_idx, width)
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1046, 691)
        Form.setMaximumSize(QSize(16777215, 16777215))
        Form.setStyleSheet(u"font-family:roboto;")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(1046, 691))
        self.tabWidget.setMaximumSize(QSize(1046, 691))
        font = QFont()
        font.setFamilies([u"roboto"])
        font.setPointSize(11)
        font.setBold(True)
        self.tabWidget.setFont(font)
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.frame_XuatKetQuaBayes = QFrame(self.tab_2)
        self.frame_XuatKetQuaBayes.setObjectName(u"frame_XuatKetQuaBayes")
        self.frame_XuatKetQuaBayes.setGeometry(QRect(30, 140, 991, 181))
        self.frame_XuatKetQuaBayes.setStyleSheet(u"")
        self.frame_XuatKetQuaBayes.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_XuatKetQuaBayes.setFrameShadow(QFrame.Shadow.Raised)
        self.layoutWidget = QWidget(self.tab_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 20, 341, 22))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_Select = QLabel(self.layoutWidget)
        self.label_Select.setObjectName(u"label_Select")
        font1 = QFont()
        font1.setFamilies([u"roboto"])
        font1.setPointSize(12)
        font1.setWeight(QFont.DemiBold)
        self.label_Select.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_Select)

        self.comboBox_Select = QComboBox(self.layoutWidget)
        self.comboBox_Select.addItem("")
        self.comboBox_Select.setObjectName(u"comboBox_Select")
        self.comboBox_Select.setStyleSheet(u"border: 1px solid;")

        self.horizontalLayout_2.addWidget(self.comboBox_Select)

        self.pushButton_RunBayes = QPushButton(self.tab_2)
        self.pushButton_RunBayes.setObjectName(u"pushButton_RunBayes")
        self.pushButton_RunBayes.setGeometry(QRect(50, 80, 121, 41))
        self.pushButton_RunBayes.setFont(font)
        self.pushButton_RunBayes.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid;\n"
"	border-radius:7px;\n"
"\n"
"	background-color: #a296ca;\n"
"}")
        self.pushButton_chooseFile = QPushButton(self.tab_2)
        self.pushButton_chooseFile.setObjectName(u"pushButton_chooseFile")
        self.pushButton_chooseFile.setGeometry(QRect(780, 20, 121, 41))
        self.pushButton_chooseFile.setFont(font)
        self.pushButton_chooseFile.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid;\n"
"	border-radius:7px;\n"
"\n"
"	background-color: #a296ca;\n"
"}")
        self.viewBtn = QPushButton(self.tab_2)
        self.viewBtn.setObjectName(u"viewBtn")
        self.viewBtn.setGeometry(QRect(920, 20, 111, 41))
        font2 = QFont()
        font2.setFamilies([u"roboto"])
        font2.setPointSize(11)
        font2.setWeight(QFont.DemiBold)
        self.viewBtn.setFont(font2)
        self.viewBtn.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid;\n"
"	border-radius:7px;\n"
"\n"
"	background-color: #a296ca;\n"
"}")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.frame_XuatKetQuaLaplace = QFrame(self.tab_3)
        self.frame_XuatKetQuaLaplace.setObjectName(u"frame_XuatKetQuaLaplace")
        self.frame_XuatKetQuaLaplace.setGeometry(QRect(40, 140, 981, 501))
        self.frame_XuatKetQuaLaplace.setStyleSheet(u"")
        self.frame_XuatKetQuaLaplace.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_XuatKetQuaLaplace.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton_RunLaplace = QPushButton(self.tab_3)
        self.pushButton_RunLaplace.setObjectName(u"pushButton_RunLaplace")
        self.pushButton_RunLaplace.setGeometry(QRect(50, 80, 121, 41))
        self.pushButton_RunLaplace.setFont(font)
        self.pushButton_RunLaplace.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid;\n"
"	border-radius:7px;\n"
"\n"
"	background-color: #a296ca;\n"
"}")
        self.layoutWidget1 = QWidget(self.tab_3)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(40, 20, 321, 26))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout_4.addWidget(self.label)

        self.comboBox = QComboBox(self.layoutWidget1)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"border: 1px solid;")

        self.horizontalLayout_4.addWidget(self.comboBox)

        self.pushButton_chooseFile_2 = QPushButton(self.tab_3)
        self.pushButton_chooseFile_2.setObjectName(u"pushButton_chooseFile_2")
        self.pushButton_chooseFile_2.setGeometry(QRect(780, 20, 121, 41))
        self.pushButton_chooseFile_2.setFont(font)
        self.pushButton_chooseFile_2.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid;\n"
"	border-radius:7px;\n"
"\n"
"	background-color: #a296ca;\n"
"}")
        self.viewBtn_2 = QPushButton(self.tab_3)
        self.viewBtn_2.setObjectName(u"viewBtn_2")
        self.viewBtn_2.setGeometry(QRect(920, 20, 111, 41))
        self.viewBtn_2.setFont(font2)
        self.viewBtn_2.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid;\n"
"	border-radius:7px;\n"
"\n"
"	background-color: #a296ca;\n"
"}")
        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_Select.setText(QCoreApplication.translate("Form", u"Ch\u1ecdn c\u1ed9t quy\u1ebft \u0111\u1ecbnh:", None))
        self.comboBox_Select.setItemText(0, QCoreApplication.translate("Form", u"<Ch\u1ecdn c\u1ed9t>", None))

        self.pushButton_RunBayes.setText(QCoreApplication.translate("Form", u"Run Bayes", None))
        self.pushButton_chooseFile.setText(QCoreApplication.translate("Form", u"T\u1ea3i file", None))
        self.viewBtn.setText(QCoreApplication.translate("Form", u"Xem File", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Thu\u1eadt to\u00e1n Bayes", None))
        self.pushButton_RunLaplace.setText(QCoreApplication.translate("Form", u"Run Laplace", None))
        self.label.setText(QCoreApplication.translate("Form", u"Ch\u1ecdn c\u1ed9t quy\u1ebft \u0111\u1ecbnh:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"<Ch\u1ecdn c\u1ed9t>", None))

        self.pushButton_chooseFile_2.setText(QCoreApplication.translate("Form", u"T\u1ea3i file", None))
        self.viewBtn_2.setText(QCoreApplication.translate("Form", u"Xem File", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"L\u00e0m tr\u01a1n Laplace", None))
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
                self.attributes = {col: self.data[col].tolist() for col in self.data.columns}

                self.comboBox_Select.clear()
                self.comboBox.clear()
                self.comboBox_Select.addItems(["<Chọn cột quyết định>"] + list(self.data.columns))
                self.comboBox.addItems(["<Chọn cột quyết định>"] + list(self.data.columns))

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
    
    def update_bayes_tab(self):
        """Cập nhật comboBox động cho Tab Bayes."""
        self.clear_dynamic_widgets(self.dynamic_widgets_bayes)

        selected_attribute = self.comboBox_Select.currentText()
        if selected_attribute not in self.attributes:
            return

        remaining_attributes = {key: values for key, values in self.attributes.items() if key != selected_attribute}
        y_offset = 10
        for i, (attr, values) in enumerate(remaining_attributes.items()):
            label = QLabel(f"Chọn giá trị {attr}:", self.frame_XuatKetQuaBayes)
            label.setGeometry(10, y_offset + i * 30, 200, 20)
            label.show()

            combo = QComboBox(self.frame_XuatKetQuaBayes)
            combo.setGeometry(220, y_offset + i * 30, 200, 20)
            combo.addItems(list(set(values)))
            combo.show()

            self.dynamic_widgets_bayes.append(label)
            self.dynamic_widgets_bayes.append(combo)

    def update_laplace_tab(self):
        """Cập nhật comboBox động cho Tab Laplace."""
        self.clear_dynamic_widgets(self.dynamic_widgets_laplace)

        selected_attribute = self.comboBox.currentText()
        if selected_attribute not in self.attributes:
            return

        remaining_attributes = {key: values for key, values in self.attributes.items() if key != selected_attribute}
        y_offset = 10
        for i, (attr, values) in enumerate(remaining_attributes.items()):
            label = QLabel(f"Chọn giá trị {attr}:", self.frame_XuatKetQuaLaplace)
            label.setGeometry(10, y_offset + i * 30, 200, 20)
            label.show()

            combo = QComboBox(self.frame_XuatKetQuaLaplace)
            combo.setGeometry(220, y_offset + i * 30, 200, 20)
            combo.addItems(list(set(values)))
            combo.show()

            self.dynamic_widgets_laplace.append(label)
            self.dynamic_widgets_laplace.append(combo)
    # Căn lề giữa và điều chỉnh kích thước cột trong quá trình thêm dữ liệu
    def update_table(self, table_widget, headers, data):
        table_widget.clear()
        table_widget.setRowCount(len(data))
        table_widget.setColumnCount(len(headers))
        table_widget.setHorizontalHeaderLabels(headers)

        for row_idx, row_data in enumerate(data):
            for col_idx, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)  # Căn giữa
                table_widget.setItem(row_idx, col_idx, item)

    def run_bayes(self):
        """Tính toán Naive Bayes và hiển thị từng bước trong bảng."""
        # Xóa nội dung cũ trong bảng
        self.tableWidget_XuatKetQuaBayes.clear()

        # Thu thập các giá trị từ comboBox động
        selected_values = {}
        for i in range(0, len(self.dynamic_widgets_bayes), 2):
            label = self.dynamic_widgets_bayes[i]
            combo = self.dynamic_widgets_bayes[i + 1]
            attribute = label.text().replace("Chọn giá trị ", "").replace(":", "")
            selected_values[attribute] = combo.currentText()

        # Kiểm tra cột quyết định đã được chọn
        target_column = self.comboBox_Select.currentText()
        if target_column not in self.attributes:
            QMessageBox.warning(self, "Warning", "Vui lòng chọn cột quyết định.")
            return

        target_values = self.attributes[target_column]
        total_samples = len(target_values)

        # Tính xác suất P(C)
        class_counts = {value: target_values.count(value) for value in set(target_values)}
        class_probs = {cls: count / total_samples for cls, count in class_counts.items()}

        # Chuẩn bị bảng
        self.tableWidget_XuatKetQuaBayes.setColumnCount(4)
        self.tableWidget_XuatKetQuaBayes.setHorizontalHeaderLabels(["Bước", "Mô tả", "Giá trị", "Kết quả"])
        row = 0

        # Bước 1: Tính xác suất P(C)
        for cls, prob in class_probs.items():
            self.tableWidget_XuatKetQuaBayes.insertRow(row)
            self.tableWidget_XuatKetQuaBayes.setItem(row, 0, QTableWidgetItem(f"Bước 1"))
            self.tableWidget_XuatKetQuaBayes.setItem(row, 1, QTableWidgetItem(f"P({cls})"))
            self.tableWidget_XuatKetQuaBayes.setItem(row, 2, QTableWidgetItem(f"Tổng số: {class_counts[cls]}"))
            self.tableWidget_XuatKetQuaBayes.setItem(row, 3, QTableWidgetItem(f"{prob:.4f}"))
            row += 1

        # Bước 2: Tính P(X|C)
        conditional_probs = {cls: class_probs[cls] for cls in class_probs}
        for attr, value in selected_values.items():
            for cls in class_probs:
                attr_counts = sum(
                    1
                    for i in range(total_samples)
                    if target_values[i] == cls and self.attributes[attr][i] == value
                )
                conditional_prob = attr_counts / class_counts[cls] if class_counts[cls] > 0 else 0
                conditional_probs[cls] *= conditional_prob

                self.tableWidget_XuatKetQuaBayes.insertRow(row)
                self.tableWidget_XuatKetQuaBayes.setItem(row, 0, QTableWidgetItem(f"Bước 2"))
                self.tableWidget_XuatKetQuaBayes.setItem(row, 1, QTableWidgetItem(f"P({attr}={value}|{cls})"))
                self.tableWidget_XuatKetQuaBayes.setItem(row, 2, QTableWidgetItem(f"Số mẫu: {attr_counts}"))
                self.tableWidget_XuatKetQuaBayes.setItem(row, 3, QTableWidgetItem(f"{conditional_prob:.4f}"))
                row += 1

        # Bước 3: Tính xác suất P(C|X) và dự đoán
        predicted_class = max(conditional_probs, key=conditional_probs.get)
        for cls, prob in conditional_probs.items():
            self.tableWidget_XuatKetQuaBayes.insertRow(row)
            self.tableWidget_XuatKetQuaBayes.setItem(row, 0, QTableWidgetItem(f"Bước 3"))
            self.tableWidget_XuatKetQuaBayes.setItem(row, 1, QTableWidgetItem(f"P({cls}|X)"))
            self.tableWidget_XuatKetQuaBayes.setItem(row, 2, QTableWidgetItem(f""))
            self.tableWidget_XuatKetQuaBayes.setItem(row, 3, QTableWidgetItem(f"{prob:.6f}"))
            row += 1

        # Hiển thị kết quả dự đoán
        self.tableWidget_XuatKetQuaBayes.insertRow(row)
        self.tableWidget_XuatKetQuaBayes.setItem(row, 0, QTableWidgetItem(f"Kết quả"))
        self.tableWidget_XuatKetQuaBayes.setItem(row, 1, QTableWidgetItem(f"Dự đoán"))
        self.tableWidget_XuatKetQuaBayes.setItem(row, 2, QTableWidgetItem(f""))
        self.tableWidget_XuatKetQuaBayes.setItem(row, 3, QTableWidgetItem(f"{predicted_class}"))



    def run_laplace(self):
        """Tính toán Naive Bayes với làm trơn Laplace và hiển thị từng bước trong bảng."""
        self.tableWidget_XuatKetQuaLaplace.clear()

        # Thu thập các giá trị từ comboBox động
        selected_values = {}
        for i in range(0, len(self.dynamic_widgets_laplace), 2):
            label = self.dynamic_widgets_laplace[i]
            combo = self.dynamic_widgets_laplace[i + 1]
            attribute = label.text().replace("Chọn giá trị ", "").replace(":", "")
            selected_values[attribute] = combo.currentText()

        # Kiểm tra cột quyết định đã được chọn
        target_column = self.comboBox.currentText()
        if target_column not in self.attributes:
            QMessageBox.warning(self, "Warning", "Vui lòng chọn cột quyết định.")
            return

        target_values = self.attributes[target_column]
        total_samples = len(target_values)
        num_classes = len(set(target_values))

        # Tính xác suất P(C) với làm trơn Laplace
        class_counts = {value: target_values.count(value) for value in set(target_values)}
        class_probs = {
            cls: (count + 1) / (total_samples + num_classes)
            for cls, count in class_counts.items()
        }

        # Chuẩn bị bảng
        self.tableWidget_XuatKetQuaLaplace.setColumnCount(4)
        self.tableWidget_XuatKetQuaLaplace.setHorizontalHeaderLabels(["Bước", "Mô tả", "Giá trị", "Kết quả"])
        row = 0

        # Bước 1: Tính xác suất P(C) với làm trơn Laplace
        for cls, prob in class_probs.items():
            self.tableWidget_XuatKetQuaLaplace.insertRow(row)
            self.tableWidget_XuatKetQuaLaplace.setItem(row, 0, QTableWidgetItem(f"Bước 1"))
            self.tableWidget_XuatKetQuaLaplace.setItem(row, 1, QTableWidgetItem(f"P({cls}) với Laplace"))
            self.tableWidget_XuatKetQuaLaplace.setItem(row, 2, QTableWidgetItem(f"Số mẫu: {class_counts[cls]}"))
            self.tableWidget_XuatKetQuaLaplace.setItem(row, 3, QTableWidgetItem(f"{prob:.4f}"))
            row += 1

        # Bước 2: Tính P(X|C) với làm trơn Laplace
        conditional_probs = {cls: class_probs[cls] for cls in class_probs}
        for attr, value in selected_values.items():
            unique_values = len(set(self.attributes[attr]))
            for cls in class_probs:
                attr_counts = sum(
                    1
                    for i in range(total_samples)
                    if target_values[i] == cls and self.attributes[attr][i] == value
                )
                conditional_prob = (attr_counts + 1) / (class_counts[cls] + unique_values)
                conditional_probs[cls] *= conditional_prob

                self.tableWidget_XuatKetQuaLaplace.insertRow(row)
                self.tableWidget_XuatKetQuaLaplace.setItem(row, 0, QTableWidgetItem(f"Bước 2"))
                self.tableWidget_XuatKetQuaLaplace.setItem(row, 1, QTableWidgetItem(f"P({attr}={value}|{cls})"))
                self.tableWidget_XuatKetQuaLaplace.setItem(row, 2, QTableWidgetItem(f"Số mẫu: {attr_counts}"))
                self.tableWidget_XuatKetQuaLaplace.setItem(row, 3, QTableWidgetItem(f"{conditional_prob:.4f}"))
                row += 1

        # Bước 3: Tính xác suất P(C|X) và dự đoán
        predicted_class = max(conditional_probs, key=conditional_probs.get)
        for cls, prob in conditional_probs.items():
            self.tableWidget_XuatKetQuaLaplace.insertRow(row)
            self.tableWidget_XuatKetQuaLaplace.setItem(row, 0, QTableWidgetItem(f"Bước 3"))
            self.tableWidget_XuatKetQuaLaplace.setItem(row, 1, QTableWidgetItem(f"P({cls}|X)"))
            self.tableWidget_XuatKetQuaLaplace.setItem(row, 2, QTableWidgetItem(f""))
            self.tableWidget_XuatKetQuaLaplace.setItem(row, 3, QTableWidgetItem(f"{prob:.6f}"))
            row += 1

        # Hiển thị kết quả dự đoán
        self.tableWidget_XuatKetQuaLaplace.insertRow(row)
        self.tableWidget_XuatKetQuaLaplace.setItem(row, 0, QTableWidgetItem(f"Kết quả"))
        self.tableWidget_XuatKetQuaLaplace.setItem(row, 1, QTableWidgetItem(f"Dự đoán"))
        self.tableWidget_XuatKetQuaLaplace.setItem(row, 2, QTableWidgetItem(f""))
        self.tableWidget_XuatKetQuaLaplace.setItem(row, 3, QTableWidgetItem(f"{predicted_class}"))


    def clear_dynamic_widgets(self, widgets):
        """Xóa các comboBox và label động."""
        for widget in widgets:
            if widget is not None:
                widget.setParent(None)  # Loại bỏ widget khỏi layout cha
                widget.deleteLater()
        widgets.clear()


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