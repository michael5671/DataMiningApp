from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QTabWidget, QWidget)
from PySide6.QtWidgets import (
    QGroupBox, QCheckBox, QScrollArea, QVBoxLayout, QDialog, QMessageBox, QComboBox, QLabel, QTableWidget,QFileDialog,QTableWidgetItem, QHeaderView,QGridLayout,QLineEdit,QFrame
)
import pandas as pd
import itertools
class TapTho(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.data = None
        self.importBtn.clicked.connect(self.import_data)
        self.viewBtn.clicked.connect(self.view_file_data)
        self.importBtn_4.clicked.connect(self.execute_reduction_and_rules)
        self.importBtn_3.clicked.connect(self.import_data)
        self.viewBtn_2.clicked.connect(self.view_file_data)
        # File label
        self.file_name_label = QLabel(self)
        self.file_name_label.setGeometry(770, 90, 250, 20)  # Vị trí dưới nút
        self.file_name_label.setStyleSheet("font-size: 12px; color: black;")
        self.file_name_label.setText("")  # Đặt trống ban đầu
        self.file_name_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.file_name_label.hide()

       # Thêm giao diện cho các checkbox tập thuộc tính
        self.groupBox_attributes = QGroupBox("Chọn tập thuộc tính", self.tab)
        self.groupBox_attributes.setGeometry(20, 90, 500, 200)  # Set vị trí cứng dưới `comboBox_decision`
        self.grid_layout = QGridLayout(self.groupBox_attributes)  # Sử dụng GridLayout cho checkbox
        self.groupBox_attributes.hide()

        # ScrollArea để hiển thị checkbox
        self.scrollArea = QScrollArea(self.tab)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.groupBox_attributes)
        self.scrollArea.setGeometry(20, 90, 500, 200)  # Vị trí dưới `label_decision` và `comboBox_decision`
        self.scrollArea.hide()
        # Nút "Thực thi"
        self.execute_button = QPushButton("Thực thi", self.tab)
        self.execute_button.setGeometry(20, 300, 120, 40)  # Set vị trí tĩnh dưới comboBox_decision
        self.execute_button.setStyleSheet(
            "QPushButton{\n"
            "\tborder: 2px solid;\n"
            "\tborder-radius:7px;\n"
            "\n"
            "\tbackground-color: #a296ca;\n"
            "}"
        )
        self.execute_button.setFont(QFont("roboto", 11, QFont.Bold))

        self.execute_button.clicked.connect(self.execute_calculation)

        self.result_label = QLabel(self.tab)
        self.result_label.setGeometry(20, 400, 600, 200)  # Đặt vị trí bên dưới nút thực thi
        self.result_label.setStyleSheet("font-size: 12px; color: black;")
        self.result_label.setWordWrap(True)
        self.result_label.hide()

        # Label và input field cho tập X
        self.label_X = QLabel("Tập X:", self.tab)
        self.label_X.setGeometry(20, 10, 80, 20)
        self.label_X.setStyleSheet("font-size: 12px;")

        self.X_input = QLineEdit(self.tab)
        self.X_input.setGeometry(100, 10, 200, 25)
        self.X_input.setPlaceholderText("Nhập tập X (ví dụ: 1,4,6)")
        self.X_input.setStyleSheet("font-size: 12px; padding: 2px;")

        # Tạo bảng hiển thị kết quả
        self.result_table = QTableWidget(self.tab)
        self.result_table.setGeometry(20, 400, 900, 250)  # Vị trí và kích thước
        self.result_table.setColumnCount(3)  # Số cột: Thông tin, Giá trị, Kích thước
        self.result_table.setHorizontalHeaderLabels(["Loại", "Nội dung", "Kích thước"])
        self.result_table.horizontalHeader().setStretchLastSection(True)
        self.result_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.result_table.setStyleSheet("font-size: 12px;")

        self.result_table.setColumnCount(3)  # Số lượng cột
        self.result_table.setHorizontalHeaderLabels(["Loại", "Nội dung", "Kích thước"])  # Đặt tiêu đề cột
        self.result_table.horizontalHeader().setVisible(True)
          # Ẩn ban đầu
        # Tạo bảng hiển thị kết quả trên tab Tìm tập thô
        self.matrix_table = QTableWidget(self.tab_2)
        self.matrix_table.setGeometry(20, 200, 1000, 250)  # Vị trí và kích thước
        self.matrix_table.setStyleSheet("font-size: 12px;")
        self.matrix_table.setVisible(True)  # Hiển thị mặc định
        # Label để hiển thị reducts
        # Thêm trong __init__():
        self.reducts_scroll_area = QScrollArea(self.tab_2)
        self.reducts_scroll_area.setGeometry(20, 470, 800, 150)  # Đặt kích thước lớn hơn
        self.reducts_scroll_area.setStyleSheet("font-size: 12px; border: none;")
        self.reducts_scroll_area.setWidgetResizable(True)

        # Tạo label bên trong scroll area
        self.reducts_label = QLabel(self.tab_2)
        self.reducts_label.setStyleSheet("font-size: 12px; color: black; padding: 5px;")
        self.reducts_label.setWordWrap(True)
        self.reducts_scroll_area.setWidget(self.reducts_label)

        # Set style cho bảng result_table (Tab 1)
        self.result_table.setStyleSheet("""
            QTableWidget {
                border: 2px solid black; /* Đường viền màu đen */
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

        # Set style cho bảng matrix_table (Tab 2)
        self.matrix_table.setStyleSheet("""
            QTableWidget {
                border: 2px solid black; /* Đường viền màu đen */
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

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1046, 691)
        Form.setStyleSheet(u"font-family:roboto;")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(1046, 691))
        self.tabWidget.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"roboto"])
        font.setPointSize(12)
        font.setWeight(QFont.DemiBold)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(u"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setFont(font)
        self.importBtn = QPushButton(self.tab)
        self.importBtn.setObjectName(u"importBtn")
        self.importBtn.setGeometry(QRect(780, 20, 121, 41))
        font1 = QFont()
        font1.setFamilies([u"roboto"])
        font1.setPointSize(11)
        font1.setWeight(QFont.DemiBold)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
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
        self.viewBtn.setGeometry(QRect(920, 20, 111, 41))
        self.viewBtn.setFont(font1)
        self.viewBtn.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid;\n"
"	border-radius:7px;\n"
"	background-color: #a296ca;\n"
"}")
        self.viewBtn.setCheckable(True)
        self.comboBox_decision = QComboBox(self.tab)
        self.comboBox_decision.setObjectName(u"comboBox_decision")
        self.comboBox_decision.setGeometry(QRect(250, 50, 121, 22))
        self.label_decision = QLabel(self.tab)
        self.label_decision.setObjectName(u"label_decision")
        self.label_decision.setGeometry(QRect(20, 50, 211, 20))
        font2 = QFont()
        font2.setFamilies([u"roboto"])
        font2.setPointSize(11)
        font2.setWeight(QFont.DemiBold)
        self.label_decision.setFont(font2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.importBtn_3 = QPushButton(self.tab_2)
        self.importBtn_3.setObjectName(u"importBtn_3")
        self.importBtn_3.setGeometry(QRect(780, 20, 121, 41))
        self.importBtn_3.setFont(font1)
        self.importBtn_3.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid;\n"
"	border-radius:7px;\n"
"\n"
"	background-color: #a296ca;\n"
"}")
        self.importBtn_3.setCheckable(True)
        self.viewBtn_2 = QPushButton(self.tab_2)
        self.viewBtn_2.setObjectName(u"viewBtn_2")
        self.viewBtn_2.setGeometry(QRect(920, 20, 111, 41))
        self.viewBtn_2.setFont(font1)
        self.viewBtn_2.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid;\n"
"	border-radius:7px;\n"
"	background-color: #a296ca;\n"
"}")
        self.viewBtn_2.setCheckable(True)
        self.label_decision_2 = QLabel(self.tab_2)
        self.label_decision_2.setObjectName(u"label_decision_2")
        self.label_decision_2.setGeometry(QRect(30, 70, 211, 20))
        self.label_decision_2.setFont(font2)
        self.comboBox_decision_2 = QComboBox(self.tab_2)
        self.comboBox_decision_2.setObjectName(u"comboBox_decision_2")
        self.comboBox_decision_2.setGeometry(QRect(260, 70, 121, 22))
        self.importBtn_4 = QPushButton(self.tab_2)
        self.importBtn_4.setObjectName(u"importBtn_4")
        self.importBtn_4.setGeometry(QRect(30, 120, 121, 41))
        self.importBtn_4.setFont(font1)
        self.importBtn_4.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid;\n"
"	border-radius:7px;\n"
"\n"
"	background-color: #a296ca;\n"
"}")
        self.importBtn_4.setCheckable(True)
        self.frame = QFrame(self.tab_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 180, 1021, 471))
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
        self.label_decision.setText(QCoreApplication.translate("Form", u"Ch\u1ecdn thu\u1ed9c t\u00ednh quy\u1ebft \u0111\u1ecbnh", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"X\u1ea5p x\u1ec9 t\u1eadp h\u1ee3p", None))
        self.importBtn_3.setText(QCoreApplication.translate("Form", u"T\u1ea3i file ", None))
        self.viewBtn_2.setText(QCoreApplication.translate("Form", u"Xem d\u1eef li\u1ec7u", None))
        self.label_decision_2.setText(QCoreApplication.translate("Form", u"Ch\u1ecdn thu\u1ed9c t\u00ednh quy\u1ebft \u0111\u1ecbnh", None))
        self.importBtn_4.setText(QCoreApplication.translate("Form", u"T\u00ecm reducts ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"T\u00ecm t\u1eadp th\u00f4", None))
    # retranslateUi


    def import_data(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx *.xls)")
        if file_path:
            try:
                self.data = pd.read_excel(file_path)  # Lưu dữ liệu vào self.data
                # Hiển thị tên file dưới nút
                file_name = file_path.split("/")[-1]  # Lấy tên file từ đường dẫn
                self.file_name_label.setText(f"Tên file: {file_name}")
                self.file_name_label.show()  # Hiển thị label
                  # Cập nhật thuộc tính từ dữ liệu
                self.update_attributes(self.data)
                self.execute_button.show()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not load data: {e}")

    def view_file_data(self):
        """Hàm hiển thị dữ liệu đã tải."""
        if self.data is None:
            QMessageBox.warning(self, "Warning", "Không có dữ liệu để hiển thị! Vui lòng tải dữ liệu trước.")
            return
        # Tạo hộp thoại hiển thị dữ liệu
        dialog = self.DataDialog(self.data, self)
        dialog.show()
    def update_attributes(self, data):
        if data is not None:
            self.comboBox_decision.clear()
            self.comboBox_decision_2.clear()
            # Xóa các checkbox hiện có trong `grid_layout`
            for i in reversed(range(self.grid_layout.count())):
                widget = self.grid_layout.itemAt(i).widget()
                if widget:
                    widget.deleteLater()

            # Thêm cột vào comboBox
            self.comboBox_decision.addItems(data.columns)
            self.comboBox_decision_2.addItems(data.columns)
            # Thêm checkbox vào grid_layout
            col_count = 2  # Số cột checkbox
            for idx, col in enumerate(data.columns):
                checkbox = QCheckBox(col, self.groupBox_attributes)
                checkbox.setStyleSheet("font-size: 11px;")
                row = idx // col_count
                col_position = idx % col_count
                self.grid_layout.addWidget(checkbox, row, col_position)

            # Hiển thị ScrollArea
            self.scrollArea.show()

    def get_selected_attributes(self):
        decision_attr = self.comboBox_decision.currentText()
        selected_attrs = [
            self.grid_layout.itemAt(i).widget().text()
            for i in range(self.grid_layout.count())
            if isinstance(self.grid_layout.itemAt(i).widget(), QCheckBox)
            and self.grid_layout.itemAt(i).widget().isChecked()
        ]
        return decision_attr, selected_attrs
    def formatEquivalenceClasses(self, equivalence_classes):
        """Định dạng lớp tương đương để hiển thị"""
        formatted = []
        for key, objects in equivalence_classes.items():
            formatted.append(f"{key}: {', '.join(objects)}")
        return "\n".join(formatted)


    def execute_calculation(self):
        """
        Tính toán lớp tương đương, xấp xỉ dưới, xấp xỉ trên, độ chính xác và sự phụ thuộc, sau đó hiển thị trong bảng.
        """
        if self.data is None:
            QMessageBox.warning(self, "Warning", "Không có dữ liệu để tính toán! Vui lòng tải dữ liệu trước.")
            return

        # Lấy tập X từ input
        X_text = self.X_input.text().strip()
        if not X_text:
            QMessageBox.warning(self, "Warning", "Vui lòng nhập tập X!")
            return

        try:
            X = {f"O{int(i.strip())}" for i in X_text.split(",")}  # Chuyển đổi tập X
        except ValueError:
            QMessageBox.warning(self, "Warning", "Tập X không hợp lệ! Vui lòng nhập các số cách nhau bằng dấu phẩy.")
            return

        # Lấy các thuộc tính B từ comboBox và checkbox
        decision_attr = self.comboBox_decision.currentText()
        selected_attrs = [
            self.grid_layout.itemAt(i).widget().text()
            for i in range(self.grid_layout.count())
            if isinstance(self.grid_layout.itemAt(i).widget(), QCheckBox) and self.grid_layout.itemAt(i).widget().isChecked()
        ]

        # Kiểm tra nếu chưa chọn thuộc tính nào
        if not decision_attr or not selected_attrs:
            QMessageBox.warning(self, "Warning", "Vui lòng chọn thuộc tính quyết định và ít nhất một thuộc tính điều kiện!")
            return

        # Tính các lớp tương đương
        equivalence_classes = self.computeEquivalenceClasses(selected_attrs)

        # Tính xấp xỉ dưới và trên
        lower_approx = self.lowerApproximation(X, equivalence_classes)
        upper_approx = self.upperApproximation(X, equivalence_classes)

        # Tính độ chính xác
        accuracy = len(lower_approx) / len(upper_approx) if upper_approx else 0

        # Tính sự phụ thuộc
        decision_groups = self.data.groupby(decision_attr)
        total_lower_cardinality = 0
        total_objects = len(self.data)
        dependency_results = []

        for group_value, group_objects in decision_groups:
            group_set = {f"O{idx+1}" for idx in group_objects.index}
            lower_approx_group = self.lowerApproximation(group_set, equivalence_classes)
            total_lower_cardinality += len(lower_approx_group)
            dependency_results.append(
                (f"Lower(B, X{group_value})", ", ".join(sorted(lower_approx_group)), len(lower_approx_group))
            )

        dependency = total_lower_cardinality / total_objects

        # Hiển thị kết quả trong bảng
        results = [
            ("Lớp tương đương (IND)", [", ".join(eq_class) for eq_class in equivalence_classes], "-"),
            ("Xấp xỉ dưới (Lower)", ", ".join(sorted(lower_approx)), len(lower_approx)),
            ("Xấp xỉ trên (Upper)", ", ".join(sorted(upper_approx)), len(upper_approx)),
            ("Độ chính xác (α)", f"{accuracy:.2f}", "-"),
            ("Sự phụ thuộc (k)", f"{dependency:.2f}", total_objects),
        ]
        results.extend(dependency_results)  # Thêm các giá trị Lower(B, Xn) vào kết quả

        # Hiển thị các kết quả trong bảng
        self.result_table.setRowCount(len(results))  # Đặt số hàng
        for row, (desc, value, size) in enumerate(results):
            self.result_table.setItem(row, 0, QTableWidgetItem(desc))
            self.result_table.setItem(row, 1, QTableWidgetItem(str(value)))
            self.result_table.setItem(row, 2, QTableWidgetItem(str(size)))

        self.result_table.show()  # Hiển thị bảng
  # Hiển thị bảng



    def computeEquivalenceClasses(self, attributes):
        """Tính các lớp tương đương, chỉ trả về danh sách đối tượng"""
        equivalence_classes = []
        for _, group in self.data.groupby(attributes):
            objects = [f"O{idx+1}" for idx in group.index]
            equivalence_classes.append(objects)  # Chỉ lưu danh sách các đối tượng
        return equivalence_classes


    def lowerApproximation(self, X, equivalence_classes):
        """Tính xấp xỉ dưới của tập X"""
        lower = set()
        for eq_class in equivalence_classes:
            if set(eq_class).issubset(X):  # Kiểm tra nếu lớp tương đương là tập con của X
                lower.update(eq_class)
        return lower

    def upperApproximation(self, X, equivalence_classes):
        """Tính xấp xỉ trên của tập X"""
        upper = set()
        for eq_class in equivalence_classes:
            if set(eq_class).intersection(X):  # Kiểm tra nếu lớp tương đương giao với X
                upper.update(eq_class)
        return upper



    def calculate_attribute_dependency(self, data, decision_attr, selected_attrs):
        # Giả định: Trả về mức độ phụ thuộc giả định (số dòng phân loại đúng / tổng số dòng)
        grouped = data.groupby(selected_attrs)[decision_attr].nunique()
        total = len(data)
        dependent_count = grouped[grouped == 1].sum()
        return f"{dependent_count}/{total} ({dependent_count / total:.2%})"
    
    #==========================Chuc nang tab sau:===========================

    def calculate_distinguish_matrix(self, condition_attrs, decision_attr):
        """
        Tính ma trận phân biệt giữa các đối tượng và xây dựng hàm phân biệt.
        """
        matrix = {}
        distinguish_function = []
        
        for i in range(len(self.data)):
            for j in range(i + 1, len(self.data)):
                if self.data[decision_attr][i] != self.data[decision_attr][j]:  # Chỉ so sánh khi quyết định khác nhau
                    diff_attrs = {
                        attr for attr in condition_attrs
                        if self.data[attr][i] != self.data[attr][j]  # Thuộc tính khác nhau
                    }
                    if diff_attrs:
                        matrix[(i, j)] = diff_attrs
                        distinguish_function.append(f"({' ∨ '.join(diff_attrs)})")
                    else:
                        matrix[(i, j)] = {"λ"}  # Thêm "λ" nếu không có thuộc tính nào khác nhau

        # Xây dựng hàm phân biệt tổng quát
        distinguish_function = " ∧ ".join(distinguish_function) if distinguish_function else "λ"
        return matrix, distinguish_function


    def find_reducts(self, distinguish_matrix):
        """
        Tìm reducts dựa trên ma trận phân biệt, chỉ trả về các reduct tối giản.
        """
        all_attrs = set.union(*distinguish_matrix.values())
        reducts = []

        def is_reduct(candidate):
            for pair, attrs in distinguish_matrix.items():
                if not attrs.intersection(candidate):
                    return False
            return True

        # Kiểm tra tất cả các tập con của tập thuộc tính
        for size in range(1, len(all_attrs) + 1):
            for subset in itertools.combinations(all_attrs, size):
                subset_set = set(subset)
                if is_reduct(subset_set):
                    # Kiểm tra nếu tập con hiện tại không phải là tập con của reduct đã có
                    if not any(subset_set.issuperset(existing) for existing in reducts):
                        reducts.append(subset_set)

        # Trả về các reducts duy nhất, được sắp xếp
        return [sorted(reduct) for reduct in reducts]


    def execute_reduction_and_rules(self):
        """
        Thực hiện các bước: tính ma trận phân biệt và tìm reducts.
        """
        if self.data is None:
            QMessageBox.warning(self, "Warning", "Không có dữ liệu để thực thi! Vui lòng tải dữ liệu trước.")
            return

        # Lấy thuộc tính quyết định từ comboBox
        decision_attr = self.comboBox_decision_2.currentText()
        if not decision_attr:
            QMessageBox.warning(self, "Warning", "Vui lòng chọn thuộc tính quyết định!")
            return

        # Lấy các thuộc tính điều kiện từ dataset, loại trừ thuộc tính quyết định
        condition_attrs = [col for col in self.data.columns if col != decision_attr]

        # 1. Tính ma trận phân biệt và hàm phân biệt
        distinguish_matrix, distinguish_function = self.calculate_distinguish_matrix(condition_attrs, decision_attr)

        # 2. Tìm reducts
        reducts = self.find_reducts(distinguish_matrix)

        # Hiển thị kết quả
        self.display_results(distinguish_matrix, distinguish_function, reducts)

    def display_results(self, distinguish_matrix, distinguish_function, reducts):
        # Hiển thị hàm phân biệt
        distinguish_text = f"Hàm phân biệt: {distinguish_function}"
        self.reducts_label.setText(distinguish_text)

        # Hiển thị reducts dưới dạng danh sách
        reducts_text = "Reducts:\n" + "\n".join([f"B{i+1} = {reduct}" for i, reduct in enumerate(reducts)])
        self.reducts_label.setText(f"{distinguish_text}\n\n{reducts_text}")

        # Hiển thị bảng ma trận phân biệt
        objects = [f"O{i+1}" for i in range(len(self.data))]
        self.matrix_table.setColumnCount(len(objects) - 1)
        self.matrix_table.setRowCount(len(objects) - 1)
        self.matrix_table.setHorizontalHeaderLabels(objects[:-1])  # Nhãn cột
        self.matrix_table.setVerticalHeaderLabels(objects[1:])  # Nhãn hàng

        # Điền dữ liệu vào ma trận (tam giác dưới)
        for (i, j), attrs in distinguish_matrix.items():
            if i < j:  # Chỉ hiển thị tam giác dưới
                cell_content = ", ".join(attrs) if attrs else "λ"
                self.matrix_table.setItem(j - 1, i, QTableWidgetItem(cell_content))
                self.matrix_table.item(j - 1, i).setTextAlignment(Qt.AlignCenter)

        self.matrix_table.resizeColumnsToContents()
        self.matrix_table.resizeRowsToContents()
        self.matrix_table.show()




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