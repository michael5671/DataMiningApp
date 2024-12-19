from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QTabWidget, QWidget)
import pandas as pd
from PySide6.QtWidgets import (QApplication, QPushButton, QWidget, QFileDialog, QMessageBox, QTableWidget, QTableWidgetItem, QVBoxLayout, QHeaderView, QDialog, QLabel,QComboBox,QFrame)
import numpy as np
from graphviz import Digraph
import math
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
class CayQuyetDinh(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.data = None
         # Thêm QLabel để hiển thị tên file (sẽ tạo động)
        self.file_name_label = QLabel(self.tab)
        self.file_name_label.setGeometry(770, 90, 250, 20)  # Vị trí dưới nút
        self.file_name_label.setStyleSheet("font-size: 12px; color: black;")
        self.file_name_label.setText("")  # Đặt trống ban đầu
        self.file_name_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.file_name_label.hide()
        # Kết nối các nút với hàm xử lý
        self.importBtn.clicked.connect(self.import_data)
        self.viewBtn.clicked.connect(self.view_file_data)
        self.importBtn_2.clicked.connect(self.calculate_steps)
        self.importBtn_3.clicked.connect(self.generate_and_display_tree)
        self.comboBox.currentIndexChanged.connect(self.clear_table_content)
        # Tạo bảng hiển thị bước tính toán
        self.result_table = QTableWidget(self.tab)
        self.result_table.setGeometry(20, 200, 1000, 300)
        self.result_table.setStyleSheet("""
    QTableWidget {
        border: 2px solid black; /* Đường viền màu tím đậm */
        border-radius: 5px; /* Bo góc đường viền */
        gridline-color: #8A2BE2; /* Màu đường lưới */
    }
    QHeaderView::section {
        background-color: #A8DADC; /* Màu xanh tím */
        color: black;              /* Màu chữ trắng */
        font-size: 14px;
        font-weight: bold;
        border: 1px solid #4B0082; /* Viền header */
        padding: 5px;
    }
""")
        self.result_table.setColumnCount(3)  # Bước, Mô tả, Kết quả
        self.result_table.setHorizontalHeaderLabels(["Bước", "Mô tả", "Kết quả"])
        self.result_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.result_table.verticalHeader().setVisible(False)
        
        self.export_rules_btn.clicked.connect(self.export_tree_rules)
        # Đảm bảo tab_2 có layout
        if not self.tab_2.layout():
            self.tab_2.setLayout(QVBoxLayout())

        
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1046, 691)
        Form.setMinimumSize(QSize(0, 0))
        Form.setMaximumSize(QSize(16777215, 16777215))
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
        self.comboBox = QComboBox(self.tab)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(210, 40, 81, 22))
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
        font4 = QFont()
        font4.setFamilies([u"roboto"])
        font4.setPointSize(11)
        font4.setWeight(QFont.DemiBold)
        font4.setUnderline(False)
        font4.setStrikeOut(False)
        self.importBtn_2.setFont(font4)
        self.importBtn_2.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid;\n"
"	border-radius:7px;\n"
"\n"
"	background-color: #a296ca;\n"
"}")
        self.importBtn_2.setCheckable(True)
        self.importBtn_3 = QPushButton(self.tab)
        self.importBtn_3.setObjectName(u"importBtn_3")
        self.importBtn_3.setGeometry(QRect(170, 100, 181, 31))
        self.importBtn_3.setFont(font4)
        self.importBtn_3.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid;\n"
"	border-radius:7px;\n"
"\n"
"	background-color: #a296ca;\n"
"}")
        self.importBtn_3.setCheckable(True)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.export_rules_btn = QPushButton(self.tab_2)
        self.export_rules_btn.setObjectName(u"export_rules_btn")
        self.export_rules_btn.setGeometry(QRect(910, 10, 121, 31))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setWeight(QFont.DemiBold)
        font5.setUnderline(False)
        font5.setStrikeOut(False)
        self.export_rules_btn.setFont(font5)
        self.export_rules_btn.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid;\n"
"	border-radius:7px;\n"
"\n"
"	background-color: #a296ca;\n"
"}")
        self.frame = QFrame(self.tab_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 60, 1041, 591))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
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
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Gain", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"Gini", None))

        self.label.setText(QCoreApplication.translate("Form", u"Ph\u01b0\u01a1ng ph\u00e1p tri\u1ec3n khai", None))
        self.importBtn_2.setText(QCoreApplication.translate("Form", u"Th\u1ef1c thi", None))
        self.importBtn_3.setText(QCoreApplication.translate("Form", u"Xem c\u00e2y quy\u1ebft \u0111\u1ecbnh ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"Ch\u1ea1y thu\u1eadt to\u00e1n ", None))
        self.export_rules_btn.setText(QCoreApplication.translate("Form", u"R\u00fat lu\u1eadt t\u1eeb c\u00e2y", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"K\u1ebft qu\u1ea3 ", None))
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

    def calculate_gini(self, column):
        """
        Tính chỉ số Gini cho một cột nhãn mục tiêu.
        """
        values, counts = np.unique(column, return_counts=True)
        total = sum(counts)
        gini = 1 - sum((count / total) ** 2 for count in counts)
        return gini

    def calculate_gini_for_attribute(self, data, attribute, target):
        """
        Tính chỉ số Gini cho một thuộc tính cụ thể.
        """
        total = len(data)
        gini_index = 0
        for value in data[attribute].unique():
            subset = data[data[attribute] == value]
            subset_gini = self.calculate_gini(subset[target])
            gini_index += (len(subset) / total) * subset_gini
        return gini_index
    def information(self, column):
        values, counts = np.unique(column, return_counts=True)
        return -sum((count / sum(counts)) * math.log2(count / sum(counts)) for count in counts)

    def calculate_entropy(self, data, target_attr):
        """Tính Entropy cho cột đích (target attribute)."""
        total = len(data)
        entropy = 0
        for value in data[target_attr].unique():
            p = len(data[data[target_attr] == value]) / total
            entropy -= p * math.log2(p)
        return entropy
    def calculate_information_gain(self, data, attribute, target_attr):
        """Tính Gain cho một thuộc tính."""
        total_entropy = self.calculate_entropy(data, target_attr)  # Sử dụng hàm calculate_entropy
        total = len(data)
        attribute_entropy = 0

        for value in data[attribute].unique():
            subset = data[data[attribute] == value]
            attribute_entropy += (len(subset) / total) * self.calculate_entropy(subset, target_attr)

        gain = total_entropy - attribute_entropy
        return gain
    

    def build_tree(self, data, target, attributes):
        tree = {}
        unique_classes = np.unique(data[target])
        if len(unique_classes) == 1:  # Nếu chỉ có 1 nhãn, trả về nhãn đó
            return unique_classes[0]
        if not attributes:  # Nếu không còn thuộc tính để phân chia
            return data[target].mode()[0]
        
        # Tính Gain cho từng thuộc tính và chọn thuộc tính có Gain cao nhất
        gains = [self.calculate_information_gain(data, attr, target) for attr in attributes]
        best_attr = attributes[np.argmax(gains)]  # Thuộc tính có Gain lớn nhất
        tree[best_attr] = {}

        # Phân chia dữ liệu dựa trên thuộc tính tốt nhất
        for value in np.unique(data[best_attr]):
            sub_data = data[data[best_attr] == value]
            subtree = self.build_tree(sub_data, target, [attr for attr in attributes if attr != best_attr])
            tree[best_attr][value] = subtree
        
        return tree

    def draw_tree(self, tree, ax, x=0, y=0, dx=1, dy=1, parent_pos=None, edge_label=None):
        """
        Vẽ cây quyết định trên matplotlib.
        """
        if isinstance(tree, dict):
            root = list(tree.keys())[0]
            children = tree[root]

            # Vẽ nút gốc
            ax.text(x, y, root, ha='center', va='center', bbox=dict(facecolor='skyblue', edgecolor='black', boxstyle='round,pad=0.5'))

            # Vẽ các nhánh con
            n = len(children)
            for i, (edge, child) in enumerate(children.items()):
                child_x = x - dx * (n - 1) / 2 + i * dx  # Tính x cho nhánh con
                child_y = y - dy  # Tính y cho nhánh con

                ax.plot([x, child_x], [y, child_y], 'k-', lw=2)  # Vẽ đường nối
                ax.text((x + child_x) / 2, (y + child_y) / 2, edge, ha='center', va='center', color='red')  # Nhãn cạnh

                self.draw_tree(child, ax, child_x, child_y, dx / 2, dy, (x, y), edge)
        else:
            # Vẽ nút lá
            ax.text(x, y, tree, ha='center', va='center', bbox=dict(facecolor='lightgreen', edgecolor='black', boxstyle='round,pad=0.5'))

    def generate_and_display_tree(self):
        if self.data is None:
            QMessageBox.warning(self, "Warning", "Vui lòng tải dữ liệu trước!")
            return
        # Kiểm tra và tạo layout cho frame nếu chưa có
        if not self.frame.layout():
            self.frame.setLayout(QVBoxLayout())
        # Xóa nội dung cũ trong frameTree (nếu có)
        for i in reversed(range(self.frame.layout().count())):
            widget = self.frame.layout().itemAt(i).widget()
            if widget:
                widget.setParent(None)

        # Tạo cây quyết định
        target = self.data.columns[-1]  # Cột mục tiêu
        attributes = list(self.data.columns[:-1])  # Các thuộc tính
        tree = self.build_tree(self.data, target, attributes)

        # Tạo biểu đồ mới
        figure = Figure(figsize=(8, 6))
        canvas = FigureCanvas(figure)
        ax = figure.add_subplot(111)

        # Vẽ cây quyết định
        ax.axis('off')  # Tắt trục tọa độ
        ax.set_title("Cây Quyết Định", fontsize=14)
        self.draw_tree(tree, ax)

        # Thêm biểu đồ vào frameTree
        self.frame.layout().addWidget(canvas)
        self.tabWidget.setCurrentIndex(1)

    def calculate_steps(self):
        """
        Tính toán các bước xây dựng cây quyết định dựa trên Gain hoặc Gini.
        Mỗi bước sẽ tính giá trị của từng thuộc tính, chọn thuộc tính tốt nhất và phân chia nhánh.
        """
        if self.data is None:
            QMessageBox.warning(self, "Warning", "Vui lòng tải dữ liệu trước!")
            return
        
        self.clear_table_content()  # Xóa kết quả cũ trong bảng

        target = self.data.columns[-1]  # Cột mục tiêu
        attributes = list(self.data.columns[:-1])  # Các thuộc tính
        steps = []  # Danh sách lưu các bước thực hiện

        method = self.comboBox.currentText()  # Phương pháp: Gain hoặc Gini

        self.recursive_tree_steps(self.data, target, attributes, steps, method, level=1)

        # Hiển thị kết quả các bước trên bảng
        self.show_steps_table(steps)

    def clear_table_content(self):
        """
        Xóa nội dung trong bảng, giữ nguyên tiêu đề cột.
        """
        while self.result_table.rowCount() > 0:
            self.result_table.removeRow(0)

    def recursive_tree_steps(self, data, target, attributes, steps, method, level):
        """
        Hàm đệ quy tính toán các bước trong quá trình xây dựng cây quyết định.
        """
        if len(attributes) == 0 or len(data[target].unique()) == 1:
            return  # Dừng khi không còn thuộc tính hoặc tất cả mẫu thuộc cùng một lớp.

        results = []
        # Bước 1: Tính Gain hoặc Gini cho từng thuộc tính
        if method == "Gain":
            for attr in attributes:
                gain = self.calculate_information_gain(data, attr, target)
                results.append((attr, gain))
                steps.append([f"Bước {len(steps)+1}", f"Tính Gain({attr})", f"Gain = {round(gain, 3)}"])
            best_attr, best_value = max(results, key=lambda x: x[1])  # Chọn Gain lớn nhất
        elif method == "Gini":
            for attr in attributes:
                gini = self.calculate_gini_for_attribute(data, attr, target)
                results.append((attr, gini))
                steps.append([f"Bước {len(steps)+1}", f"Tính Gini({attr})", f"Gini = {round(gini, 3)}"])
            best_attr, best_value = min(results, key=lambda x: x[1])  # Chọn Gini nhỏ nhất

        # Bước 2: Chọn thuộc tính làm gốc và ghi lại bước
        steps.append([f"Bước {len(steps)+1}", f"Chọn thuộc tính '{best_attr}' làm gốc", f"{method} = {round(best_value, 3)}"])

        # Bước 3: Phân chia nhánh dựa trên thuộc tính đã chọn
        for value in data[best_attr].unique():
            subset = data[data[best_attr] == value]
            steps.append([
                f"Bước {len(steps)+1}",
                f"Phân chia nhánh '{best_attr} = {value}'",
                f"Số lượng mẫu: {len(subset)}"
            ])
            
            # Đệ quy cho tập con nếu cần
            if len(subset[target].unique()) > 1 and len(attributes) > 1:
                remaining_attributes = [attr for attr in attributes if attr != best_attr]
                self.recursive_tree_steps(subset, target, remaining_attributes, steps, method, level + 1)

    def show_steps_table(self, steps):
        """
        Hiển thị kết quả tính toán từng bước trên bảng.
        """
        self.clear_table_content()  # Xóa nội dung cũ

        # Tạo lại hàng dựa trên kết quả mới
        for step in steps:
            row = self.result_table.rowCount()
            self.result_table.insertRow(row)
            self.result_table.setItem(row, 0, QTableWidgetItem(step[0]))
            self.result_table.setItem(row, 1, QTableWidgetItem(step[1]))
            self.result_table.setItem(row, 2, QTableWidgetItem(step[2]))
    def calculate_tree_depth(self, data, target, attributes):
        """
        Tính độ sâu của cây quyết định cho một thuộc tính.
        """
        if len(attributes) == 0 or len(data[target].unique()) == 1:
            return 1  # Điều kiện dừng: nhánh lá

        gains = [(attr, self.calculate_information_gain(data, attr, target)) for attr in attributes]
        best_attr = attributes[np.argmax([gain for _, gain in gains])]  # Chọn thuộc tính có Gain lớn nhất

        max_depth = 0
        for value in data[best_attr].unique():
            subset = data[data[best_attr] == value]
            if len(subset) > 0:
                remaining_attrs = [attr for attr in attributes if attr != best_attr]
                depth = self.calculate_tree_depth(subset, target, remaining_attrs)
                max_depth = max(max_depth, depth)

        return 1 + max_depth  # Tính tổng độ sâu từ gốc
    def clear_layout_content(self, layout):
        """
        Xóa tất cả widget trong layout nhưng giữ lại layout.
        """
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
    def extract_rules(self, tree, current_rule="", rules=None):
        """
        Hàm đệ quy để duyệt cây và trích xuất các luật IF-THEN.
        """
        if rules is None:
            rules = []

        if isinstance(tree, dict):
            root = list(tree.keys())[0]  # Nút gốc
            for value, subtree in tree[root].items():
                new_rule = f"{current_rule} ({root}={value})"
                self.extract_rules(subtree, new_rule, rules)
        else:
            # Nút lá: thêm luật vào danh sách
            rules.append(f"{current_rule} THEN {tree}")

        return rules

    def export_tree_rules(self):
        """
        Xuất luật từ cây và hiển thị trong Dialog.
        """
        if self.data is None:
            QMessageBox.warning(self, "Warning", "Vui lòng tải dữ liệu trước!")
            return

        # Tạo cây nếu chưa có
        target = self.data.columns[-1]
        attributes = list(self.data.columns[:-1])
        tree = self.build_tree(self.data, target, attributes)

        # Trích xuất luật
        rules = self.extract_rules(tree)

        # Hiển thị luật trong Dialog
        dialog = QDialog(self)
        dialog.setWindowTitle("Luật Rút Từ Cây Quyết Định")
        dialog.resize(600, 400)

        layout = QVBoxLayout(dialog)
        rules_label = QLabel("\n".join(rules), dialog)
        rules_label.setStyleSheet("""
        QLabel {
            font-size: 13px;
            color: #333333;
            padding: 10px;
            background-color: #F8F8F8;
            border: 1px solid #CCCCCC;
            border-radius: 5px;
        }
    """)
        rules_label.setWordWrap(True)
        layout.addWidget(rules_label)

        close_btn = QPushButton("Đóng", dialog)
        close_btn.setStyleSheet("""
        QPushButton {
            background-color: #6A5ACD; /* Màu xanh tím */
            color: white;
            font-size: 14px;
            border-radius: 8px;
            padding: 8px 16px;
        }
        QPushButton:hover {
            background-color: #836FFF; /* Màu sáng hơn khi hover */
        }
    """)
        close_btn.clicked.connect(dialog.close)
        layout.addWidget(close_btn)
        layout.setAlignment(close_btn, Qt.AlignmentFlag.AlignCenter)

        dialog.exec()

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