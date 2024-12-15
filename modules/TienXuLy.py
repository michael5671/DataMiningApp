from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QFileDialog, QHBoxLayout, QGridLayout
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
import pandas as pd
from scipy.stats import pearsonr


class TienXuLy(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Tiền Xử Lý Dữ Liệu")
        self.setStyleSheet("background-color: white; color: black;")
        layout = QVBoxLayout()
        layout.setSpacing(15)

        label = QLabel("Tiền Xử Lý Dữ Liệu", self)
        label.setFont(QFont("Arial", 18, QFont.Bold))
        label.setAlignment(Qt.AlignCenter)
        label.setFixedHeight(50)
        layout.addWidget(label)

        # File input section
        file_layout = QHBoxLayout()
        self.file_path_input = QLineEdit(self)
        self.file_path_input.setPlaceholderText("Chọn file Excel")
        self.file_path_input.setReadOnly(True)
        self.file_path_input.setAlignment(Qt.AlignCenter)
        file_layout.addWidget(self.file_path_input)

        file_button = QPushButton("Chọn File Excel", self)
        file_button.setStyleSheet("background-color: #4CAF50; color: black; padding: 10px;")
        file_button.clicked.connect(self.open_file_dialog)
        file_layout.addWidget(file_button)
        layout.addLayout(file_layout)

        # X input section
        x_layout = QHBoxLayout()
        self.x_input = QLineEdit(self)
        self.x_input.setPlaceholderText("Nhập thuộc tính X")
        self.x_input.setAlignment(Qt.AlignCenter)
        x_layout.addWidget(self.x_input)
        layout.addLayout(x_layout)

        # Y input section
        y_layout = QHBoxLayout()
        self.y_input = QLineEdit(self)
        self.y_input.setPlaceholderText("Nhập thuộc tính Y")
        self.y_input.setAlignment(Qt.AlignCenter)
        y_layout.addWidget(self.y_input)
        layout.addLayout(y_layout)

        # Calculate button
        calc_button = QPushButton("Tính Hệ Số Tương Quan", self)
        calc_button.setStyleSheet("background-color: #4CAF50; color: black; padding: 10px;")
        calc_button.clicked.connect(self.calculate_correlation)
        layout.addWidget(calc_button)

        # Create a grid layout for result display
        self.result_grid = QGridLayout()
        self.result_grid.setSpacing(5)

        # Result labels (N, Σxy, Σx, Σy, Σx², Σy²)
        self.result_labels = {}
        result_titles = ["N", "Σxy", "Σx", "Σy", "Σx²", "Σy²"]
        for i, title in enumerate(result_titles):
            label = QLabel(title, self)
            label.setFont(QFont("Arial", 12, QFont.Bold))
            label.setAlignment(Qt.AlignCenter)
            self.result_labels[title] = QLabel("", self)
            self.result_labels[title].setAlignment(Qt.AlignCenter)
            self.result_labels[title].setFont(QFont("Arial", 12))

            # Adding labels to grid layout
            self.result_grid.addWidget(label, i, 0)
            self.result_grid.addWidget(self.result_labels[title], i, 1)

        layout.addLayout(self.result_grid)

        # Result interpretation label
        self.result_label = QLabel(self)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("background-color: #f0f0f0; font-size: 18px; padding: 2px;")
        layout.addWidget(self.result_label)

        # Set the layout for the window
        self.setLayout(layout)

    def open_file_dialog(self):
        file, _ = QFileDialog.getOpenFileName(self, "Chọn file Excel", "", "Excel Files (*.xlsx *.xls)")
        if file:
            self.file_path_input.setText(file)

    def calculate_correlation(self):
        file_path = self.file_path_input.text()
        try:
            # Load the Excel file
            df = pd.read_excel(file_path)
            x_column = self.x_input.text()
            y_column = self.y_input.text()

            if x_column not in df.columns or y_column not in df.columns:
                self.result_label.setText("Thuộc tính không hợp lệ!")
                return

            # Clean and align data
            x_data = df[x_column].dropna()
            y_data = df[y_column].dropna()
            min_length = min(len(x_data), len(y_data))
            x_data = x_data[:min_length]
            y_data = y_data[:min_length]

            # Pearson Correlation Calculation
            correlation, _ = pearsonr(x_data, y_data)

            N = len(x_data)
            Σxy = (x_data * y_data).sum()
            Σx = x_data.sum()
            Σy = y_data.sum()
            Σx2 = (x_data ** 2).sum()
            Σy2 = (y_data ** 2).sum()

            # Update the grid with results
            self.result_labels["N"].setText(f"{N}")
            self.result_labels["Σxy"].setText(f"{Σxy:.4f}")
            self.result_labels["Σx"].setText(f"{Σx:.4f}")
            self.result_labels["Σy"].setText(f"{Σy:.4f}")
            self.result_labels["Σx²"].setText(f"{Σx2:.4f}")
            self.result_labels["Σy²"].setText(f"{Σy2:.4f}")

            # Remove any custom background colors
            for label in self.result_labels.values():
                label.setStyleSheet("background-color: white; padding: 5px;")

            # Build the result message with detailed correlation info
            result_message = f"<b>Hệ số tương quan giữa {x_column} và {y_column}: {correlation:.4f}</b><br><br><br><br><br>"
            self.result_label.setText(result_message)
            

        except Exception as e:
            self.result_label.setText(f"Đã có lỗi: {str(e)}")


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    app = QApplication([])
    window = TienXuLy()
    window.show()
    app.exec()