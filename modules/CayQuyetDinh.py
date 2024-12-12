from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog, QTabWidget, QHBoxLayout
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree, export_graphviz
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import pydotplus
from IPython.display import Image
from sklearn.preprocessing import LabelEncoder
import pandas as pd

class CayQuyetDinh(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cây Quyết Định")
        self.setGeometry(100, 100, 800, 600)
        self.df = None  # DataFrame để chứa dữ liệu
        self.setup_ui()

    def setup_ui(self):
        # Tạo QTabWidget để chia giao diện thành các tab
        self.tabs = QTabWidget(self)
        self.tabs.setTabPosition(QTabWidget.North)  # Đặt các tab về phía bên trái
        self.tabs.setStyleSheet("""
                    
                """)
        # Tab 1: Nhập file
        self.file_tab = QWidget()
        self.setup_file_tab()
        
        # Tab 2: Vẽ cây quyết định
        self.tree_tab = QWidget()
        self.setup_tree_tab()

        # Tab 3: Biến đổi cây thành luật if-then
        self.rules_tab = QWidget()
        self.setup_rules_tab()

        # Thêm các tab vào QTabWidget
        self.tabs.addTab(self.file_tab, "Nhập file")
        self.tabs.addTab(self.tree_tab, "Vẽ cây quyết định")
        self.tabs.addTab(self.rules_tab, "Biến đổi cây thành luật if-then")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)  # Loại bỏ margin của widget lớn nhất
        layout.addWidget(self.tabs)
        self.setLayout(layout)

    def setup_file_tab(self):
        # Layout của tab nhập file
        layout = QVBoxLayout()

        # Nút chọn file
        self.select_file_button = QPushButton("   Chọn File (Excel hoặc CSV)  ", self)
        self.select_file_button.setFixedWidth(self.select_file_button.fontMetrics().boundingRect(self.select_file_button.text()).width())  # Đặt chiều rộng nút theo chiều dài của text
        self.select_file_button.clicked.connect(self.select_file)
        layout.addWidget(self.select_file_button)

        # Kết quả hiển thị dữ liệu đã tải
        self.result_label = QLabel("", self)
        layout.addWidget(self.result_label)

        self.file_tab.setLayout(layout)

    def setup_tree_tab(self):
        # Layout của tab vẽ cây quyết định
        layout = QVBoxLayout()

        # Nút vẽ cây quyết định
        self.draw_tree_button = QPushButton("   Vẽ Cây Quyết Định  ", self)
        self.draw_tree_button.setFixedWidth(self.draw_tree_button.fontMetrics().boundingRect(self.draw_tree_button.text()).width())  # Đặt chiều rộng nút theo chiều dài của text
        self.draw_tree_button.clicked.connect(self.analyze_data)
        layout.addWidget(self.draw_tree_button)

        # Kết quả tính Gain và Gini
        self.result_label_tree = QLabel("", self)
        layout.addWidget(self.result_label_tree)

        self.tree_tab.setLayout(layout)

    def setup_rules_tab(self):
        # Layout của tab biến đổi cây thành luật if-then
        layout = QVBoxLayout()

        # Nút hiển thị luật if-then
        self.show_rules_button = QPushButton("   Hiển thị Luật IF-THEN  ", self)
        self.show_rules_button.setFixedWidth(self.show_rules_button.fontMetrics().boundingRect(self.show_rules_button.text()).width())  # Đặt chiều rộng nút theo chiều dài của text
        self.show_rules_button.clicked.connect(self.show_if_then_rules)
        layout.addWidget(self.show_rules_button)

        # Label hiển thị các luật if-then
        self.rules_label = QLabel("", self)
        layout.addWidget(self.rules_label)

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
            self.result_label.setText(f"Dữ liệu đã tải xong:\n{self.df.head()}")
        except Exception as e:
            self.result_label.setText(f"Lỗi khi đọc dữ liệu: {e}")

    def analyze_data(self):
        if self.df is None:
            self.result_label_tree.setText("Chưa có dữ liệu!")
            return

        # Giả sử cột cuối cùng là nhãn (Label)
        X = self.df.iloc[:, :-1]  # Các thuộc tính
        y = self.df.iloc[:, -1]   # Nhãn

        # Mã hóa dữ liệu chuỗi thành số
        label_encoders = {}
        for column in X.columns:
            le = LabelEncoder()
            X[column] = le.fit_transform(X[column])
            label_encoders[column] = le

        # Mã hóa nhãn nếu nhãn là chuỗi
        y_encoder = LabelEncoder()
        y = y_encoder.fit_transform(y)

        # Chia dữ liệu thành tập huấn luyện và tập kiểm tra
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        # Xây dựng cây quyết định với tiêu chí Gini
        clf_gini = DecisionTreeClassifier(criterion='gini', random_state=42)
        clf_gini.fit(X_train, y_train)

        # Dự đoán và đánh giá
        y_pred_gini = clf_gini.predict(X_test)
        print("Accuracy với Gini:", metrics.accuracy_score(y_test, y_pred_gini))

        # Xây dựng cây quyết định với tiêu chí Entropy (Information Gain)
        clf_entropy = DecisionTreeClassifier(criterion='entropy', random_state=42)
        clf_entropy.fit(X_train, y_train)

        # Dự đoán và đánh giá
        y_pred_entropy = clf_entropy.predict(X_test)
        print("Accuracy với Entropy:", metrics.accuracy_score(y_test, y_pred_entropy))

        # Hiển thị cấu trúc cây quyết định
        print("\nCây Quyết Định với Gini:")
        tree_rules_gini = export_text(clf_gini, feature_names=list(X.columns))
        print(tree_rules_gini)

        print("\nCây Quyết Định với Entropy:")
        tree_rules_entropy = export_text(clf_entropy, feature_names=list(X.columns))
        print(tree_rules_entropy)

        # Trực quan hóa cây quyết định bằng matplotlib
        plt.figure(figsize=(20, 10))
        plot_tree(clf_gini, feature_names=X.columns, class_names=y_encoder.classes_, filled=True)
        plt.title("Cây Quyết Định với tiêu chí Gini")
        plt.savefig("decision_tree_gini.png")
        plt.show()

        plt.figure(figsize=(20, 10))
        plot_tree(clf_entropy, feature_names=X.columns, class_names=y_encoder.classes_, filled=True)
        plt.title("Cây Quyết Định với tiêu chí Entropy")
        plt.savefig("decision_tree_entropy.png")
        plt.show()

        # Trực quan hóa cây quyết định bằng Graphviz
        dot_data_gini = export_graphviz(clf_gini, out_file=None, 
                                        feature_names=X.columns, 
                                        class_names=y_encoder.classes_, 
                                        filled=True, rounded=True, 
                                        special_characters=True)  
        graph_gini = pydotplus.graph_from_dot_data(dot_data_gini)  
        graph_gini.write_png("decision_tree_gini_graphviz.png")  # Lưu ảnh với tiêu chí Gini
        Image(graph_gini.create_png())

        dot_data_entropy = export_graphviz(clf_entropy, out_file=None, 
                                        feature_names=X.columns, 
                                        class_names=y_encoder.classes_, 
                                        filled=True, rounded=True, 
                                        special_characters=True)  
        graph_entropy = pydotplus.graph_from_dot_data(dot_data_entropy)  
        graph_entropy.write_png("decision_tree_entropy_graphviz.png")  # Lưu ảnh với tiêu chí Entropy
        Image(graph_entropy.create_png())

    def encode_data(self, X, y):
        # Mã hóa các đặc trưng trong X nếu chúng là chuỗi
        label_encoders = {}
        for column in X.columns:
            if X[column].dtype == 'object':  # Kiểm tra nếu cột có dữ liệu chuỗi
                le = LabelEncoder()
                X[column] = le.fit_transform(X[column])
                label_encoders[column] = le
        
        # Mã hóa nhãn (y) nếu là chuỗi
        if y.dtype == 'object':
            y_encoder = LabelEncoder()
            y = y_encoder.fit_transform(y)
        
        return X, y, label_encoders

    def show_if_then_rules(self):
        if self.df is None:
            self.rules_label.setText("Chưa có dữ liệu!")
            return

        # Lấy dữ liệu và chia thành các đặc trưng và nhãn
        X = self.df.iloc[:, :-1]
        y = self.df.iloc[:, -1]

        # Mã hóa dữ liệu nếu có cột chứa chuỗi
        X, y, label_encoders = self.encode_data(X, y)

        # Xây dựng cây quyết định với tiêu chí Gini
        clf_gini = DecisionTreeClassifier(criterion='gini', random_state=42)
        clf_gini.fit(X, y)

        # Xuất các luật if-then từ cây quyết định
        tree_rules = export_text(clf_gini, feature_names=list(X.columns))
        
        # Hiển thị các luật if-then trong QLabel
        self.rules_label.setText(f"Các luật IF-THEN:\n{tree_rules}")

