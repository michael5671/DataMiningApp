from PySide6.QtWidgets import QMainWindow, QMenu, QButtonGroup, QVBoxLayout, QLabel, QSizePolicy
from PySide6.QtGui import QAction, QMovie
from PySide6.QtCore import Qt, QPoint
from ui_index import Ui_MainWindow
from modules.TienXuLy import TienXuLy
from modules.TapPhoBien import TapPhoBien
from modules.TapTho import TapTho
from modules.CayQuyetDinh import CayQuyetDinh
from modules.Bayes import Bayes
from modules.KMean import KMean
from modules.Konohen import Konohen


class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Pickadata")
        # Tạo QLabel để chứa nền động
        self.header_background = QLabel(self.header_widget)
        self.header_background.setScaledContents(True)
        self.header_background.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.header_background.lower()  # Đặt QLabel dưới các thành phần khác

        # Thêm ảnh GIF động
        self.movie = QMovie("headerbg.gif")  # Thay bằng đường dẫn GIF
        self.header_background.setMovie(self.movie)
        self.movie.start()

        # Thêm QLabel vào layout của header_widget
        layout = QVBoxLayout(self.header_widget)
        layout.addWidget(self.header_background)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.header_widget.setLayout(layout)

        # Đảm bảo các thành phần khác nằm phía trên
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.icon_only_widget.setHidden(True)

        
        self.phanlop_dropdown.hide()
        self.gomcum_dropdown.hide()
        self.PhanLop1.clicked.connect(self.toggle_phanlop_dropdown)
        self.GomCum1.clicked.connect(self.toggle_gomcum_dropdown)

        
        
        #Switch giữa các trang
        self.pages = [
            TienXuLy(),
            TapPhoBien(),
            TapTho(),
            CayQuyetDinh(),
            Bayes(),
            KMean(),
            Konohen(),
        ]

        for page in self.pages:
            self.stackedWidget.addWidget(page)
        
        layout = QVBoxLayout(self.main_screen_widget)  # Sử dụng QVBoxLayout
        layout.addWidget(self.stackedWidget)  # Thêm stackedWidget vào layout
        layout.setContentsMargins(0, 0, 0, 0)  # Đặt margin bằng 0
        layout.setSpacing(0)
        self.main_screen_widget.setLayout(layout) 
        
        # Thêm các widget thực tế
        for page in self.pages:
            self.stackedWidget.addWidget(page)

        # Button list
        self.buttons = [
            self.TienXL1,
            self.TapPB1,
            self.TapTho1,
            self.CayQD,
            self.NaiveBayes,
            self.KMean,
            self.Konohen,
        ]

        # Button group
        self.button_group = QButtonGroup(self)
        for btn in self.buttons:
            btn.setCheckable(True)
            self.button_group.addButton(btn)
    
        # Liên kết các nút sidebar với trang tương ứng
        self.TienXL1.clicked.connect(lambda: self.switch_page(0))  # Tiền xử lý
        self.TienXL2.clicked.connect(lambda: self.switch_page(0))
        self.TapPB1.clicked.connect(lambda: self.switch_page(1))  # Tập phổ biến
        self.TapPB2.clicked.connect(lambda: self.switch_page(1)) 
        self.TapTho1.clicked.connect(lambda: self.switch_page(2))  # Tập thô
        self.TapTho1_2.clicked.connect(lambda: self.switch_page(2)) 
        self.CayQD.clicked.connect(lambda: self.switch_page(3))  # Cây quyết định
        self.NaiveBayes.clicked.connect(lambda: self.switch_page(4))  # Naive Bayes
        self.KMean.clicked.connect(lambda: self.switch_page(5))  # K-Means
        self.Konohen.clicked.connect(lambda: self.switch_page(6))  # Kohonen
        self.PhanLop2.clicked.connect(self.show_phanlop_menu)
        self.GomCum2.clicked.connect(self.show_gomcum_menu)

        # Update button state when clicked
        self.button_group.buttonClicked.connect(self.update_button_state)
    
    def toggle_phanlop_dropdown(self):
        """Ẩn/hiện dropdown menu cho phân lớp"""
        if self.phanlop_dropdown.isVisible():
            self.phanlop_dropdown.hide()
        else:
            self.phanlop_dropdown.show()

    def toggle_gomcum_dropdown(self):
        """Ẩn/hiện dropdown menu cho gom cụm"""
        if self.gomcum_dropdown.isVisible():
            self.gomcum_dropdown.hide()
        else:
            self.gomcum_dropdown.show()

    def show_phanlop_menu(self):
        """Hiển thị menu ngữ cảnh cho nút Phân Lớp."""
        menu = QMenu(self)
        menu.setStyleSheet("""
        QMenu {
            background-color: black;
            color: white;
            border: 1px solid #5C3B8F;
            font-family: Montserrat;
            font-size: 14px;
        }
        QMenu::item {
            padding: 8px 20px;
        }
        QMenu::item:selected {
            background-color: #9457AD;
            color: white;
        }
        """)

        cay_quyet_dinh_action = QAction("Cây Quyết Định", self)
        naive_bayes_action = QAction("Naive Bayes", self)

        # Gắn các hành động vào menu
        menu.addAction(cay_quyet_dinh_action)
        menu.addAction(naive_bayes_action)

        # Gắn sự kiện cho các lựa chọn
        cay_quyet_dinh_action.triggered.connect(lambda: self.switch_page(3))  # Chuyển đến Cây Quyết Định
        naive_bayes_action.triggered.connect(lambda: self.switch_page(4))  # Chuyển đến Naive Bayes

        # Hiển thị menu tại vị trí của nút
        button_pos = self.PhanLop2.mapToGlobal(QPoint(50, self.PhanLop2.height()))
        menu.exec(button_pos)

    def show_gomcum_menu(self):
        """Hiển thị menu ngữ cảnh cho nút Gom Cụm."""
        menu = QMenu(self)
        menu.setStyleSheet("""
        QMenu {
            background-color: black;
            color: white;
            border: 1px solid #5C3B8F;
            font-family: Montserrat;
            font-size: 14px;
        }
        QMenu::item {
            padding: 8px 20px;
        }
        QMenu::item:selected {
            background-color: #9457AD;
            color: white;
        }
        """)

        kmean_action = QAction("K-Means", self)
        konohen_action = QAction("Kohonen", self)

        # Gắn các hành động vào menu
        menu.addAction(kmean_action)
        menu.addAction(konohen_action)

        # Gắn sự kiện cho các lựa chọn
        kmean_action.triggered.connect(lambda: self.switch_page(5))  # Chuyển đến K-Means
        konohen_action.triggered.connect(lambda: self.switch_page(6))  # Chuyển đến Kohonen

        # Hiển thị menu tại vị trí của nút
        button_pos = self.GomCum2.mapToGlobal(QPoint(50, self.GomCum2.height()))
        menu.exec(button_pos)
    
    def update_button_state(self, clicked_button):
        """Ensure only one button is highlighted at a time."""
        for btn in self.buttons:
            btn.setChecked(btn == clicked_button)

    def switch_page(self, index):
        """Chuyển đến trang cụ thể trong QStackedWidget"""
        self.stackedWidget.setCurrentIndex(index)
    
    