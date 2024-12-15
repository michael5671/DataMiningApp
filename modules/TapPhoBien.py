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
    QWidget)

class TapPhoBien(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
         # Create a QTextEdit inside the frame for displaying the preview and error messages
        self.textEdit_XuatKetQua = QTextEdit(self.frame_XuatKetQua)
        self.textEdit_XuatKetQua.setObjectName(u"textEdit_XuatKetQua")
        self.textEdit_XuatKetQua.setGeometry(QRect(10, 10, 550, 340))  # Adjust size
        self.textEdit_XuatKetQua.setReadOnly(True)  # Make it read-only

        # Connect the "Import File" button to the choose_file function
        self.pushButton_ImportFile.clicked.connect(self.choose_file)
        self.pushButton_Solve.clicked.connect(self.solve)

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(544, 581)
        self.listWidget = QListWidget(Form)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(-30, 0, 581, 591))
        self.pushButton_Solve = QPushButton(Form)
        self.pushButton_Solve.setObjectName(u"pushButton_Solve")
        self.pushButton_Solve.setGeometry(QRect(180, 170, 75, 24))
        self.pushButton_Solve.setStyleSheet(u"border: 1px solid;")
        self.frame_XuatKetQua = QFrame(Form)
        self.frame_XuatKetQua.setObjectName(u"frame_XuatKetQua")
        self.frame_XuatKetQua.setGeometry(QRect(20, 220, 571, 361))
        self.frame_XuatKetQua.setStyleSheet(u"QFrame { border: 1px solid;\n"
"}")
        self.frame_XuatKetQua.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_XuatKetQua.setFrameShadow(QFrame.Shadow.Raised)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(70, 30, 187, 20))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_ImportFile = QLabel(self.widget)
        self.label_ImportFile.setObjectName(u"label_ImportFile")

        self.horizontalLayout.addWidget(self.label_ImportFile)

        self.pushButton_ImportFile = QPushButton(self.widget)
        self.pushButton_ImportFile.setObjectName(u"pushButton_ImportFile")
        self.pushButton_ImportFile.setStyleSheet(u"border: 1px solid;")

        self.horizontalLayout.addWidget(self.pushButton_ImportFile)

        self.widget1 = QWidget(Form)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(70, 80, 229, 22))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_MinSupport = QLabel(self.widget1)
        self.label_MinSupport.setObjectName(u"label_MinSupport")

        self.horizontalLayout_2.addWidget(self.label_MinSupport)

        self.doubleSpinBox_MinSupport = QDoubleSpinBox(self.widget1)
        self.doubleSpinBox_MinSupport.setObjectName(u"doubleSpinBox_MinSupport")
        self.doubleSpinBox_MinSupport.setStyleSheet(u"border: 1px solid;")
        self.doubleSpinBox_MinSupport.setSingleStep(0.100000000000000)

        self.horizontalLayout_2.addWidget(self.doubleSpinBox_MinSupport)

        self.widget2 = QWidget(Form)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(70, 130, 246, 22))
        self.horizontalLayout_3 = QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_MinConfidence = QLabel(self.widget2)
        self.label_MinConfidence.setObjectName(u"label_MinConfidence")

        self.horizontalLayout_3.addWidget(self.label_MinConfidence)

        self.doubleSpinBox_MinConfidence = QDoubleSpinBox(self.widget2)
        self.doubleSpinBox_MinConfidence.setObjectName(u"doubleSpinBox_MinConfidence")
        self.doubleSpinBox_MinConfidence.setStyleSheet(u"border: 1px solid;")
        self.doubleSpinBox_MinConfidence.setSingleStep(0.100000000000000)

        self.horizontalLayout_3.addWidget(self.doubleSpinBox_MinConfidence)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_Solve.setText(QCoreApplication.translate("Form", u"X\u1eed l\u00fd", None))
        self.label_ImportFile.setText(QCoreApplication.translate("Form", u"Nh\u1eadp d\u1eef li\u1ec7u c\u1ee7a b\u1ea1n:", None))
        self.pushButton_ImportFile.setText(QCoreApplication.translate("Form", u"Choose File", None))
        self.label_MinSupport.setText(QCoreApplication.translate("Form", u"Nh\u1eadp gi\u00e1 tr\u1ecb Min-Support:", None))
        self.label_MinConfidence.setText(QCoreApplication.translate("Form", u"Nh\u1eadp gi\u00e1 tr\u1ecb Min-Confidence:", None))
    # retranslateUi

    def choose_file(self):
        """Hàm xử lý khi người dùng nhấn nút 'Choose File'."""
        try:
            # Mở hộp thoại để chọn file CSV hoặc Excel
            file_path, _ = QFileDialog.getOpenFileName(self, "Chọn tệp", "", "CSV Files (*.csv);;Excel Files (*.xlsx)")
            
            if file_path:
                # Kiểm tra loại file và đọc dữ liệu
                if file_path.endswith('.csv'):
                    self.data = pd.read_csv(file_path)  # Đọc tệp CSV
                elif file_path.endswith('.xlsx'):
                    self.data = pd.read_excel(file_path)  # Đọc tệp Excel
                else:
                    raise ValueError("Tệp không phải dạng CSV hoặc Excel.")

                # Hiển thị thông báo và dữ liệu mẫu trong textEdit_XuatKetQua
                self.textEdit_XuatKetQua.clear()  # Xóa nội dung cũ
                self.textEdit_XuatKetQua.append(f"Dữ liệu đã được nhập từ: {file_path}")
                self.textEdit_XuatKetQua.append(f"Preview:\n{self.data.head().to_string(index=False)}")
            else:
                self.textEdit_XuatKetQua.setText("Không có tệp nào được chọn.")

        except Exception as e:
            # Hiển thị lỗi trong textEdit_XuatKetQua
            self.textEdit_XuatKetQua.clear()  # Xóa nội dung cũ
            self.textEdit_XuatKetQua.setText(f"Lỗi khi đọc tệp: {str(e)}")

    def solve(self):
        """Hàm xử lý khi người dùng nhấn nút 'Solve'."""
        if not hasattr(self, 'data'):
            self.textEdit_XuatKetQua.setText("Vui lòng chọn tệp trước.")
            return

        try:
            # Kiểm tra file có đủ ít nhất 2 cột
            if self.data.shape[1] < 2:
                self.textEdit_XuatKetQua.setText('File phải chứa ít nhất hai cột dữ liệu.')
                return

            # Lấy tên cột từ request (hoặc mặc định lấy cột đầu tiên và thứ hai)
            column1 = self.data.columns[0]
            column2 = self.data.columns[1]

            # Kiểm tra cột người dùng chọn có tồn tại
            if column1 not in self.data.columns or column2 not in self.data.columns:
                self.textEdit_XuatKetQua.setText(f'Cột {column1} hoặc {column2} không tồn tại trong file.')
                return

            # Xây dựng bảng transaction_data
            transaction_data = self.data.pivot_table(index=column1, columns=column2, aggfunc='size', fill_value=0)
            transaction_data = transaction_data.applymap(lambda x: 1 if x > 0 else 0)

            # Nhận giá trị minsupp và minconf từ các widget
            minsupp = self.doubleSpinBox_MinSupport.value()
            minconf = self.doubleSpinBox_MinConfidence.value()
            num_transactions = len(transaction_data)

            # Hàm tìm các tập phổ biến
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

            # Hàm tìm tập cực đại
            def find_maximal_itemsets(frequent_itemsets):
                maximal_itemsets = []
                for itemset in frequent_itemsets:
                    is_maximal = True
                    for other_itemset in frequent_itemsets:
                        if itemset != other_itemset and itemset.issubset(other_itemset):
                            is_maximal = False
                            break
                    if is_maximal:
                        maximal_itemsets.append(itemset)
                return maximal_itemsets

            # Hàm tạo luật kết hợp
            def generate_association_rules(frequent_itemsets, minconf):
                rules = []
                for itemset, support in frequent_itemsets.items():
                    if len(itemset) > 1:
                        for consequence in itemset:
                            antecedent = itemset - frozenset([consequence])
                            if antecedent:
                                antecedent_support = frequent_itemsets[antecedent]
                                confidence = support / antecedent_support
                                if confidence >= minconf:
                                    rules.append({
                                        'antecedent': list(antecedent),
                                        'consequence': [consequence],
                                        'confidence': confidence
                                    })
                return rules

            # Tính toán các itemsets phổ biến, cực đại và luật kết hợp
            frequent_itemsets = find_frequent_itemsets(transaction_data, minsupp)
            maximal_itemsets = find_maximal_itemsets(frequent_itemsets)
            association_rules = generate_association_rules(frequent_itemsets, minconf)

            # Hiển thị kết quả
            self.textEdit_XuatKetQua.clear()  # Xóa nội dung cũ
            self.textEdit_XuatKetQua.append("Tập phổ biến:")
            for itemset, support in frequent_itemsets.items():
                self.textEdit_XuatKetQua.append(f"{list(itemset)}: Support = {support:.2f}")

            self.textEdit_XuatKetQua.append("\nTập phổ biến tối đại:")
            for itemset in maximal_itemsets:
                self.textEdit_XuatKetQua.append(f"{list(itemset)}")

            self.textEdit_XuatKetQua.append("\nCác luật kết hợp:")
            for rule in association_rules:
                self.textEdit_XuatKetQua.append(f"{rule['antecedent']} --> {rule['consequence']}, Confidence: {rule['confidence']:.2f}")

        except Exception as e:
            self.textEdit_XuatKetQua.setText(f"Lỗi khi tính toán: {str(e)}")

    

