from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QPushButton, QFileDialog, QTabWidget, QTableWidget, QTableWidgetItem, QSpacerItem, QSizePolicy
)
from PySide6.QtGui import QPixmap, QFont
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt


class CayQuyetDinh(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cây Quyết Định - Trực Quan Hóa")
        self.setGeometry(100, 100, 1200, 800)
        self.df = None
        self.clf_gini = None
        self.clf_entropy = None
        self.label_encoders = {}
        self.y_encoder = None
        self.setup_ui()

    def setup_ui(self):
        self.setStyleSheet("""
            QPushButton {
                background-color: #5B8C5A;
                color: white;
                padding: 10px;
                border-radius: 5px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #417B44;
            }
            QLabel {
                font-size: 14px;
                color: #333;
            }
            QTableWidget {
                border: 1px solid #ccc;
                font-size: 14px;
                background-color: #F9F9F9;
            }
            QTabWidget::pane {
                background: #F4F4F4;
                border-radius: 5px;
            }
        """)

        self.tabs = QTabWidget(self)
        self.tabs.setTabPosition(QTabWidget.North)

        # Tabs
        self.file_tab = QWidget()
        self.setup_file_tab()
        
        self.tree_tab = QWidget()
        self.setup_tree_tab()

        self.rules_tab = QWidget()
        self.setup_rules_tab()

        self.tabs.addTab(self.file_tab, "Nhập File")
        self.tabs.addTab(self.tree_tab, "Vẽ Cây Quyết Định")
        self.tabs.addTab(self.rules_tab, "Luật If-Then")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.addWidget(self.tabs)
        self.setLayout(layout)

    def setup_file_tab(self):
        layout = QVBoxLayout()

        self.select_file_button = QPushButton("Chọn File (Excel hoặc CSV)")
        self.select_file_button.clicked.connect(self.select_file)
        layout.addWidget(self.select_file_button)

        self.table_widget = QTableWidget()
        layout.addWidget(self.table_widget)

        self.result_label = QLabel("Chưa có dữ liệu được tải.")
        layout.addWidget(self.result_label)

        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.file_tab.setLayout(layout)

    def setup_tree_tab(self):
        layout = QVBoxLayout()

        self.draw_tree_button = QPushButton("Vẽ Cây Quyết Định")
        self.draw_tree_button.clicked.connect(self.analyze_data)
        layout.addWidget(self.draw_tree_button)

        accuracy_layout = QHBoxLayout()
        self.result_label_accuracy_gini = QLabel("Accuracy (Gini): -")
        self.result_label_accuracy_entropy = QLabel("Accuracy (Entropy): -")

        accuracy_layout.addWidget(self.result_label_accuracy_gini)
        accuracy_layout.addWidget(self.result_label_accuracy_entropy)
        layout.addLayout(accuracy_layout)

        self.tree_image_gini_label = QLabel("Hình Cây Gini:")
        self.tree_image_entropy_label = QLabel("Hình Cây Entropy:")

        self.tree_image_gini_label.setFixedHeight(300)
        self.tree_image_entropy_label.setFixedHeight(300)

        layout.addWidget(self.tree_image_gini_label)
        layout.addWidget(self.tree_image_entropy_label)
        
        self.tree_tab.setLayout(layout)

    def setup_rules_tab(self):
        layout = QVBoxLayout()

        self.show_rules_button = QPushButton("Hiển Thị Luật If-Then")
        self.show_rules_button.clicked.connect(self.show_if_then_rules)
        layout.addWidget(self.show_rules_button)

        self.rules_label = QLabel("Chưa có luật được tạo.")
        self.rules_label.setFont(QFont("Arial", 14))
        self.rules_label.setWordWrap(True)
        layout.addWidget(self.rules_label)

        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.rules_tab.setLayout(layout)

    def select_file(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("Excel Files (*.xlsx *.xls);;CSV Files (*.csv)")
        
        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0]
            self.load_data(file_path)

    def load_data(self, file_path):
        try:
            if file_path.endswith('.csv'):
                self.df = pd.read_csv(file_path)
            else:
                self.df = pd.read_excel(file_path)
            
            self.df.columns = self.df.columns.str.strip().str.replace(' ', '_')
            
            self.result_label.setText(f"Dữ liệu đã tải xong.")
            self.update_table_widget()
        except Exception as e:
            self.result_label.setText(f"Lỗi khi đọc dữ liệu: {e}")

    def update_table_widget(self):
        if self.df is not None:
            self.table_widget.setColumnCount(len(self.df.columns))
            self.table_widget.setRowCount(len(self.df))
            self.table_widget.setHorizontalHeaderLabels(self.df.columns)

            for row_idx, row in self.df.iterrows():
                for col_idx, value in enumerate(row):
                    self.table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

    def analyze_data(self):
        if self.df is None:
            self.result_label_accuracy_gini.setText("Chưa có dữ liệu!")
            return

        X = self.df.iloc[:, :-1]
        y = self.df.iloc[:, -1]

        for column in X.columns:
            le = LabelEncoder()
            X[column] = le.fit_transform(X[column])
            self.label_encoders[column] = le

        y_encoder = LabelEncoder()
        y = y_encoder.fit_transform(y)
        self.y_encoder = y_encoder

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        # Gini
        self.clf_gini = DecisionTreeClassifier(criterion='gini', random_state=42)
        self.clf_gini.fit(X_train, y_train)
        accuracy_gini = metrics.accuracy_score(y_test, self.clf_gini.predict(X_test))
        self.result_label_accuracy_gini.setText(f"Accuracy (Gini): {accuracy_gini:.2f}")

        # Entropy
        self.clf_entropy = DecisionTreeClassifier(criterion='entropy', random_state=42)
        self.clf_entropy.fit(X_train, y_train)
        accuracy_entropy = metrics.accuracy_score(y_test, self.clf_entropy.predict(X_test))
        self.result_label_accuracy_entropy.setText(f"Accuracy (Entropy): {accuracy_entropy:.2f}")

        self.export_tree_image(self.clf_gini, X.columns, "Cây Gini", self.tree_image_gini_label)
        self.export_tree_image(self.clf_entropy, X.columns, "Cây Entropy", self.tree_image_entropy_label)

    def export_tree_image(self, clf, feature_names, title, target_label):
        plt.figure(figsize=(10, 5))
        plot_tree(clf, feature_names=feature_names, class_names=self.y_encoder.classes_, filled=True)
        plt.title(title)
        plt.savefig(f"{title}.png")
        plt.close()

        pixmap = QPixmap(f"{title}.png")
        target_label.setPixmap(pixmap)
        target_label.setScaledContents(True)

    def show_if_then_rules(self):
        if self.df is None:
            self.rules_label.setText("Chưa có dữ liệu!")
            return

        if not hasattr(self, 'clf_gini') or not hasattr(self, 'clf_entropy'):
            self.rules_label.setText("Chưa có cây quyết định để tạo luật!")
            return

        gini_rules = self.extract_if_then_rules(self.clf_gini)
        entropy_rules = self.extract_if_then_rules(self.clf_entropy)

        if not gini_rules.strip():
            gini_rules = "Không có luật nào được tạo từ cây Gini."
        if not entropy_rules.strip():
            entropy_rules = "Không có luật nào được tạo từ cây Entropy."

        self.rules_label.setText(f"Luật từ cây Gini:\n{gini_rules}\n\nLuật từ cây Entropy:\n{entropy_rules}")
  
    def extract_if_then_rules(self, clf):
        # Lấy các luật từ cây quyết định
        tree_rules = export_text(clf, feature_names=self.df.columns[:-1].tolist())
        print("Tree Rules:\n", tree_rules)  # In ra cấu trúc của cây quyết định để kiểm tra

        rules = []
        current_rule = []

        for rule in tree_rules.split('\n'):
            if not rule.strip():
                continue

            # Làm sạch điều kiện, loại bỏ |--- và khoảng trắng thừa
            rule = rule.replace('|', '').strip()
            rule = rule.replace('-', '').strip()

            # Tìm các điều kiện như "feature_name <= value"
            if "<=" in rule or ">" in rule:
                condition = rule.strip()  # Làm sạch điều kiện
                current_rule.append(condition)
            
            # Tìm lớp (class) của nhãn trong cây quyết định
            elif "class:" in rule:
                # Lấy giá trị lớp
                class_value = int(rule.split("class: ")[1].strip())
                class_name = self.y_encoder.inverse_transform([class_value])[0]  # Giải mã lớp từ số thành chữ

                # Tạo luật if-then
                rule_if_then = " and ".join(current_rule)  # Kết hợp các điều kiện
                rule_if_then = f"If {rule_if_then} Then Play = {class_name}"  # Đổi lớp thành Play = Yes/No
                rules.append(rule_if_then)

                # Reset điều kiện cho luật tiếp theo
                current_rule = []

        return "\n".join(rules)
