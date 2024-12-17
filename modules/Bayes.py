from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QLabel, QTextEdit
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

        # Connect signals
        self.pushButton_chooseFile.clicked.connect(self.choose_file)
        self.pushButton_RunBayes.clicked.connect(self.run_bayes)
        self.pushButton_RunLaplace.clicked.connect(self.run_laplace)
        self.comboBox_Select.currentIndexChanged.connect(self.update_bayes_tab)
        self.comboBox.currentIndexChanged.connect(self.update_laplace_tab)

        # QTextEdit để hiển thị thông báo
        self.textEdit_XuatKetQua = QTextEdit(self.frame_XuatImportFile)
        self.textEdit_XuatKetQua.setObjectName("textEdit_XuatKetQua")
        self.textEdit_XuatKetQua.setGeometry(QRect(10, 10, 440, 160))
        self.textEdit_XuatKetQua.setReadOnly(True)  # Chỉ đọc, không cho phép chỉnh sửa
        self.textEdit_XuatKetQua.setStyleSheet("border: 1px solid; background-color: #f4f4f4;")

        # QTextEdit để hiển thị thông báo
        self.textEdit_XuatKetQuaBayes = QTextEdit(self.frame_XuatKetQuaBayes)
        self.textEdit_XuatKetQuaBayes.setObjectName("textEdit_XuatKetQuaBayes")
        self.textEdit_XuatKetQuaBayes.setGeometry(QRect(10, 130, 440, 160))
        self.textEdit_XuatKetQuaBayes.setReadOnly(True)  # Chỉ đọc, không cho phép chỉnh sửa
        self.textEdit_XuatKetQuaBayes.setStyleSheet("border: 1px solid; background-color: #f4f4f4;")

        # QTextEdit để hiển thị thông báo
        self.textEdit_XuatKetQuaLaplace = QTextEdit(self.frame_XuatKetQuaLaplace)
        self.textEdit_XuatKetQuaLaplace.setObjectName("textEdit_XuatKetQuaLaplace")
        self.textEdit_XuatKetQuaLaplace.setGeometry(QRect(10, 130, 440, 160))
        self.textEdit_XuatKetQuaLaplace.setReadOnly(True)  # Chỉ đọc, không cho phép chỉnh sửa
        self.textEdit_XuatKetQuaLaplace.setStyleSheet("border: 1px solid; background-color: #f4f4f4;")

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(500, 516)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.frame_XuatImportFile = QFrame(self.tab_1)
        self.frame_XuatImportFile.setObjectName(u"frame_XuatImportFile")
        self.frame_XuatImportFile.setGeometry(QRect(-1, 150, 501, 361))
        self.frame_XuatImportFile.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_XuatImportFile.setFrameShadow(QFrame.Shadow.Raised)
        self.layoutWidget = QWidget(self.tab_1)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(70, 50, 211, 20))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_inputImportFile = QLabel(self.layoutWidget)
        self.label_inputImportFile.setObjectName(u"label_inputImportFile")

        self.horizontalLayout_3.addWidget(self.label_inputImportFile)

        self.pushButton_chooseFile = QPushButton(self.layoutWidget)
        self.pushButton_chooseFile.setObjectName(u"pushButton_chooseFile")
        self.pushButton_chooseFile.setStyleSheet(u"border: 1px solid;")

        self.horizontalLayout_3.addWidget(self.pushButton_chooseFile)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.frame_XuatKetQuaBayes = QFrame(self.tab_2)
        self.frame_XuatKetQuaBayes.setObjectName(u"frame_XuatKetQuaBayes")
        self.frame_XuatKetQuaBayes.setGeometry(QRect(0, 190, 501, 311))
        self.frame_XuatKetQuaBayes.setStyleSheet(u"border: 1px solid;")
        self.frame_XuatKetQuaBayes.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_XuatKetQuaBayes.setFrameShadow(QFrame.Shadow.Raised)
        self.layoutWidget1 = QWidget(self.tab_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(50, 20, 231, 22))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_Select = QLabel(self.layoutWidget1)
        self.label_Select.setObjectName(u"label_Select")

        self.horizontalLayout_2.addWidget(self.label_Select)

        self.comboBox_Select = QComboBox(self.layoutWidget1)
        self.comboBox_Select.addItem("")
        self.comboBox_Select.setObjectName(u"comboBox_Select")
        self.comboBox_Select.setStyleSheet(u"border: 1px solid;")

        self.horizontalLayout_2.addWidget(self.comboBox_Select)

        self.pushButton_RunBayes = QPushButton(self.tab_2)
        self.pushButton_RunBayes.setObjectName(u"pushButton_RunBayes")
        self.pushButton_RunBayes.setGeometry(QRect(360, 80, 75, 24))
        self.pushButton_RunBayes.setStyleSheet(u"border: 1px solid;")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.frame_XuatKetQuaLaplace = QFrame(self.tab_3)
        self.frame_XuatKetQuaLaplace.setObjectName(u"frame_XuatKetQuaLaplace")
        self.frame_XuatKetQuaLaplace.setGeometry(QRect(0, 190, 501, 311))
        self.frame_XuatKetQuaLaplace.setStyleSheet(u"border: 1px solid;")
        self.frame_XuatKetQuaLaplace.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_XuatKetQuaLaplace.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton_RunLaplace = QPushButton(self.tab_3)
        self.pushButton_RunLaplace.setObjectName(u"pushButton_RunLaplace")
        self.pushButton_RunLaplace.setGeometry(QRect(360, 80, 75, 24))
        self.pushButton_RunLaplace.setStyleSheet(u"border: 1px solid;")
        self.layoutWidget2 = QWidget(self.tab_3)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(50, 20, 218, 26))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.comboBox = QComboBox(self.layoutWidget2)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"border: 1px solid;")

        self.horizontalLayout_4.addWidget(self.comboBox)

        self.tabWidget.addTab(self.tab_3, "")

        self.horizontalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_inputImportFile.setText(QCoreApplication.translate("Form", u"Nh\u1eadp d\u1eef li\u1ec7u c\u1ee7a b\u1ea1n:", None))
        self.pushButton_chooseFile.setText(QCoreApplication.translate("Form", u"Choose File", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("Form", u"Import File", None))
        self.label_Select.setText(QCoreApplication.translate("Form", u"Ch\u1ecdn c\u1ed9t quy\u1ebft \u0111\u1ecbnh:", None))
        self.comboBox_Select.setItemText(0, QCoreApplication.translate("Form", u"<Ch\u1ecdn c\u1ed9t>", None))

        self.pushButton_RunBayes.setText(QCoreApplication.translate("Form", u"Run Bayes", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Thu\u1eadt to\u00e1n Bayes", None))
        self.pushButton_RunLaplace.setText(QCoreApplication.translate("Form", u"Run Laplace", None))
        self.label.setText(QCoreApplication.translate("Form", u"Ch\u1ecdn c\u1ed9t quy\u1ebft \u0111\u1ecbnh:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"<Ch\u1ecdn c\u1ed9t>", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"L\u00e0m tr\u01a1n Laplace", None))
    # retranslateUi


    def choose_file(self):
        """Hàm xử lý khi người dùng nhấn nút 'Choose File' để chọn file CSV hoặc Excel."""
        try:
            # Mở hộp thoại để chọn file CSV hoặc Excel
            file_path, _ = QFileDialog.getOpenFileName(self, "Chọn tệp", "", "Excel Files (*.xlsx);;CSV Files (*.csv)")

            if file_path:
                # Kiểm tra loại file và đọc dữ liệu
                if file_path.endswith('.xlsx'):
                    self.data = pd.read_excel(file_path)  # Đọc tệp Excel  
                elif file_path.endswith('.csv'):
                    self.data = pd.read_csv(file_path)  # Đọc tệp CSV
                else:
                    raise ValueError("Tệp không phải dạng CSV hoặc Excel.")
                
                self.attributes = {col: self.data[col].tolist() for col in self.data.columns}

                self.comboBox_Select.clear()
                self.comboBox.clear()
                self.comboBox_Select.addItems(["<Chọn cột quyết định>"] + list(self.data.columns))
                self.comboBox.addItems(["<Chọn cột quyết định>"] + list(self.data.columns))

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

    def run_bayes(self):
        """Tính toán Naive Bayes."""
        self.textEdit_XuatKetQua.clear()

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
            self.textEdit_XuatKetQua.setText("Vui lòng chọn cột quyết định.")
            return

        target_values = self.attributes[target_column]
        total_samples = len(target_values)

        # Tính xác suất P(C)
        class_counts = {value: target_values.count(value) for value in set(target_values)}
        class_probs = {cls: count / total_samples for cls, count in class_counts.items()}

        result_text = "Xác suất P(C):\n"
        for cls, prob in class_probs.items():
            result_text += f"P({cls}): {prob:.4f}\n"

        # Tính P(X|C)
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

                result_text += f"P({attr}={value}|{cls}): {conditional_prob:.4f}\n"

        # Xác định lớp dự đoán
        predicted_class = max(conditional_probs, key=conditional_probs.get)
        result_text += "\nKết quả dự đoán:\n"
        for cls, prob in conditional_probs.items():
            result_text += f"P({cls}|X): {prob:.6f}\n"
        result_text += f"Dự đoán: {target_column} = {predicted_class}"

        # Hiển thị kết quả
        self.textEdit_XuatKetQuaBayes.setText(result_text)

    def run_laplace(self):
        """Tính toán Naive Bayes với làm trơn Laplace."""
        self.textEdit_XuatKetQua.clear()

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
            self.textEdit_XuatKetQua.setText("Vui lòng chọn cột quyết định.")
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

        result_text = "Xác suất P(C) với làm trơn Laplace:\n"
        for cls, prob in class_probs.items():
            result_text += f"P({cls}): {prob:.4f}\n"

        # Tính P(X|C) với làm trơn Laplace
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

                result_text += f"P({attr}={value}|{cls}) with Laplace: {conditional_prob:.4f}\n"

        # Xác định lớp dự đoán
        predicted_class = max(conditional_probs, key=conditional_probs.get)
        result_text += "\nKết quả dự đoán:\n"
        for cls, prob in conditional_probs.items():
            result_text += f"P({cls}|X): {prob:.6f}\n"
        result_text += f"Dự đoán: {target_column} = {predicted_class}"

        # Hiển thị kết quả
        self.textEdit_XuatKetQuaLaplace.setText(result_text)

    def clear_dynamic_widgets(self, widgets):
        """Xóa các comboBox và label động."""
        for widget in widgets:
            widget.deleteLater()
        widgets.clear()