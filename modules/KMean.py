from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QFileDialog, QTextEdit, QSizePolicy
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class KMean(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("K-Means Clustering")
        self.setGeometry(100, 100, 1000, 600)
        self.setStyleSheet("background-color: white; color: black;")

        layout = QVBoxLayout()
        layout.setSpacing(15)

        label = QLabel("K-Means Clustering", self)
        label.setFont(QFont("Arial", 18, QFont.Bold))
        label.setAlignment(Qt.AlignCenter)
        label.setFixedHeight(50)
        layout.addWidget(label)

        # File selection layout
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

        # K value input and button
        k_layout = QHBoxLayout()
        self.k_input = QLineEdit(self)
        self.k_input.setPlaceholderText("Nhập số cụm (k)")
        self.k_input.setAlignment(Qt.AlignCenter)
        k_layout.addWidget(self.k_input)

        calc_button = QPushButton("Thực hiện K-Means", self)
        calc_button.setStyleSheet("background-color: #4CAF50; color: black; padding: 10px;")
        calc_button.clicked.connect(self.perform_kmeans_and_display_results)
        k_layout.addWidget(calc_button)

        layout.addLayout(k_layout)

        # Result display area
        self.result_display = QTextEdit(self)
        self.result_display.setReadOnly(True)
        self.result_display.setStyleSheet("background-color: #f0f0f0; font-size: 14px; padding: 10px;")
        self.result_display.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(self.result_display)

        self.setLayout(layout)

    def open_file_dialog(self):
        file, _ = QFileDialog.getOpenFileName(self, "Chọn file Excel", "", "Excel Files (*.xlsx *.xls)")
        if file:
            self.file_path_input.setText(file)

    def perform_kmeans_and_display_results(self):
        file_path = self.file_path_input.text()
        try:
            df = pd.read_excel(file_path)

            if df.empty:
                self.result_display.setText("File Excel không có dữ liệu!")
                return

            k = int(self.k_input.text())
            kmeans = KMeans(n_clusters=k, random_state=42)
            numeric_data = df.select_dtypes(include=[np.number])

            if numeric_data.shape[1] < 2:
                self.result_display.setText("Dữ liệu không đủ để thực hiện KMeans (cần ít nhất 2 cột số).")
                return

            # Perform clustering
            kmeans.fit(numeric_data)
            clusters = kmeans.predict(numeric_data)
            df['Cluster'] = clusters
            distances = kmeans.transform(numeric_data)

            # Generate results as HTML
            result_html = f"<h3>Đã phân cụm vào {k} nhóm:</h3>"
            for i in range(k):
                result_html += f"<p>Cụm {i}: {len(df[df['Cluster'] == i])} mẫu</p>"

            result_html += "<h4>Tâm cụm:</h4><ul>"
            for i, centroid in enumerate(kmeans.cluster_centers_):
                result_html += f"<li>Cụm {i}: {centroid.tolist()}</li>"
            result_html += "</ul>"

            # Add clustering table with center-aligned content
            result_html += "<h4>Bảng phân cụm:</h4>"
            result_html += """
                <style>
                    table {
                        width: 100%;
                        border-collapse: collapse;
                        margin-top: 20px;
                    }
                    th, td {
                        padding: 10px;
                        text-align: center;
                        border: 1px solid #ddd;
                    }
                    th {
                        background-color: #4CAF50;
                        color: white;
                    }
                    tr:nth-child(even) {
                        background-color: #f2f2f2;
                    }
                    tr:hover {
                        background-color: #ddd;
                    }
                </style>
            """
            result_html += "<table>"
            result_html += "<tr><th>Index</th><th>Thuộc tính</th>"

            # Add columns for distances to each cluster
            for i in range(k):
                result_html += f"<th>Khoảng cách đến Cụm {i}</th>"
            result_html += "<th>Cụm</th>"  # Move "Cụm" to the last column
            result_html += "</tr>"

            # Add table rows with distances to each cluster
            for i in range(len(df)):
                attributes = ", ".join(map(str, numeric_data.iloc[i].values))
                cluster_value = int(df.iloc[i]['Cluster'])
                row = f"<tr><td>{i}</td><td>{attributes}</td>"

                # Add distances to each cluster
                for j in range(k):
                    row += f"<td>{distances[i][j]:.2f}</td>"
                row += f"<td>{cluster_value}</td>"  # Move "Cụm" to the last column
                row += "</tr>"
                result_html += row

            result_html += "</table>"

            self.result_display.setHtml(result_html)

            # Visualize clusters
            self.visualize_clusters(df, numeric_data, kmeans)

        except Exception as e:
            self.result_display.setText(f"Lỗi khi thực hiện K-Means: {e}")

    def visualize_clusters(self, df, numeric_data, kmeans):
        try:
            plt.figure(figsize=(6, 4))
            cmap = plt.cm.get_cmap('tab10')

            x_min, x_max = numeric_data.iloc[:, 0].min() - 1, numeric_data.iloc[:, 0].max() + 1
            y_min, y_max = numeric_data.iloc[:, 1].min() - 1, numeric_data.iloc[:, 1].max() + 1
            plt.xlim(x_min, x_max)
            plt.ylim(y_min, y_max)

            for cluster in np.unique(df['Cluster']):
                cluster_data = numeric_data[df['Cluster'] == cluster]
                plt.scatter(cluster_data.iloc[:, 0], cluster_data.iloc[:, 1],
                            label=f"Cụm {cluster}")

            centroids = kmeans.cluster_centers_
            plt.scatter(centroids[:, 0], centroids[:, 1], color='black', marker='X', s=100, label="Tâm Cụm")

            plt.title("K-Means Clustering Visualization", fontsize=12)
            plt.xlabel("Feature 1", fontsize=10)
            plt.ylabel("Feature 2", fontsize=10)
            plt.legend()
            plt.grid(True, linestyle='--', alpha=0.7)

            plt.show()

        except Exception as e:
            self.result_display.setText(f"Lỗi khi vẽ đồ thị phân cụm: {e}")

# Run application
if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    app = QApplication([])
    window = KMean()
    window.show()
    app.exec()