from PySide6.QtWidgets import QWidget, QVBoxLayout, QTabWidget, QPushButton, QFileDialog, QTextEdit, QLineEdit, QLabel, QComboBox, QListWidget
import pandas as pd
from collections import defaultdict
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from itertools import combinations

class TapTho(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Widget Tập Thô")
        self.setGeometry(100, 100, 800, 600)
        self.layout = QVBoxLayout(self)
        self.initUI()

    def initUI(self):
        """Khởi tạo giao diện người dùng"""
        self.tabs = QTabWidget(self)
        self.layout.addWidget(self.tabs)

        # Tab 1: Nhập file
        self.tab1 = QWidget()
        self.tabs.addTab(self.tab1, "Nhập file Excel hoặc CSV")
        self.layout1 = QVBoxLayout(self.tab1)
        self.loadButton = QPushButton("Chọn file Excel hoặc CSV", self)
        self.layout1.addWidget(self.loadButton)
        self.loadButton.clicked.connect(self.loadFile)

        self.resultText1 = QTextEdit(self)
        self.resultText1.setReadOnly(True)
        self.layout1.addWidget(self.resultText1)

# Tab 2: Tính xấp xỉ
        self.tab2 = QWidget()
        self.tabs.addTab(self.tab2, "Tính xấp xỉ")
        self.layout2 = QVBoxLayout(self.tab2)
        self.X_input = QLineEdit(self)
        self.X_input.setPlaceholderText("Nhập tập X")
        self.layout2.addWidget(self.X_input)
        self.B_input = QLineEdit(self)
        self.B_input.setPlaceholderText("Nhập tập B")
        self.layout2.addWidget(self.B_input)
        
        self.approxButton = QPushButton("Tính xấp xỉ", self)
        self.layout2.addWidget(self.approxButton)
        self.approxButton.clicked.connect(self.calculateApproximation)
        
        self.resultText2 = QTextEdit(self)
        self.resultText2.setReadOnly(True)
        self.layout2.addWidget(self.resultText2)
        
        # Tab 3: Khảo sát sự phụ thuộc
        self.tab3 = QWidget()
        self.tabs.addTab(self.tab3, "Khảo sát sự phụ thuộc")
        self.layout3 = QVBoxLayout(self.tab3)
        self.C_input = QLineEdit(self)
        self.C_input.setPlaceholderText("Nhập tập C (ví dụ: Ketqua)")
        self.layout3.addWidget(self.C_input)
        self.B2_input = QLineEdit(self)
        self.B2_input.setPlaceholderText("Nhập tập B (ví dụ: trời,gió)")
        self.layout3.addWidget(self.B2_input)
        
        self.dependencyButton = QPushButton("Khảo sát sự phụ thuộc", self)
        self.layout3.addWidget(self.dependencyButton)
        self.dependencyButton.clicked.connect(self.analyzeDependency)
        
        self.resultText3 = QTextEdit(self)
        self.resultText3.setReadOnly(True)
        self.layout3.addWidget(self.resultText3)
        
        # Tab 4: Tìm Reduct
        self.tab4 = QWidget()
        self.tabs.addTab(self.tab4, "Tìm Reduct")
        self.layout4 = QVBoxLayout(self.tab4)

        # Dropdown cho thuộc tính quyết định
        self.decision_input = QComboBox(self)
        self.decision_input.setPlaceholderText("Chọn thuộc tính quyết định")
        self.layout4.addWidget(self.decision_input)

        # Listbox cho thuộc tính điều kiện (cho phép chọn nhiều thuộc tính)
        self.condition_input = QListWidget(self)
        self.condition_input.setSelectionMode(QListWidget.MultiSelection)
        self.layout4.addWidget(self.condition_input)

        self.reductButton = QPushButton("Tìm Reduct", self)
        self.layout4.addWidget(self.reductButton)
        self.reductButton.clicked.connect(self.findReduct)

        self.resultText4 = QTextEdit(self)
        self.resultText4.setReadOnly(True)
        self.layout4.addWidget(self.resultText4)

    def loadFile(self):
        """Chọn file Excel hoặc CSV và xử lý dữ liệu"""
        options = QFileDialog.Options()
        file, _ = QFileDialog.getOpenFileName(self, "Chọn file", "", "Excel Files (*.xls *.xlsx);;CSV Files (*.csv)", options=options)

        if file:
            if file.endswith('.csv'):
                self.df = pd.read_csv(file)  # Đọc file CSV vào DataFrame
            else:
                self.df = pd.read_excel(file)  # Đọc file Excel vào DataFrame
            self.resultText1.setHtml(f"<b>Đã tải file:</b> {file}<br><br>")
            self.resultText1.append(f"<b>Dữ liệu đầu tiên:</b><br>{self.df.head().to_html(index=False)}<br>")

            # Cập nhật dropdown thuộc tính quyết định và điều kiện
            self.decision_input.clear()
            self.decision_input.addItems(self.df.columns.tolist())
            self.condition_input.clear()
            self.condition_input.addItems(self.df.columns.tolist())

    def loadFile(self):
        """Chọn file Excel hoặc CSV và xử lý dữ liệu"""
        options = QFileDialog.Options()
        file, _ = QFileDialog.getOpenFileName(self, "Chọn file", "", "Excel Files (*.xls *.xlsx);;CSV Files (*.csv)", options=options)

        if file:
            if file.endswith('.csv'):
                self.df = pd.read_csv(file)  # Đọc file CSV vào DataFrame
            else:
                self.df = pd.read_excel(file)  # Đọc file Excel vào DataFrame
            self.resultText1.setHtml(f"<b>Đã tải file:</b> {file}<br><br>")
            self.resultText1.append(f"<b>Dữ liệu đầu tiên:</b><br>{self.df.head().to_html(index=False)}<br>")

            # Cập nhật dropdown thuộc tính quyết định và điều kiện
            self.decision_input.clear()
            self.decision_input.addItems(self.df.columns.tolist())
            self.condition_input.clear()
            self.condition_input.addItems(self.df.columns.tolist())

    def calculateApproximation(self):
        """Tính toán xấp xỉ dưới và trên"""
        try:
            X = set(self.X_input.text().split(","))
            # Chuyển sang định dạng giống như trong các lớp tương đương (o1, o2, o3, ...)
            X = {f"o{i}" for i in X}

            B = self.B_input.text().split(",")
            
            # Kiểm tra các cột tồn tại
            missing_columns = [col for col in B if col not in self.df.columns]
            if missing_columns:
                self.resultText2.setText(f"Các thuộc tính không tồn tại trong dữ liệu: {', '.join(missing_columns)}")
                return

            # In ra giá trị của X để kiểm tra
            print(f"Tập X nhập vào (sau khi chuyển đổi): {X}")

            equivalence_classes = self.computeEquivalenceClasses(B)

            lower_approx = self.lowerApproximation(X, equivalence_classes)
            upper_approx = self.upperApproximation(X, equivalence_classes)

            # Hiển thị kết quả
            self.resultText2.clear()
            self.resultText2.append(f"<b>Các lớp tương đương (IND):</b><br>{self.formatEquivalenceClasses(equivalence_classes)}")
            self.resultText2.append(f"<b>Xấp xỉ dưới (Lower):</b> {', '.join(lower_approx)}")
            self.resultText2.append(f"<b>Xấp xỉ trên (Upper):</b> {', '.join(upper_approx)}")

            accuracy = len(lower_approx) / len(upper_approx)
            self.resultText2.append(f"<b>Độ chính xác:</b> {accuracy:.2f}")
            
            # Đưa ra kết luận
            if accuracy == 1:
                self.resultText2.append("<b>Kết luận:</b> Tập X rõ với B.")
            elif accuracy < 1:
                self.resultText2.append("<b>Kết luận:</b> Tập X là thô so với B.")
            else:
                self.resultText2.append("<b>Kết luận:</b> Độ chính xác không xác định.")
        except Exception as e:
            self.resultText2.setText(f"Lỗi khi tính xấp xỉ: {str(e)}")

    def computeEquivalenceClasses(self, B):
        """Tạo lớp tương đương từ các giá trị trong tập B"""
        equivalence_classes = defaultdict(set)
        for i, row in self.df.iterrows():
            key = tuple(row[col] for col in B)  # Lấy giá trị của các thuộc tính trong B
            equivalence_classes[key].add(f"o{i+1}")  # Gắn nhãn "o1", "o2", ... vào lớp tương đương
        return equivalence_classes

    def lowerApproximation(self, X, equivalence_classes):
        """Tính xấp xỉ dưới (Lower)"""
        lower_approx = set()
        for eq_class in equivalence_classes.values():
            # Thêm các lớp tương đương hoàn toàn nằm trong tập X
            if eq_class.issubset(X):
                lower_approx.update(eq_class)
        return lower_approx

    def upperApproximation(self, X, equivalence_classes):
        """Tính xấp xỉ trên (Upper)"""
        upper_approx = set()
        for eq_class in equivalence_classes.values():
            # Thêm các lớp tương đương có giao với tập X
            if eq_class.intersection(X):
                upper_approx.update(eq_class)
        return upper_approx

    def formatEquivalenceClasses(self, equivalence_classes):
        """Định dạng các lớp tương đương để hiển thị"""
        formatted = "<ul>"
        for key, eq_class in equivalence_classes.items():
            formatted += f"<li><b>{key}:</b> {', '.join(eq_class)}</li>"
        formatted += "</ul>"
        return formatted

    def analyzeDependency(self):
        """Khảo sát sự phụ thuộc của C vào B"""
        C = self.C_input.text().split(",")  # Nhập tập C
        B = self.B2_input.text().split(",")  # Nhập tập B

        # Kiểm tra nếu các input trống
        if not C or not B:
            self.resultText3.setText("<b>Lỗi:</b> Các tập C và B không thể trống!")
            return

        # Kiểm tra xem tất cả các cột trong C và B có tồn tại trong DataFrame không
        missing_columns = [col for col in C + B if col not in self.df.columns]
        if missing_columns:
            self.resultText3.setText(f"<b>Lỗi:</b> Các cột không tồn tại trong dữ liệu: {', '.join(missing_columns)}")
            return

        # Tạo các lớp tương đương từ B
        equivalence_classes = self.computeEquivalenceClasses(B)

        # Tạo các tập C1, C2, ..., Cn từ các đối tượng có giá trị giống nhau trong cột C
        C_sets = self.createC1C2Sets(C, equivalence_classes)

        # Hiển thị các tập C
        C_sets_text = "\n".join([f"C{i+1}: {set}" for i, set in enumerate(C_sets)])  # Chuyển C_sets thành chuỗi
        self.resultText3.setText(f"<b>Các tập C:</b>\n{C_sets_text}")

        # Tính xấp xỉ dưới (lower approximation) cho các tập C
        C_lower_approximations = []
        for i, c_set in enumerate(C_sets):
            lower_approx = self.lowerApproximation(set(c_set), equivalence_classes)
            C_lower_approximations.append(f"C{i+1} (Lower Approximation): {', '.join(lower_approx)}")

        # Hiển thị xấp xỉ dưới của các tập C
        self.resultText3.append(f"\n<b>Xấp xỉ dưới của các tập C:</b>\n" + "\n".join(C_lower_approximations))
        
        # Tính độ phụ thuộc (dependency)
        dependency = self.calculateDependency(C_sets, equivalence_classes)
        self.resultText3.append(f"\n<b>Hệ số phụ thuộc giữa C và B:</b> {dependency:.2f}")

        # Nhận xét về độ phụ thuộc
        if dependency == 1:
            self.resultText3.append(f"<b>Nhận xét:</b> C phụ thuộc hoàn toàn vào B.")
        elif dependency < 1:
            self.resultText3.append(f"<b>Nhận xét:</b> C phụ thuộc một phần vào B.")
        else:
            self.resultText3.append(f"<b>Nhận xét:</b> Độ phụ thuộc không xác định.")

    def createC1C2Sets(self, C, equivalence_classes):
        """Tạo các tập C1, C2, ..., Cn dựa trên các giá trị trong cột C nhập vào"""
        C_sets = defaultdict(set)  # Khởi tạo từ điển với các giá trị trong C làm keys

        # Duyệt qua các lớp tương đương
        for eq_class in equivalence_classes.values():
            for obj in eq_class:
                row_idx = int(obj[1:]) - 1  # Lấy chỉ số của đối tượng (ví dụ: 'o1' -> index 0)
                
                # Lấy giá trị trong cột C mà người dùng nhập vào
                value_in_C = self.df.loc[row_idx, C[0]]  # Giả sử C chỉ chứa một cột
                
                # Thêm đối tượng vào tập tương ứng
                C_sets[value_in_C].add(obj)

        # Trả về tất cả các tập tương đương (có thể có nhiều hơn 2 tập)
        return list(C_sets.values())

    def calculateDependency(self, C_sets, equivalence_classes):
        """Tính độ phụ thuộc giữa C và B theo công thức đã cho"""
        try:
            total_lower_approx = 0
            total_elements_in_C = 0
            
            # Duyệt qua từng tập C trong C_sets
            for C_set in C_sets:
                # Tính xấp xỉ dưới của mỗi C_set với các lớp tương đương từ B
                lower_approx_of_C = self.lowerApproximation(C_set, equivalence_classes)
                total_lower_approx += len(lower_approx_of_C)  # Thêm số phần tử vào tổng xấp xỉ dưới
                
                total_elements_in_C += len(C_set)  # Thêm số phần tử vào tổng số phần tử của C
            
            # Tính Dependency theo công thức
            dependency = total_lower_approx / total_elements_in_C if total_elements_in_C > 0 else 0
            
            return dependency
        except Exception as e:
            print(f"Lỗi khi tính dependency: {e}")
            return 0

    def computeEquivalenceClasses(self, B):
        """Tạo lớp tương đương từ các giá trị trong tập B"""
        equivalence_classes = defaultdict(set)
        for i, row in self.df.iterrows():
            key = tuple(row[col] for col in B)  # Lấy giá trị của các thuộc tính trong B
            equivalence_classes[key].add(f"o{i+1}")  # Gắn nhãn "o1", "o2", ... vào lớp tương đương
        return equivalence_classes

    def findReduct(self):
        """Tìm Reduct từ tập thuộc tính trong dữ liệu và hiển thị các luật phân lớp"""
        try:
            # Lấy thuộc tính quyết định và các thuộc tính điều kiện từ giao diện
            decision_attribute = self.decision_input.currentText()
            selected_conditions = [item.text() for item in self.condition_input.selectedItems()]

            if not decision_attribute or not selected_conditions:
                self.resultText4.setText("Vui lòng chọn cả thuộc tính quyết định và thuộc tính điều kiện.")
                return

            # Loại bỏ cột quyết định khỏi các thuộc tính điều kiện
            columns = self.df.columns
            attributes = [col for col in columns if col != decision_attribute]

            # Tìm các tập rút gọn với các thuộc tính điều kiện đã chọn
            reducts = self.find_reducts(self.df, decision_attribute, selected_conditions)

            if reducts:
                self.resultText4.clear()
                self.resultText4.append(f"<b>Các tập Reduct tìm được:</b><br>{'<br>'.join([', '.join(reduct) for reduct in reducts])}<br><br>")

                # Hiển thị các luật phân lớp từ các tập rút gọn
                for reduct in reducts:
                    rules = self.generate_classification(self.df, reduct, decision_attribute)
                    self.resultText4.append(f"<b>Luật phân lớp cho tập Reduct {', '.join(reduct)}:</b><br>{'<br>'.join(rules)}<br>")
            else:
                self.resultText4.setText("Không tìm thấy tập Reduct.")

        except Exception as e:
            self.resultText4.setText(f"Đã xảy ra lỗi: {str(e)}")

    def find_reducts(self, df, decision_column, attributes):
        """Tìm các tập rút gọn"""
        from itertools import combinations
        reducts = []

        # Tìm tất cả các tổ hợp thuộc tính
        for r in range(1, len(attributes) + 1):
            for subset in combinations(attributes, r):
                grouped = df.groupby(list(subset))[decision_column].nunique()
                if grouped.eq(1).all():
                    reducts.append(set(subset))  # Lưu tập rút gọn

        # Loại bỏ tập dư thừa (chỉ giữ tập rút gọn tối thiểu)
        minimal_reducts = []
        for reduct in reducts:
            if not any(reduct > other for other in reducts if reduct != other):
                minimal_reducts.append(reduct)
        return minimal_reducts

    def generate_classification(self, df, reduct, decision_column):
        """Tạo luật phân lớp từ tập rút gọn"""
        rules = []
        for _, subset in df.groupby(list(reduct)):
            decision_values = subset[decision_column].unique()
            if len(decision_values) == 1:
                decision_value = decision_values[0]
                conditions = " AND ".join([f"{col} = '{subset[col].iloc[0]}'" for col in reduct])
                rules.append(f"IF {conditions} THEN {decision_column} = '{decision_value}'")
        return rules