# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import asset_rc
import asset_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1368, 790)
        MainWindow.setMinimumSize(QSize(1360, 790))
        MainWindow.setMaximumSize(QSize(16777215, 790))
        font = QFont()
        font.setFamilies([u"roboto"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"font-family:roboto;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(1370, 879))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 1371, 791))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.layoutWidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setMinimumSize(QSize(110, 789))
        self.icon_only_widget.setMaximumSize(QSize(110, 789))
        self.icon_only_widget.setStyleSheet(u"QWidget {\n"
"	background-color: #2F0746;\n"
"color: white;	\n"
"}\n"
"QPushButton{\n"
"	border:none;\n"
"	padding-bottom: 10px;\n"
"	\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: #5C3B8F;\n"
"	border-radius: 10px; \n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #5C3B8F;\n"
"	border-radius: 10px; \n"
"}\n"
"")
        self.verticalLayout_7 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 13, -1, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_4 = QLabel(self.icon_only_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(80, 80))
        self.label_4.setPixmap(QPixmap(u":/images/asset/logo.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.line_2 = QFrame(self.icon_only_widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setLineWidth(0)
        self.line_2.setMidLineWidth(1)
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self.line_2)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(18)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 28, -1, -1)
        self.TienXL2 = QPushButton(self.icon_only_widget)
        self.TienXL2.setObjectName(u"TienXL2")
        self.TienXL2.setMinimumSize(QSize(0, 50))
        icon = QIcon()
        icon.addFile(u":/images/asset/table-list.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.TienXL2.setIcon(icon)
        self.TienXL2.setIconSize(QSize(35, 35))
        self.TienXL2.setCheckable(True)
        self.TienXL2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.TienXL2)

        self.TapPB2 = QPushButton(self.icon_only_widget)
        self.TapPB2.setObjectName(u"TapPB2")
        self.TapPB2.setMinimumSize(QSize(0, 50))
        icon1 = QIcon()
        icon1.addFile(u":/images/asset/circle-nodes-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.TapPB2.setIcon(icon1)
        self.TapPB2.setIconSize(QSize(35, 35))
        self.TapPB2.setCheckable(True)
        self.TapPB2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.TapPB2)

        self.TapTho1_2 = QPushButton(self.icon_only_widget)
        self.TapTho1_2.setObjectName(u"TapTho1_2")
        self.TapTho1_2.setMinimumSize(QSize(0, 50))
        icon2 = QIcon()
        icon2.addFile(u":/images/asset/list-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.TapTho1_2.setIcon(icon2)
        self.TapTho1_2.setIconSize(QSize(35, 35))
        self.TapTho1_2.setCheckable(True)
        self.TapTho1_2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.TapTho1_2)

        self.PhanLop2 = QPushButton(self.icon_only_widget)
        self.PhanLop2.setObjectName(u"PhanLop2")
        self.PhanLop2.setMinimumSize(QSize(0, 50))
        icon3 = QIcon()
        icon3.addFile(u":/images/asset/sitemap-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PhanLop2.setIcon(icon3)
        self.PhanLop2.setIconSize(QSize(35, 35))
        self.PhanLop2.setCheckable(True)
        self.PhanLop2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.PhanLop2)

        self.GomCum2 = QPushButton(self.icon_only_widget)
        self.GomCum2.setObjectName(u"GomCum2")
        self.GomCum2.setMinimumSize(QSize(0, 50))
        icon4 = QIcon()
        icon4.addFile(u":/images/asset/object-ungroup-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.GomCum2.setIcon(icon4)
        self.GomCum2.setIconSize(QSize(35, 35))
        self.GomCum2.setCheckable(True)
        self.GomCum2.setAutoExclusive(True)

        self.verticalLayout_6.addWidget(self.GomCum2)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.verticalSpacer_2 = QSpacerItem(20, 320, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.line_4 = QFrame(self.icon_only_widget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setLineWidth(0)
        self.line_4.setMidLineWidth(1)
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self.line_4)

        self.pushButton_7 = QPushButton(self.icon_only_widget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        icon5 = QIcon()
        icon5.addFile(u":/images/asset/log-out.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_7.setIcon(icon5)
        self.pushButton_7.setIconSize(QSize(35, 35))
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setChecked(False)
        self.pushButton_7.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.pushButton_7)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.header_widget = QWidget(self.layoutWidget)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setMinimumSize(QSize(845, 71))
        self.header_widget.setMaximumSize(QSize(16777215, 16777215))
#         self.header_widget.setStyleSheet(u"QWidget{\n"
# "	\n"
# "	background-image: url(:/images/asset/last_background.jpg);\n"
# "\n"
# "}")
        self.layoutWidget1 = QWidget(self.header_widget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 10, 836, 82))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 15)
        self.pushButton = QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"	background: transparent;\n"
"	border:none;\n"
"	\n"
"\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/images/asset/bars-solid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon6)
        self.pushButton.setIconSize(QSize(35, 35))
        self.pushButton.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(9)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, -1, -1, 15)
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"roboto"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: white;\n"
"background: transparent;")

        self.verticalLayout_9.addWidget(self.label)

        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamilies([u"roboto"])
        font2.setPointSize(11)
        font2.setBold(False)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: white;\n"
"background: transparent;")

        self.verticalLayout_9.addWidget(self.label_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_9)

        self.horizontalSpacer_3 = QSpacerItem(500, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_10.addWidget(self.header_widget)

        self.main_screen_widget = QWidget(self.layoutWidget)
        self.main_screen_widget.setObjectName(u"main_screen_widget")
        self.main_screen_widget.setMinimumSize(QSize(931, 701))
        self.main_screen_widget.setMaximumSize(QSize(16777215, 16777215))
        self.main_screen_widget.setStyleSheet(u"background-color: white;\n"
"border:none;")
        self.stackedWidget = QStackedWidget(self.main_screen_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 841, 691))
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        self.stackedWidget.setStyleSheet(u"")

        self.verticalLayout_10.addWidget(self.main_screen_widget)


        self.gridLayout.addLayout(self.verticalLayout_10, 0, 2, 1, 1)

        self.icon_text_widget = QWidget(self.layoutWidget)
        self.icon_text_widget.setObjectName(u"icon_text_widget")
        self.icon_text_widget.setMinimumSize(QSize(310, 789))
        self.icon_text_widget.setMaximumSize(QSize(305, 789))
        self.icon_text_widget.setStyleSheet(u"QWidget {\n"
"	\n"
"	background-color: #2F0746;\n"
"color: white;	\n"
"\n"
"}\n"
"QPushButton{\n"
"	border:none;\n"
"	\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout_8 = QVBoxLayout(self.icon_text_widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 18, 5, 5)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(self.icon_text_widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(71, 71))
        self.label_5.setPixmap(QPixmap(u":/images/asset/logo.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(self.icon_text_widget)
        self.label_6.setObjectName(u"label_6")
        font3 = QFont()
        font3.setFamilies([u"roboto"])
        font3.setPointSize(18)
        font3.setBold(True)
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.label_6)


        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.line = QFrame(self.icon_text_widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line.setLineWidth(0)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_8.addWidget(self.line)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(18)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 28, 0, -1)
        self.TienXL1 = QPushButton(self.icon_text_widget)
        self.TienXL1.setObjectName(u"TienXL1")
        self.TienXL1.setMinimumSize(QSize(300, 45))
        font4 = QFont()
        font4.setFamilies([u"roboto"])
        font4.setPointSize(11)
        font4.setBold(True)
        self.TienXL1.setFont(font4)
        self.TienXL1.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	padding-left: -55px;\n"
"\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: #5C3B8F;\n"
"	border-radius: 8px; \n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #5C3B8F;\n"
"	border-radius: 8px; \n"
"	font-size: 16px;\n"
"	padding-left: -75px;\n"
"}")
        self.TienXL1.setIcon(icon)
        self.TienXL1.setIconSize(QSize(30, 30))
        self.TienXL1.setCheckable(True)
        self.TienXL1.setAutoRepeat(False)
        self.TienXL1.setAutoExclusive(False)

        self.verticalLayout_5.addWidget(self.TienXL1)

        self.TapPB1 = QPushButton(self.icon_text_widget)
        self.TapPB1.setObjectName(u"TapPB1")
        self.TapPB1.setMinimumSize(QSize(300, 45))
        self.TapPB1.setFont(font4)
        self.TapPB1.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	padding-left: 15px;\n"
"	\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: #5C3B8F;\n"
"	border-radius: 8px; \n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #5C3B8F;\n"
"	border-radius: 8px; \n"
"	font-size: 16px;\n"
"	padding-left: -26px;\n"
"}")
        self.TapPB1.setIcon(icon1)
        self.TapPB1.setIconSize(QSize(30, 32))
        self.TapPB1.setCheckable(True)
        self.TapPB1.setAutoRepeat(False)
        self.TapPB1.setAutoExclusive(False)

        self.verticalLayout_5.addWidget(self.TapPB1)

        self.TapTho1 = QPushButton(self.icon_text_widget)
        self.TapTho1.setObjectName(u"TapTho1")
        self.TapTho1.setMinimumSize(QSize(300, 45))
        self.TapTho1.setFont(font4)
        self.TapTho1.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	padding-left: -120px;\n"
"	\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: #5C3B8F;\n"
"	border-radius: 8px; \n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #5C3B8F;\n"
"	border-radius: 8px; \n"
"	font-size: 16px;\n"
"	padding-left: -135px;\n"
"}")
        self.TapTho1.setIcon(icon2)
        self.TapTho1.setIconSize(QSize(30, 30))
        self.TapTho1.setCheckable(True)
        self.TapTho1.setAutoExclusive(False)

        self.verticalLayout_5.addWidget(self.TapTho1)

        self.phanLop = QFrame(self.icon_text_widget)
        self.phanLop.setObjectName(u"phanLop")
        self.phanLop.setFrameShape(QFrame.Shape.StyledPanel)
        self.phanLop.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.phanLop)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.PhanLop1 = QPushButton(self.phanLop)
        self.PhanLop1.setObjectName(u"PhanLop1")
        self.PhanLop1.setMinimumSize(QSize(300, 45))
        font5 = QFont()
        font5.setFamilies([u"roboto"])
        font5.setPointSize(11)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setStrikeOut(False)
        self.PhanLop1.setFont(font5)
        self.PhanLop1.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	padding-left: -60px;\n"
"	\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #5C3B8F;\n"
"	border-radius: 8px; \n"
"	font-size: 16px;\n"
"	padding-left: -75px;\n"
"}")
        self.PhanLop1.setIcon(icon3)
        self.PhanLop1.setIconSize(QSize(30, 30))
        self.PhanLop1.setCheckable(True)
        self.PhanLop1.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.PhanLop1)

        self.phanlop_dropdown = QFrame(self.phanLop)
        self.phanlop_dropdown.setObjectName(u"phanlop_dropdown")
        self.phanlop_dropdown.setStyleSheet(u"")
        self.phanlop_dropdown.setFrameShape(QFrame.Shape.StyledPanel)
        self.phanlop_dropdown.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.phanlop_dropdown)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.CayQD = QPushButton(self.phanlop_dropdown)
        self.CayQD.setObjectName(u"CayQD")
        self.CayQD.setMinimumSize(QSize(300, 45))
        font6 = QFont()
        font6.setFamilies([u"roboto"])
        font6.setPointSize(11)
        font6.setBold(True)
        font6.setItalic(False)
        self.CayQD.setFont(font6)
        self.CayQD.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	padding-left: -95px;\n"
"	\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #5C3B8F;\n"
"	border-radius: 8px; \n"
"	font-size: 16px;\n"
"	padding-left: -105px;	\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: #5C3B8F;\n"
"	border-radius: 8px; \n"
"	\n"
"}")
        self.CayQD.setCheckable(True)
        self.CayQD.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.CayQD)

        self.NaiveBayes = QPushButton(self.phanlop_dropdown)
        self.NaiveBayes.setObjectName(u"NaiveBayes")
        self.NaiveBayes.setMinimumSize(QSize(300, 45))
        self.NaiveBayes.setFont(font4)
        self.NaiveBayes.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	padding-left: -110px;\n"
"	\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #5C3B8F;\n"
"	border-radius: 8px; \n"
"	font-size: 16px;\n"
"	padding-left: -115px;	\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: #5C3B8F;\n"
"	border-radius: 8px; \n"
"}")
        self.NaiveBayes.setCheckable(True)
        self.NaiveBayes.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.NaiveBayes)


        self.verticalLayout_3.addWidget(self.phanlop_dropdown)


        self.verticalLayout_5.addWidget(self.phanLop)

        self.gomCum = QFrame(self.icon_text_widget)
        self.gomCum.setObjectName(u"gomCum")
        self.gomCum.setFrameShape(QFrame.Shape.StyledPanel)
        self.gomCum.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.gomCum)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.GomCum1 = QPushButton(self.gomCum)
        self.GomCum1.setObjectName(u"GomCum1")
        self.GomCum1.setMinimumSize(QSize(300, 45))
        self.GomCum1.setFont(font4)
        self.GomCum1.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	padding-left: -105px;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #5C3B8F;\n"
"	border-radius: 8px; \n"
"	font-size: 16px;\n"
"	padding-left: -120px;	\n"
"}")
        self.GomCum1.setIcon(icon4)
        self.GomCum1.setIconSize(QSize(30, 30))
        self.GomCum1.setCheckable(True)
        self.GomCum1.setAutoExclusive(False)

        self.verticalLayout_4.addWidget(self.GomCum1)

        self.gomcum_dropdown = QFrame(self.gomCum)
        self.gomcum_dropdown.setObjectName(u"gomcum_dropdown")
        self.gomcum_dropdown.setFrameShape(QFrame.Shape.StyledPanel)
        self.gomcum_dropdown.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.gomcum_dropdown)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.KMean = QPushButton(self.gomcum_dropdown)
        self.KMean.setObjectName(u"KMean")
        self.KMean.setMinimumSize(QSize(300, 45))
        self.KMean.setFont(font4)
        self.KMean.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	padding-left: -125px;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #5C3B8F;\n"
"	border-radius: 8px; \n"
"	font-size: 16px;\n"
"	padding-left: -135px;	\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: #5C3B8F;\n"
"	border-radius: 8px; \n"
"}")
        self.KMean.setCheckable(True)
        self.KMean.setAutoExclusive(False)

        self.verticalLayout_2.addWidget(self.KMean)

        self.Konohen = QPushButton(self.gomcum_dropdown)
        self.Konohen.setObjectName(u"Konohen")
        self.Konohen.setMinimumSize(QSize(300, 45))
        self.Konohen.setFont(font4)
        self.Konohen.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	padding-left: -125px;\n"
"	\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #5C3B8F;\n"
"	border-radius: 8px; \n"
"	font-size: 16px;\n"
"	padding-left: -135px;	\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: #5C3B8F;\n"
"	border-radius: 8px; \n"
"}")
        self.Konohen.setCheckable(True)
        self.Konohen.setAutoExclusive(False)

        self.verticalLayout_2.addWidget(self.Konohen)


        self.verticalLayout_4.addWidget(self.gomcum_dropdown)


        self.verticalLayout_5.addWidget(self.gomCum)


        self.verticalLayout_8.addLayout(self.verticalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 364, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.line_3 = QFrame(self.icon_text_widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setLineWidth(0)
        self.line_3.setMidLineWidth(1)
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_8.addWidget(self.line_3)

        self.pushButton_12 = QPushButton(self.icon_text_widget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(0, 45))
        self.pushButton_12.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: #5C3B8F;\n"
"	border-radius: 10px; \n"
"}")
        self.pushButton_12.setIcon(icon5)
        self.pushButton_12.setIconSize(QSize(32, 32))
        self.pushButton_12.setCheckable(True)

        self.verticalLayout_8.addWidget(self.pushButton_12)


        self.gridLayout.addWidget(self.icon_text_widget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.PhanLop1.toggled.connect(self.phanlop_dropdown.setHidden)
        self.GomCum1.toggled.connect(self.gomcum_dropdown.setHidden)
        self.TienXL1.toggled.connect(self.TienXL2.setChecked)
        self.TapPB1.toggled.connect(self.TapPB2.setChecked)
        self.TapTho1.toggled.connect(self.TapTho1_2.setChecked)
        self.PhanLop1.toggled.connect(self.PhanLop2.setChecked)
        self.GomCum1.toggled.connect(self.GomCum2.setChecked)
        self.pushButton_12.toggled.connect(self.pushButton_7.setChecked)
        self.pushButton_7.toggled.connect(MainWindow.close)
        self.pushButton_12.toggled.connect(MainWindow.close)
        self.pushButton.toggled.connect(self.icon_text_widget.setHidden)
        self.pushButton.toggled.connect(self.icon_only_widget.setVisible)
        self.KMean.toggled.connect(self.GomCum2.setChecked)

        self.stackedWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText("")
        self.TienXL2.setText("")
        self.TapPB2.setText("")
        self.TapTho1_2.setText("")
        self.PhanLop2.setText("")
        self.GomCum2.setText("")
        self.pushButton_7.setText("")
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ch\u00e0o m\u1eebng \u0111\u00e3 quay l\u1ea1i!", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"H\u00e3y bi\u1ebfn d\u1eef li\u1ec7u c\u1ee7a b\u1ea1n tr\u1edf th\u00e0nh th\u00f4ng tin b\u1ed5 \u00edch.", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"PICKADATA", None))
        self.TienXL1.setText(QCoreApplication.translate("MainWindow", u"    Ti\u1ec1n x\u1eed l\u00fd d\u1eef li\u1ec7u", None))
        self.TapPB1.setText(QCoreApplication.translate("MainWindow", u"    T\u1eadp ph\u1ed5 bi\u1ebfn, Lu\u1eadt k\u1ebft h\u1ee3p", None))
        self.TapTho1.setText(QCoreApplication.translate("MainWindow", u"    T\u1eadp Th\u00f4", None))
        self.PhanLop1.setText(QCoreApplication.translate("MainWindow", u"    Ph\u00e2n l\u1edbp d\u1eef li\u1ec7u", None))
        self.CayQD.setText(QCoreApplication.translate("MainWindow", u"    C\u00e2y quy\u1ebft \u0111\u1ecbnh", None))
        self.NaiveBayes.setText(QCoreApplication.translate("MainWindow", u"    Naive Bayes", None))
        self.GomCum1.setText(QCoreApplication.translate("MainWindow", u"    Gom c\u1ee5m", None))
        self.KMean.setText(QCoreApplication.translate("MainWindow", u"    K Means", None))
        self.Konohen.setText(QCoreApplication.translate("MainWindow", u"    Konohen", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"THO\u00c1T", None))
    # retranslateUi

