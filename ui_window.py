# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(810, 602)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(0, 85, 127);")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(50, 50))
        self.label.setPixmap(QPixmap(u":/images/open-book.png"))
        self.label.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.dashboard_btn_1 = QPushButton(self.widget)
        self.dashboard_btn_1.setObjectName(u"dashboard_btn_1")
        self.dashboard_btn_1.setStyleSheet(u"QPushButton { \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: #1E6FD9; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        icon = QIcon()
        icon.addFile(u":/images/menu (2).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.dashboard_btn_1.setIcon(icon)
        self.dashboard_btn_1.setIconSize(QSize(40, 40))
        self.dashboard_btn_1.setCheckable(True)

        self.verticalLayout_2.addWidget(self.dashboard_btn_1)

        self.books_btn_1 = QPushButton(self.widget)
        self.books_btn_1.setObjectName(u"books_btn_1")
        self.books_btn_1.setStyleSheet(u"QPushButton { \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: #1E6FD9; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        icon1 = QIcon()
        icon1.addFile(u":/images/stack-of-books.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.books_btn_1.setIcon(icon1)
        self.books_btn_1.setIconSize(QSize(40, 40))
        self.books_btn_1.setCheckable(True)

        self.verticalLayout_2.addWidget(self.books_btn_1)

        self.returned_btn_1 = QPushButton(self.widget)
        self.returned_btn_1.setObjectName(u"returned_btn_1")
        self.returned_btn_1.setStyleSheet(u"QPushButton { \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: #1E6FD9; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        icon2 = QIcon()
        icon2.addFile(u":/images/return.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.returned_btn_1.setIcon(icon2)
        self.returned_btn_1.setIconSize(QSize(40, 40))
        self.returned_btn_1.setCheckable(True)

        self.verticalLayout_2.addWidget(self.returned_btn_1)

        self.borrowed_btn_1 = QPushButton(self.widget)
        self.borrowed_btn_1.setObjectName(u"borrowed_btn_1")
        self.borrowed_btn_1.setStyleSheet(u"QPushButton { \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: #1E6FD9; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        icon3 = QIcon()
        icon3.addFile(u":/images/book.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.borrowed_btn_1.setIcon(icon3)
        self.borrowed_btn_1.setIconSize(QSize(40, 40))
        self.borrowed_btn_1.setCheckable(True)

        self.verticalLayout_2.addWidget(self.borrowed_btn_1)

        self.fines_btn_1 = QPushButton(self.widget)
        self.fines_btn_1.setObjectName(u"fines_btn_1")
        self.fines_btn_1.setStyleSheet(u"QPushButton { \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: #1E6FD9; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        icon4 = QIcon()
        icon4.addFile(u":/images/penalty.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.fines_btn_1.setIcon(icon4)
        self.fines_btn_1.setIconSize(QSize(40, 40))
        self.fines_btn_1.setCheckable(True)

        self.verticalLayout_2.addWidget(self.fines_btn_1)

        self.transaction_btn_1 = QPushButton(self.widget)
        self.transaction_btn_1.setObjectName(u"transaction_btn_1")
        self.transaction_btn_1.setStyleSheet(u"QPushButton { \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: #1E6FD9; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        icon5 = QIcon()
        icon5.addFile(u":/images/Webiconset-E-Commerce-Secure-payment.128.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.transaction_btn_1.setIcon(icon5)
        self.transaction_btn_1.setIconSize(QSize(40, 40))
        self.transaction_btn_1.setCheckable(True)

        self.verticalLayout_2.addWidget(self.transaction_btn_1)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 46, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pushButton_6 = QPushButton(self.widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"QPushButton { \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: #1E6FD9; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        icon6 = QIcon()
        icon6.addFile(u":/images/logout.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_6.setIcon(icon6)
        self.pushButton_6.setIconSize(QSize(40, 40))
        self.pushButton_6.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pushButton_6)


        self.gridLayout.addWidget(self.widget, 0, 0, 2, 1)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color: rgb(0, 85, 127);")
        self.verticalLayout_5 = QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(65, 65))
        self.label_2.setPixmap(QPixmap(u":/images/open-book.png"))
        self.label_2.setScaledContents(True)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 600 18pt \"Segoe UI\";")

        self.verticalLayout.addWidget(self.label_3)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.dashboard_btn_2 = QPushButton(self.widget_2)
        self.dashboard_btn_2.setObjectName(u"dashboard_btn_2")
        self.dashboard_btn_2.setStyleSheet(u"QPushButton { \n"
"background-color: #2D89EF; \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: #1E6FD9; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        self.dashboard_btn_2.setIcon(icon)
        self.dashboard_btn_2.setIconSize(QSize(20, 20))
        self.dashboard_btn_2.setCheckable(True)

        self.verticalLayout_4.addWidget(self.dashboard_btn_2)

        self.books_btn_2 = QPushButton(self.widget_2)
        self.books_btn_2.setObjectName(u"books_btn_2")
        self.books_btn_2.setStyleSheet(u"QPushButton { \n"
"background-color: #2D89EF; \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: #1E6FD9; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        self.books_btn_2.setIcon(icon1)
        self.books_btn_2.setIconSize(QSize(20, 20))
        self.books_btn_2.setCheckable(True)
        self.books_btn_2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.books_btn_2)

        self.returned_btn_2 = QPushButton(self.widget_2)
        self.returned_btn_2.setObjectName(u"returned_btn_2")
        self.returned_btn_2.setStyleSheet(u"QPushButton { \n"
"background-color: #2D89EF; \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: #1E6FD9; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        self.returned_btn_2.setIcon(icon2)
        self.returned_btn_2.setIconSize(QSize(20, 20))
        self.returned_btn_2.setCheckable(True)
        self.returned_btn_2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.returned_btn_2)

        self.borrowed_btn_2 = QPushButton(self.widget_2)
        self.borrowed_btn_2.setObjectName(u"borrowed_btn_2")
        self.borrowed_btn_2.setStyleSheet(u"QPushButton { \n"
"background-color: #2D89EF; \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: #1E6FD9; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        self.borrowed_btn_2.setIcon(icon3)
        self.borrowed_btn_2.setIconSize(QSize(20, 20))
        self.borrowed_btn_2.setCheckable(True)
        self.borrowed_btn_2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.borrowed_btn_2)

        self.fines_btn_2 = QPushButton(self.widget_2)
        self.fines_btn_2.setObjectName(u"fines_btn_2")
        self.fines_btn_2.setStyleSheet(u"QPushButton { \n"
"background-color: #2D89EF; \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: #1E6FD9; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        self.fines_btn_2.setIcon(icon4)
        self.fines_btn_2.setIconSize(QSize(20, 20))
        self.fines_btn_2.setCheckable(True)

        self.verticalLayout_4.addWidget(self.fines_btn_2)

        self.transaction_btn_2 = QPushButton(self.widget_2)
        self.transaction_btn_2.setObjectName(u"transaction_btn_2")
        self.transaction_btn_2.setStyleSheet(u"QPushButton { \n"
"background-color: #2D89EF; \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: #1E6FD9; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        self.transaction_btn_2.setIcon(icon5)
        self.transaction_btn_2.setIconSize(QSize(20, 20))
        self.transaction_btn_2.setCheckable(True)

        self.verticalLayout_4.addWidget(self.transaction_btn_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 139, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.pushButton_12 = QPushButton(self.widget_2)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setStyleSheet(u"QPushButton { \n"
"background-color: #2D89EF; \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: #1E6FD9; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        self.pushButton_12.setIcon(icon6)
        self.pushButton_12.setIconSize(QSize(20, 20))
        self.pushButton_12.setCheckable(True)

        self.verticalLayout_5.addWidget(self.pushButton_12)


        self.gridLayout.addWidget(self.widget_2, 0, 1, 2, 1)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"background-color: rgb(0, 85, 127);")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_13 = QPushButton(self.widget_3)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setStyleSheet(u"QPushButton { \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: #1E6FD9; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        icon7 = QIcon()
        icon7.addFile(u":/images/menu (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_13.setIcon(icon7)
        self.pushButton_13.setIconSize(QSize(35, 35))
        self.pushButton_13.setCheckable(True)

        self.horizontalLayout.addWidget(self.pushButton_13)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 600 italic 14pt \"Segoe UI\";")

        self.verticalLayout_6.addWidget(self.label_4)

        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 350 italic 10pt \"Segoe UI\";")

        self.verticalLayout_6.addWidget(self.label_5)


        self.horizontalLayout.addLayout(self.verticalLayout_6)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_14 = QPushButton(self.widget_3)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setStyleSheet(u"QPushButton { \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: #1E6FD9; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        icon8 = QIcon()
        icon8.addFile(u":/images/search (2).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_14.setIcon(icon8)
        self.pushButton_14.setIconSize(QSize(35, 35))
        self.pushButton_14.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.pushButton_14)

        self.lineEdit = QLineEdit(self.widget_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.label_6 = QLabel(self.widget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(40, 40))
        self.label_6.setPixmap(QPixmap(u":/images/profile.png"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_6)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)

        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setStyleSheet(u"background-color: rgb(0, 85, 127);")
        self.verticalLayout_14 = QVBoxLayout(self.widget_4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.stackedWidget = QStackedWidget(self.widget_4)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_35 = QVBoxLayout(self.page)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_48 = QLabel(self.page)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMaximumSize(QSize(65, 65))
        self.label_48.setPixmap(QPixmap(u":/images/fine (1).png"))
        self.label_48.setScaledContents(True)

        self.horizontalLayout_42.addWidget(self.label_48)

        self.label_49 = QLabel(self.page)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setStyleSheet(u"font: 600 italic 20pt \"Segoe UI\";")

        self.horizontalLayout_42.addWidget(self.label_49)


        self.verticalLayout_29.addLayout(self.horizontalLayout_42)

        self.label_50 = QLabel(self.page)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setStyleSheet(u"font: 600 italic 12pt \"Segoe UI\";")

        self.verticalLayout_29.addWidget(self.label_50)


        self.verticalLayout_34.addLayout(self.verticalLayout_29)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_51 = QLabel(self.page)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setStyleSheet(u"font: 600 italic 18pt \"Segoe UI\";")

        self.verticalLayout_32.addWidget(self.label_51)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_52 = QLabel(self.page)
        self.label_52.setObjectName(u"label_52")

        self.horizontalLayout_43.addWidget(self.label_52)

        self.fine_line_1 = QLineEdit(self.page)
        self.fine_line_1.setObjectName(u"fine_line_1")
        self.fine_line_1.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_43.addWidget(self.fine_line_1)


        self.verticalLayout_31.addLayout(self.horizontalLayout_43)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_53 = QLabel(self.page)
        self.label_53.setObjectName(u"label_53")

        self.horizontalLayout_44.addWidget(self.label_53)

        self.fine_line_2 = QLineEdit(self.page)
        self.fine_line_2.setObjectName(u"fine_line_2")
        self.fine_line_2.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_44.addWidget(self.fine_line_2)


        self.verticalLayout_31.addLayout(self.horizontalLayout_44)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_54 = QLabel(self.page)
        self.label_54.setObjectName(u"label_54")

        self.horizontalLayout_45.addWidget(self.label_54)

        self.fine_line_3 = QLineEdit(self.page)
        self.fine_line_3.setObjectName(u"fine_line_3")
        self.fine_line_3.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_45.addWidget(self.fine_line_3)


        self.verticalLayout_31.addLayout(self.horizontalLayout_45)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_55 = QLabel(self.page)
        self.label_55.setObjectName(u"label_55")

        self.horizontalLayout_46.addWidget(self.label_55)

        self.fine_line_4 = QLineEdit(self.page)
        self.fine_line_4.setObjectName(u"fine_line_4")
        self.fine_line_4.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_46.addWidget(self.fine_line_4)


        self.verticalLayout_31.addLayout(self.horizontalLayout_46)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_56 = QLabel(self.page)
        self.label_56.setObjectName(u"label_56")

        self.horizontalLayout_47.addWidget(self.label_56)

        self.fine_line_5 = QLineEdit(self.page)
        self.fine_line_5.setObjectName(u"fine_line_5")
        self.fine_line_5.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_47.addWidget(self.fine_line_5)


        self.verticalLayout_31.addLayout(self.horizontalLayout_47)


        self.horizontalLayout_52.addLayout(self.verticalLayout_31)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_57 = QLabel(self.page)
        self.label_57.setObjectName(u"label_57")

        self.horizontalLayout_49.addWidget(self.label_57)

        self.fine_line_6 = QLineEdit(self.page)
        self.fine_line_6.setObjectName(u"fine_line_6")
        self.fine_line_6.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_49.addWidget(self.fine_line_6)


        self.verticalLayout_30.addLayout(self.horizontalLayout_49)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.label_58 = QLabel(self.page)
        self.label_58.setObjectName(u"label_58")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_58.sizePolicy().hasHeightForWidth())
        self.label_58.setSizePolicy(sizePolicy1)

        self.horizontalLayout_51.addWidget(self.label_58)

        self.fine_line_7 = QComboBox(self.page)
        self.fine_line_7.addItem("")
        self.fine_line_7.addItem("")
        self.fine_line_7.addItem("")
        self.fine_line_7.setObjectName(u"fine_line_7")
        self.fine_line_7.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_51.addWidget(self.fine_line_7)


        self.verticalLayout_30.addLayout(self.horizontalLayout_51)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_59 = QLabel(self.page)
        self.label_59.setObjectName(u"label_59")
        sizePolicy1.setHeightForWidth(self.label_59.sizePolicy().hasHeightForWidth())
        self.label_59.setSizePolicy(sizePolicy1)

        self.horizontalLayout_50.addWidget(self.label_59)

        self.fine_line_8 = QComboBox(self.page)
        self.fine_line_8.addItem("")
        self.fine_line_8.addItem("")
        self.fine_line_8.addItem("")
        self.fine_line_8.addItem("")
        self.fine_line_8.addItem("")
        self.fine_line_8.setObjectName(u"fine_line_8")
        self.fine_line_8.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_50.addWidget(self.fine_line_8)


        self.verticalLayout_30.addLayout(self.horizontalLayout_50)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.label_60 = QLabel(self.page)
        self.label_60.setObjectName(u"label_60")

        self.horizontalLayout_48.addWidget(self.label_60)

        self.fine_line_9 = QLineEdit(self.page)
        self.fine_line_9.setObjectName(u"fine_line_9")
        self.fine_line_9.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_48.addWidget(self.fine_line_9)


        self.verticalLayout_30.addLayout(self.horizontalLayout_48)


        self.horizontalLayout_52.addLayout(self.verticalLayout_30)


        self.verticalLayout_32.addLayout(self.horizontalLayout_52)


        self.verticalLayout_34.addLayout(self.verticalLayout_32)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.add_fine_btn = QPushButton(self.page)
        self.add_fine_btn.setObjectName(u"add_fine_btn")
        self.add_fine_btn.setStyleSheet(u"QPushButton { \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: #1E6FD9; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        icon9 = QIcon()
        icon9.addFile(u":/images/plus-symbol-button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_fine_btn.setIcon(icon9)
        self.add_fine_btn.setIconSize(QSize(16, 16))
        self.add_fine_btn.setCheckable(True)

        self.horizontalLayout_53.addWidget(self.add_fine_btn)

        self.add_fines_btn = QPushButton(self.page)
        self.add_fines_btn.setObjectName(u"add_fines_btn")
        self.add_fines_btn.setStyleSheet(u"QPushButton { \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: #1E6FD9; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        icon10 = QIcon()
        icon10.addFile(u":/images/vecteezy_an-open-eye-icon-isolated_55810413.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_fines_btn.setIcon(icon10)
        self.add_fines_btn.setIconSize(QSize(20, 20))
        self.add_fines_btn.setCheckable(True)

        self.horizontalLayout_53.addWidget(self.add_fines_btn)

        self.remove_fine_btn = QPushButton(self.page)
        self.remove_fine_btn.setObjectName(u"remove_fine_btn")
        self.remove_fine_btn.setStyleSheet(u"QPushButton { \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: red; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        icon11 = QIcon()
        icon11.addFile(u":/images/delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.remove_fine_btn.setIcon(icon11)
        self.remove_fine_btn.setIconSize(QSize(16, 16))
        self.remove_fine_btn.setCheckable(True)

        self.horizontalLayout_53.addWidget(self.remove_fine_btn)


        self.verticalLayout_34.addLayout(self.horizontalLayout_53)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.borrow_line_17 = QLineEdit(self.page)
        self.borrow_line_17.setObjectName(u"borrow_line_17")
        self.borrow_line_17.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.verticalLayout_33.addWidget(self.borrow_line_17)

        self.borrow_books_table_2 = QTableWidget(self.page)
        self.borrow_books_table_2.setObjectName(u"borrow_books_table_2")
        self.borrow_books_table_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 85, 127);")

        self.verticalLayout_33.addWidget(self.borrow_books_table_2)


        self.verticalLayout_34.addLayout(self.verticalLayout_33)


        self.verticalLayout_35.addLayout(self.verticalLayout_34)

        self.stackedWidget.addWidget(self.page)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_40 = QVBoxLayout(self.page_6)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_61 = QLabel(self.page_6)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMaximumSize(QSize(65, 65))
        self.label_61.setPixmap(QPixmap(u":/images/Webiconset-E-Commerce-Secure-payment.128.png"))
        self.label_61.setScaledContents(True)

        self.horizontalLayout_54.addWidget(self.label_61)

        self.label_62 = QLabel(self.page_6)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setStyleSheet(u"font: 600 italic 20pt \"Segoe UI\";")

        self.horizontalLayout_54.addWidget(self.label_62)


        self.verticalLayout_36.addLayout(self.horizontalLayout_54)

        self.label_63 = QLabel(self.page_6)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setStyleSheet(u"font: 600 italic 12pt \"Segoe UI\";")

        self.verticalLayout_36.addWidget(self.label_63)


        self.verticalLayout_39.addLayout(self.verticalLayout_36)

        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_64 = QLabel(self.page_6)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setStyleSheet(u"font: 600 italic 18pt \"Segoe UI\";")

        self.verticalLayout_37.addWidget(self.label_64)

        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.label_65 = QLabel(self.page_6)
        self.label_65.setObjectName(u"label_65")

        self.horizontalLayout_55.addWidget(self.label_65)

        self.transaction_line_1 = QLineEdit(self.page_6)
        self.transaction_line_1.setObjectName(u"transaction_line_1")
        self.transaction_line_1.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_55.addWidget(self.transaction_line_1)


        self.verticalLayout_37.addLayout(self.horizontalLayout_55)

        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.label_66 = QLabel(self.page_6)
        self.label_66.setObjectName(u"label_66")

        self.horizontalLayout_56.addWidget(self.label_66)

        self.transaction_line_2 = QLineEdit(self.page_6)
        self.transaction_line_2.setObjectName(u"transaction_line_2")
        self.transaction_line_2.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_56.addWidget(self.transaction_line_2)


        self.verticalLayout_37.addLayout(self.horizontalLayout_56)

        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.label_67 = QLabel(self.page_6)
        self.label_67.setObjectName(u"label_67")

        self.horizontalLayout_57.addWidget(self.label_67)

        self.transaction_line_3 = QLineEdit(self.page_6)
        self.transaction_line_3.setObjectName(u"transaction_line_3")
        self.transaction_line_3.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_57.addWidget(self.transaction_line_3)


        self.verticalLayout_37.addLayout(self.horizontalLayout_57)

        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.label_68 = QLabel(self.page_6)
        self.label_68.setObjectName(u"label_68")
        sizePolicy1.setHeightForWidth(self.label_68.sizePolicy().hasHeightForWidth())
        self.label_68.setSizePolicy(sizePolicy1)

        self.horizontalLayout_59.addWidget(self.label_68)

        self.lineEdit_2 = QLineEdit(self.page_6)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_59.addWidget(self.lineEdit_2)


        self.verticalLayout_37.addLayout(self.horizontalLayout_59)

        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.label_69 = QLabel(self.page_6)
        self.label_69.setObjectName(u"label_69")
        sizePolicy1.setHeightForWidth(self.label_69.sizePolicy().hasHeightForWidth())
        self.label_69.setSizePolicy(sizePolicy1)

        self.horizontalLayout_58.addWidget(self.label_69)

        self.transaction_line_5 = QComboBox(self.page_6)
        self.transaction_line_5.addItem("")
        self.transaction_line_5.addItem("")
        self.transaction_line_5.addItem("")
        self.transaction_line_5.setObjectName(u"transaction_line_5")
        self.transaction_line_5.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_58.addWidget(self.transaction_line_5)


        self.verticalLayout_37.addLayout(self.horizontalLayout_58)


        self.verticalLayout_39.addLayout(self.verticalLayout_37)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.add_transaction_btn = QPushButton(self.page_6)
        self.add_transaction_btn.setObjectName(u"add_transaction_btn")
        self.add_transaction_btn.setStyleSheet(u"QPushButton { \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: #1E6FD9; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        icon12 = QIcon()
        icon12.addFile(u":/images/plus (2).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_transaction_btn.setIcon(icon12)
        self.add_transaction_btn.setIconSize(QSize(16, 16))
        self.add_transaction_btn.setCheckable(True)

        self.horizontalLayout_60.addWidget(self.add_transaction_btn)

        self.view_transaction_btn = QPushButton(self.page_6)
        self.view_transaction_btn.setObjectName(u"view_transaction_btn")
        self.view_transaction_btn.setStyleSheet(u"QPushButton { \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: #1E6FD9; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        icon13 = QIcon()
        icon13.addFile(u":/images/vecteezy_eye-3d-rendering-icon-illustration_28203822.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.view_transaction_btn.setIcon(icon13)
        self.view_transaction_btn.setIconSize(QSize(25, 25))
        self.view_transaction_btn.setCheckable(True)

        self.horizontalLayout_60.addWidget(self.view_transaction_btn)

        self.remove_transaction_btn = QPushButton(self.page_6)
        self.remove_transaction_btn.setObjectName(u"remove_transaction_btn")
        self.remove_transaction_btn.setStyleSheet(u"QPushButton { \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: red; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        icon14 = QIcon()
        icon14.addFile(u":/images/minus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.remove_transaction_btn.setIcon(icon14)
        self.remove_transaction_btn.setIconSize(QSize(16, 16))
        self.remove_transaction_btn.setCheckable(True)

        self.horizontalLayout_60.addWidget(self.remove_transaction_btn)


        self.verticalLayout_39.addLayout(self.horizontalLayout_60)

        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.transaction_table_search = QLineEdit(self.page_6)
        self.transaction_table_search.setObjectName(u"transaction_table_search")
        self.transaction_table_search.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.verticalLayout_38.addWidget(self.transaction_table_search)

        self.transaction_table = QTableWidget(self.page_6)
        self.transaction_table.setObjectName(u"transaction_table")
        self.transaction_table.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 85, 127);")

        self.verticalLayout_38.addWidget(self.transaction_table)


        self.verticalLayout_39.addLayout(self.verticalLayout_38)


        self.verticalLayout_40.addLayout(self.verticalLayout_39)

        self.stackedWidget.addWidget(self.page_6)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_44 = QVBoxLayout(self.page_2)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.label_70 = QLabel(self.page_2)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setMaximumSize(QSize(65, 65))
        self.label_70.setPixmap(QPixmap(u":/images/menu (2).png"))
        self.label_70.setScaledContents(True)

        self.horizontalLayout_61.addWidget(self.label_70)

        self.label_71 = QLabel(self.page_2)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setStyleSheet(u"font: 600 italic 20pt \"Segoe UI\";")

        self.horizontalLayout_61.addWidget(self.label_71)


        self.verticalLayout_41.addLayout(self.horizontalLayout_61)

        self.label_72 = QLabel(self.page_2)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setStyleSheet(u"font: 600 italic 12pt \"Segoe UI\";")

        self.verticalLayout_41.addWidget(self.label_72)


        self.verticalLayout_43.addLayout(self.verticalLayout_41)

        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.show_books_btn = QPushButton(self.page_2)
        self.show_books_btn.setObjectName(u"show_books_btn")
        self.show_books_btn.setStyleSheet(u"QPushButton { \n"
"background-color: #2D89EF; \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: #1E6FD9; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        self.show_books_btn.setIcon(icon1)
        self.show_books_btn.setIconSize(QSize(20, 20))
        self.show_books_btn.setCheckable(True)
        self.show_books_btn.setAutoExclusive(True)

        self.horizontalLayout_63.addWidget(self.show_books_btn)

        self.how_returned_btn = QPushButton(self.page_2)
        self.how_returned_btn.setObjectName(u"how_returned_btn")
        self.how_returned_btn.setStyleSheet(u"QPushButton { \n"
"background-color: #2D89EF; \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: #1E6FD9; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        self.how_returned_btn.setIcon(icon2)
        self.how_returned_btn.setIconSize(QSize(20, 20))
        self.how_returned_btn.setCheckable(True)
        self.how_returned_btn.setAutoExclusive(True)

        self.horizontalLayout_63.addWidget(self.how_returned_btn)

        self.show_borrowed_btn = QPushButton(self.page_2)
        self.show_borrowed_btn.setObjectName(u"show_borrowed_btn")
        self.show_borrowed_btn.setStyleSheet(u"QPushButton { \n"
"background-color: #2D89EF; \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: #1E6FD9; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        self.show_borrowed_btn.setIcon(icon3)
        self.show_borrowed_btn.setIconSize(QSize(20, 20))
        self.show_borrowed_btn.setCheckable(True)
        self.show_borrowed_btn.setAutoExclusive(True)

        self.horizontalLayout_63.addWidget(self.show_borrowed_btn)


        self.verticalLayout_42.addLayout(self.horizontalLayout_63)

        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.show_fines_btn = QPushButton(self.page_2)
        self.show_fines_btn.setObjectName(u"show_fines_btn")
        self.show_fines_btn.setStyleSheet(u"QPushButton { \n"
"background-color: #2D89EF; \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: #1E6FD9; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        self.show_fines_btn.setIcon(icon4)
        self.show_fines_btn.setIconSize(QSize(20, 20))
        self.show_fines_btn.setCheckable(True)

        self.horizontalLayout_62.addWidget(self.show_fines_btn)

        self.show_transaction_btn = QPushButton(self.page_2)
        self.show_transaction_btn.setObjectName(u"show_transaction_btn")
        self.show_transaction_btn.setStyleSheet(u"QPushButton { \n"
"background-color: #2D89EF; \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: #1E6FD9; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        self.show_transaction_btn.setIcon(icon5)
        self.show_transaction_btn.setIconSize(QSize(20, 20))
        self.show_transaction_btn.setCheckable(True)

        self.horizontalLayout_62.addWidget(self.show_transaction_btn)


        self.verticalLayout_42.addLayout(self.horizontalLayout_62)


        self.verticalLayout_43.addLayout(self.verticalLayout_42)

        self.dashboard_table = QTableWidget(self.page_2)
        self.dashboard_table.setObjectName(u"dashboard_table")
        self.dashboard_table.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 85, 127);")

        self.verticalLayout_43.addWidget(self.dashboard_table)


        self.verticalLayout_44.addLayout(self.verticalLayout_43)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_13 = QVBoxLayout(self.page_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(self.page_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(65, 65))
        self.label_7.setPixmap(QPixmap(u":/images/stack-of-books.png"))
        self.label_7.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_7)

        self.label_8 = QLabel(self.page_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font: 600 italic 20pt \"Segoe UI\";")

        self.horizontalLayout_4.addWidget(self.label_8)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.label_9 = QLabel(self.page_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font: 600 italic 12pt \"Segoe UI\";")

        self.verticalLayout_7.addWidget(self.label_9)


        self.verticalLayout_12.addLayout(self.verticalLayout_7)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_10 = QLabel(self.page_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font: 600 italic 18pt \"Segoe UI\";")

        self.verticalLayout_10.addWidget(self.label_10)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_11 = QLabel(self.page_3)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_5.addWidget(self.label_11)

        self.books_line_1 = QLineEdit(self.page_3)
        self.books_line_1.setObjectName(u"books_line_1")
        self.books_line_1.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_5.addWidget(self.books_line_1)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_12 = QLabel(self.page_3)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_6.addWidget(self.label_12)

        self.books_line_2 = QLineEdit(self.page_3)
        self.books_line_2.setObjectName(u"books_line_2")
        self.books_line_2.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_6.addWidget(self.books_line_2)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_13 = QLabel(self.page_3)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_14.addWidget(self.label_13)

        self.books_line_3 = QLineEdit(self.page_3)
        self.books_line_3.setObjectName(u"books_line_3")
        self.books_line_3.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_14.addWidget(self.books_line_3)


        self.verticalLayout_9.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_14 = QLabel(self.page_3)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_7.addWidget(self.label_14)

        self.books_line_4 = QLineEdit(self.page_3)
        self.books_line_4.setObjectName(u"books_line_4")
        self.books_line_4.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_7.addWidget(self.books_line_4)


        self.verticalLayout_9.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_15 = QLabel(self.page_3)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_8.addWidget(self.label_15)

        self.books_line_5 = QLineEdit(self.page_3)
        self.books_line_5.setObjectName(u"books_line_5")
        self.books_line_5.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_8.addWidget(self.books_line_5)


        self.verticalLayout_9.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_15.addLayout(self.verticalLayout_9)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_18 = QLabel(self.page_3)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_9.addWidget(self.label_18)

        self.books_line_6 = QLineEdit(self.page_3)
        self.books_line_6.setObjectName(u"books_line_6")
        self.books_line_6.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_9.addWidget(self.books_line_6)


        self.verticalLayout_8.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_19 = QLabel(self.page_3)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_10.addWidget(self.label_19)

        self.books_line_7 = QLineEdit(self.page_3)
        self.books_line_7.setObjectName(u"books_line_7")
        self.books_line_7.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_10.addWidget(self.books_line_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_16 = QLabel(self.page_3)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_11.addWidget(self.label_16)

        self.books_line_8 = QLineEdit(self.page_3)
        self.books_line_8.setObjectName(u"books_line_8")
        self.books_line_8.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_11.addWidget(self.books_line_8)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_17 = QLabel(self.page_3)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_12.addWidget(self.label_17)

        self.books_line_9 = QLineEdit(self.page_3)
        self.books_line_9.setObjectName(u"books_line_9")
        self.books_line_9.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_12.addWidget(self.books_line_9)


        self.verticalLayout_8.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_20 = QLabel(self.page_3)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_13.addWidget(self.label_20)

        self.books_line_10 = QLineEdit(self.page_3)
        self.books_line_10.setObjectName(u"books_line_10")
        self.books_line_10.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_13.addWidget(self.books_line_10)


        self.verticalLayout_8.addLayout(self.horizontalLayout_13)


        self.horizontalLayout_15.addLayout(self.verticalLayout_8)


        self.verticalLayout_10.addLayout(self.horizontalLayout_15)


        self.verticalLayout_12.addLayout(self.verticalLayout_10)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.add_book_btn = QPushButton(self.page_3)
        self.add_book_btn.setObjectName(u"add_book_btn")
        self.add_book_btn.setStyleSheet(u"QPushButton { \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: #1E6FD9; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        self.add_book_btn.setIcon(icon12)
        self.add_book_btn.setIconSize(QSize(16, 16))
        self.add_book_btn.setCheckable(True)

        self.horizontalLayout_16.addWidget(self.add_book_btn)

        self.View_books_btn = QPushButton(self.page_3)
        self.View_books_btn.setObjectName(u"View_books_btn")
        self.View_books_btn.setStyleSheet(u"QPushButton { \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: #1E6FD9; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        icon15 = QIcon()
        icon15.addFile(u":/images/Basic_Ui_(9).jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.View_books_btn.setIcon(icon15)
        self.View_books_btn.setIconSize(QSize(16, 16))
        self.View_books_btn.setCheckable(True)

        self.horizontalLayout_16.addWidget(self.View_books_btn)

        self.remove_book_btn = QPushButton(self.page_3)
        self.remove_book_btn.setObjectName(u"remove_book_btn")
        self.remove_book_btn.setStyleSheet(u"QPushButton { \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: red; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        self.remove_book_btn.setIcon(icon14)
        self.remove_book_btn.setIconSize(QSize(16, 16))
        self.remove_book_btn.setCheckable(True)

        self.horizontalLayout_16.addWidget(self.remove_book_btn)


        self.verticalLayout_12.addLayout(self.horizontalLayout_16)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.books_table_search = QLineEdit(self.page_3)
        self.books_table_search.setObjectName(u"books_table_search")
        self.books_table_search.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.verticalLayout_11.addWidget(self.books_table_search)

        self.books_table = QTableWidget(self.page_3)
        self.books_table.setObjectName(u"books_table")
        self.books_table.setStyleSheet(u"background-color: rgb(0, 85, 127);\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_11.addWidget(self.books_table)


        self.verticalLayout_12.addLayout(self.verticalLayout_11)


        self.verticalLayout_13.addLayout(self.verticalLayout_12)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_21 = QVBoxLayout(self.page_4)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_21 = QLabel(self.page_4)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(65, 65))
        self.label_21.setPixmap(QPixmap(u":/images/literacy (1).png"))
        self.label_21.setScaledContents(True)

        self.horizontalLayout_17.addWidget(self.label_21)

        self.label_22 = QLabel(self.page_4)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"font: 600 italic 20pt \"Segoe UI\";")

        self.horizontalLayout_17.addWidget(self.label_22)


        self.verticalLayout_19.addLayout(self.horizontalLayout_17)

        self.label_23 = QLabel(self.page_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"font: 600 italic 12pt \"Segoe UI\";")

        self.verticalLayout_19.addWidget(self.label_23)


        self.verticalLayout_20.addLayout(self.verticalLayout_19)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_24 = QLabel(self.page_4)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"font: 600 italic 18pt \"Segoe UI\";")

        self.verticalLayout_17.addWidget(self.label_24)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_28 = QLabel(self.page_4)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_18.addWidget(self.label_28)

        self.return_line_1 = QLineEdit(self.page_4)
        self.return_line_1.setObjectName(u"return_line_1")
        self.return_line_1.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_18.addWidget(self.return_line_1)


        self.verticalLayout_16.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_25 = QLabel(self.page_4)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_19.addWidget(self.label_25)

        self.return_line_2 = QLineEdit(self.page_4)
        self.return_line_2.setObjectName(u"return_line_2")
        self.return_line_2.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_19.addWidget(self.return_line_2)


        self.verticalLayout_16.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_27 = QLabel(self.page_4)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_20.addWidget(self.label_27)

        self.return_line_3 = QLineEdit(self.page_4)
        self.return_line_3.setObjectName(u"return_line_3")
        self.return_line_3.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_20.addWidget(self.return_line_3)


        self.verticalLayout_16.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_33 = QLabel(self.page_4)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_21.addWidget(self.label_33)

        self.return_line_4 = QLineEdit(self.page_4)
        self.return_line_4.setObjectName(u"return_line_4")
        self.return_line_4.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_21.addWidget(self.return_line_4)


        self.verticalLayout_16.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_34 = QLabel(self.page_4)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_22.addWidget(self.label_34)

        self.return_line_5 = QLineEdit(self.page_4)
        self.return_line_5.setObjectName(u"return_line_5")
        self.return_line_5.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_22.addWidget(self.return_line_5)


        self.verticalLayout_16.addLayout(self.horizontalLayout_22)


        self.horizontalLayout_28.addLayout(self.verticalLayout_16)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_26 = QLabel(self.page_4)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_23.addWidget(self.label_26)

        self.return_line_6 = QLineEdit(self.page_4)
        self.return_line_6.setObjectName(u"return_line_6")
        self.return_line_6.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_23.addWidget(self.return_line_6)


        self.verticalLayout_15.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_29 = QLabel(self.page_4)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_24.addWidget(self.label_29)

        self.return_line_7 = QLineEdit(self.page_4)
        self.return_line_7.setObjectName(u"return_line_7")
        self.return_line_7.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_24.addWidget(self.return_line_7)


        self.verticalLayout_15.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_30 = QLabel(self.page_4)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_25.addWidget(self.label_30)

        self.return_line_8 = QLineEdit(self.page_4)
        self.return_line_8.setObjectName(u"return_line_8")
        self.return_line_8.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_25.addWidget(self.return_line_8)


        self.verticalLayout_15.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_31 = QLabel(self.page_4)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_26.addWidget(self.label_31)

        self.return_line_9 = QLineEdit(self.page_4)
        self.return_line_9.setObjectName(u"return_line_9")
        self.return_line_9.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_26.addWidget(self.return_line_9)


        self.verticalLayout_15.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_32 = QLabel(self.page_4)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_27.addWidget(self.label_32)

        self.return_line_10 = QLineEdit(self.page_4)
        self.return_line_10.setObjectName(u"return_line_10")
        self.return_line_10.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_27.addWidget(self.return_line_10)


        self.verticalLayout_15.addLayout(self.horizontalLayout_27)


        self.horizontalLayout_28.addLayout(self.verticalLayout_15)


        self.verticalLayout_17.addLayout(self.horizontalLayout_28)


        self.verticalLayout_20.addLayout(self.verticalLayout_17)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.add_record_btn = QPushButton(self.page_4)
        self.add_record_btn.setObjectName(u"add_record_btn")
        self.add_record_btn.setStyleSheet(u"QPushButton { \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: #1E6FD9; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        self.add_record_btn.setIcon(icon9)
        self.add_record_btn.setIconSize(QSize(16, 16))
        self.add_record_btn.setCheckable(True)

        self.horizontalLayout_29.addWidget(self.add_record_btn)

        self.view_returns_btn = QPushButton(self.page_4)
        self.view_returns_btn.setObjectName(u"view_returns_btn")
        self.view_returns_btn.setStyleSheet(u"QPushButton { \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: #1E6FD9; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        self.view_returns_btn.setIcon(icon10)
        self.view_returns_btn.setIconSize(QSize(20, 20))
        self.view_returns_btn.setCheckable(True)

        self.horizontalLayout_29.addWidget(self.view_returns_btn)

        self.remove_record_btn = QPushButton(self.page_4)
        self.remove_record_btn.setObjectName(u"remove_record_btn")
        self.remove_record_btn.setStyleSheet(u"QPushButton { \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: red; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        self.remove_record_btn.setIcon(icon11)
        self.remove_record_btn.setIconSize(QSize(16, 16))
        self.remove_record_btn.setCheckable(True)

        self.horizontalLayout_29.addWidget(self.remove_record_btn)


        self.verticalLayout_20.addLayout(self.horizontalLayout_29)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.return_table_search = QLineEdit(self.page_4)
        self.return_table_search.setObjectName(u"return_table_search")
        self.return_table_search.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.verticalLayout_18.addWidget(self.return_table_search)

        self.return_books_table = QTableWidget(self.page_4)
        self.return_books_table.setObjectName(u"return_books_table")
        self.return_books_table.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 85, 127);")

        self.verticalLayout_18.addWidget(self.return_books_table)


        self.verticalLayout_20.addLayout(self.verticalLayout_18)


        self.verticalLayout_21.addLayout(self.verticalLayout_20)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_28 = QVBoxLayout(self.page_5)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_35 = QLabel(self.page_5)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(65, 65))
        self.label_35.setPixmap(QPixmap(u":/images/literacy.png"))
        self.label_35.setScaledContents(True)

        self.horizontalLayout_30.addWidget(self.label_35)

        self.label_36 = QLabel(self.page_5)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"font: 600 italic 20pt \"Segoe UI\";")

        self.horizontalLayout_30.addWidget(self.label_36)


        self.verticalLayout_22.addLayout(self.horizontalLayout_30)

        self.label_37 = QLabel(self.page_5)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"font: 600 italic 12pt \"Segoe UI\";")

        self.verticalLayout_22.addWidget(self.label_37)


        self.verticalLayout_27.addLayout(self.verticalLayout_22)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_38 = QLabel(self.page_5)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setStyleSheet(u"font: 600 italic 18pt \"Segoe UI\";")

        self.verticalLayout_25.addWidget(self.label_38)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_39 = QLabel(self.page_5)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_39.addWidget(self.label_39)

        self.borrow_line_1 = QLineEdit(self.page_5)
        self.borrow_line_1.setObjectName(u"borrow_line_1")
        self.borrow_line_1.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_39.addWidget(self.borrow_line_1)


        self.verticalLayout_23.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_40 = QLabel(self.page_5)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_38.addWidget(self.label_40)

        self.borrow_line_2 = QLineEdit(self.page_5)
        self.borrow_line_2.setObjectName(u"borrow_line_2")
        self.borrow_line_2.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_38.addWidget(self.borrow_line_2)


        self.verticalLayout_23.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_41 = QLabel(self.page_5)
        self.label_41.setObjectName(u"label_41")

        self.horizontalLayout_37.addWidget(self.label_41)

        self.borrow_line_3 = QLineEdit(self.page_5)
        self.borrow_line_3.setObjectName(u"borrow_line_3")
        self.borrow_line_3.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_37.addWidget(self.borrow_line_3)


        self.verticalLayout_23.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_42 = QLabel(self.page_5)
        self.label_42.setObjectName(u"label_42")

        self.horizontalLayout_36.addWidget(self.label_42)

        self.borrow_line_4 = QLineEdit(self.page_5)
        self.borrow_line_4.setObjectName(u"borrow_line_4")
        self.borrow_line_4.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_36.addWidget(self.borrow_line_4)


        self.verticalLayout_23.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_47 = QLabel(self.page_5)
        self.label_47.setObjectName(u"label_47")

        self.horizontalLayout_34.addWidget(self.label_47)

        self.borrow_line_5 = QLineEdit(self.page_5)
        self.borrow_line_5.setObjectName(u"borrow_line_5")
        self.borrow_line_5.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_34.addWidget(self.borrow_line_5)


        self.verticalLayout_23.addLayout(self.horizontalLayout_34)


        self.horizontalLayout_40.addLayout(self.verticalLayout_23)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_44 = QLabel(self.page_5)
        self.label_44.setObjectName(u"label_44")

        self.horizontalLayout_31.addWidget(self.label_44)

        self.borrow_line_6 = QLineEdit(self.page_5)
        self.borrow_line_6.setObjectName(u"borrow_line_6")
        self.borrow_line_6.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_31.addWidget(self.borrow_line_6)


        self.verticalLayout_24.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_45 = QLabel(self.page_5)
        self.label_45.setObjectName(u"label_45")

        self.horizontalLayout_32.addWidget(self.label_45)

        self.borrow_line_7 = QLineEdit(self.page_5)
        self.borrow_line_7.setObjectName(u"borrow_line_7")
        self.borrow_line_7.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_32.addWidget(self.borrow_line_7)


        self.verticalLayout_24.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_46 = QLabel(self.page_5)
        self.label_46.setObjectName(u"label_46")

        self.horizontalLayout_33.addWidget(self.label_46)

        self.borrow_line_8 = QLineEdit(self.page_5)
        self.borrow_line_8.setObjectName(u"borrow_line_8")
        self.borrow_line_8.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_33.addWidget(self.borrow_line_8)


        self.verticalLayout_24.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_43 = QLabel(self.page_5)
        self.label_43.setObjectName(u"label_43")

        self.horizontalLayout_35.addWidget(self.label_43)

        self.borrow_line_9 = QLineEdit(self.page_5)
        self.borrow_line_9.setObjectName(u"borrow_line_9")
        self.borrow_line_9.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_35.addWidget(self.borrow_line_9)


        self.verticalLayout_24.addLayout(self.horizontalLayout_35)


        self.horizontalLayout_40.addLayout(self.verticalLayout_24)


        self.verticalLayout_25.addLayout(self.horizontalLayout_40)


        self.verticalLayout_27.addLayout(self.verticalLayout_25)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.add_borrow_record_btn = QPushButton(self.page_5)
        self.add_borrow_record_btn.setObjectName(u"add_borrow_record_btn")
        self.add_borrow_record_btn.setStyleSheet(u"QPushButton { \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: #1E6FD9; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        self.add_borrow_record_btn.setIcon(icon12)
        self.add_borrow_record_btn.setIconSize(QSize(16, 16))
        self.add_borrow_record_btn.setCheckable(True)

        self.horizontalLayout_41.addWidget(self.add_borrow_record_btn)

        self.view_borrows_btn = QPushButton(self.page_5)
        self.view_borrows_btn.setObjectName(u"view_borrows_btn")
        self.view_borrows_btn.setStyleSheet(u"QPushButton { \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: #1E6FD9; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        self.view_borrows_btn.setIcon(icon13)
        self.view_borrows_btn.setIconSize(QSize(25, 25))
        self.view_borrows_btn.setCheckable(True)

        self.horizontalLayout_41.addWidget(self.view_borrows_btn)

        self.remove_borrow_record_btn = QPushButton(self.page_5)
        self.remove_borrow_record_btn.setObjectName(u"remove_borrow_record_btn")
        self.remove_borrow_record_btn.setStyleSheet(u"QPushButton { \n"
"color: white; \n"
"border-radius: 8px; \n"
"padding: 8px 16px; \n"
"font-weight: bold; \n"
"} \n"
"QPushButton:hover { \n"
"background-color: red; \n"
"} \n"
"QPushButton:pressed { \n"
"background-color: #174EA6; \n"
"} ")
        self.remove_borrow_record_btn.setIcon(icon14)
        self.remove_borrow_record_btn.setIconSize(QSize(16, 16))
        self.remove_borrow_record_btn.setCheckable(True)

        self.horizontalLayout_41.addWidget(self.remove_borrow_record_btn)


        self.verticalLayout_27.addLayout(self.horizontalLayout_41)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.borrow_table_search = QLineEdit(self.page_5)
        self.borrow_table_search.setObjectName(u"borrow_table_search")
        self.borrow_table_search.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #ccc;\n"
"border-radius: 5px;\n"
"}")

        self.verticalLayout_26.addWidget(self.borrow_table_search)

        self.borrow_books_table = QTableWidget(self.page_5)
        self.borrow_books_table.setObjectName(u"borrow_books_table")
        self.borrow_books_table.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 85, 127);")

        self.verticalLayout_26.addWidget(self.borrow_books_table)


        self.verticalLayout_27.addLayout(self.verticalLayout_26)


        self.verticalLayout_28.addLayout(self.verticalLayout_27)

        self.stackedWidget.addWidget(self.page_5)

        self.verticalLayout_14.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.widget_4, 1, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_13.toggled.connect(self.widget.setHidden)
        self.pushButton_13.toggled.connect(self.widget_2.setVisible)
        self.dashboard_btn_2.toggled.connect(self.dashboard_btn_1.setChecked)
        self.dashboard_btn_1.toggled.connect(self.dashboard_btn_2.setChecked)
        self.books_btn_2.toggled.connect(self.books_btn_1.setChecked)
        self.books_btn_1.toggled.connect(self.books_btn_2.setChecked)
        self.returned_btn_2.toggled.connect(self.returned_btn_1.setChecked)
        self.returned_btn_1.toggled.connect(self.returned_btn_2.setChecked)
        self.borrowed_btn_2.toggled.connect(self.borrowed_btn_1.setChecked)
        self.borrowed_btn_1.toggled.connect(self.borrowed_btn_2.setChecked)
        self.fines_btn_2.toggled.connect(self.fines_btn_1.setChecked)
        self.fines_btn_1.toggled.connect(self.fines_btn_2.setChecked)
        self.transaction_btn_2.toggled.connect(self.transaction_btn_1.setChecked)
        self.transaction_btn_1.toggled.connect(self.transaction_btn_2.setChecked)
        self.pushButton_12.toggled.connect(MainWindow.close)
        self.pushButton_6.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.dashboard_btn_1.setText("")
        self.books_btn_1.setText("")
        self.returned_btn_1.setText("")
        self.borrowed_btn_1.setText("")
        self.fines_btn_1.setText("")
        self.transaction_btn_1.setText("")
        self.pushButton_6.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Library", None))
        self.dashboard_btn_2.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.books_btn_2.setText(QCoreApplication.translate("MainWindow", u"Books", None))
        self.returned_btn_2.setText(QCoreApplication.translate("MainWindow", u"Returned", None))
        self.borrowed_btn_2.setText(QCoreApplication.translate("MainWindow", u"Borrowed", None))
        self.fines_btn_2.setText(QCoreApplication.translate("MainWindow", u"Fines", None))
        self.transaction_btn_2.setText(QCoreApplication.translate("MainWindow", u"Transactions", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Log out", None))
        self.pushButton_13.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Hello, Yasir", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Welcome to your Library", None))
        self.pushButton_14.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search here", None))
        self.label_6.setText("")
        self.label_48.setText("")
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Fines", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Welcome you at Fines Page", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Add a New Fine", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Fine_No:", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Student_ID:", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Student_Name:", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Borrowed_Book:", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Book_ID:", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Amount:", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.fine_line_7.setItemText(0, QCoreApplication.translate("MainWindow", u"Select  Fine Payment Status", None))
        self.fine_line_7.setItemText(1, QCoreApplication.translate("MainWindow", u"Paid", None))
        self.fine_line_7.setItemText(2, QCoreApplication.translate("MainWindow", u"Pending", None))

        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Reason:", None))
        self.fine_line_8.setItemText(0, QCoreApplication.translate("MainWindow", u"Select reason for fine", None))
        self.fine_line_8.setItemText(1, QCoreApplication.translate("MainWindow", u"Late returned", None))
        self.fine_line_8.setItemText(2, QCoreApplication.translate("MainWindow", u"Not returned(Lost)", None))
        self.fine_line_8.setItemText(3, QCoreApplication.translate("MainWindow", u"Page was tore", None))
        self.fine_line_8.setItemText(4, QCoreApplication.translate("MainWindow", u"Other reason", None))

        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Remarks:", None))
        self.add_fine_btn.setText(QCoreApplication.translate("MainWindow", u"Add Fine", None))
        self.add_fines_btn.setText(QCoreApplication.translate("MainWindow", u"View Fines", None))
        self.remove_fine_btn.setText(QCoreApplication.translate("MainWindow", u"Remove Fine", None))
        self.borrow_line_17.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Fines using Fine_No", None))
        self.label_61.setText("")
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Transactions", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Welcome you at Transaction Page", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Add a New Transaction", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Transaction_ID:", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"From_Account:", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"To_Account:", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Amount:", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Transaction_For:", None))
        self.transaction_line_5.setItemText(0, QCoreApplication.translate("MainWindow", u"Select reason for transaction", None))
        self.transaction_line_5.setItemText(1, QCoreApplication.translate("MainWindow", u"Fine ", None))
        self.transaction_line_5.setItemText(2, QCoreApplication.translate("MainWindow", u"Other", None))

        self.add_transaction_btn.setText(QCoreApplication.translate("MainWindow", u"Add Transaction", None))
        self.view_transaction_btn.setText(QCoreApplication.translate("MainWindow", u"View Transactions", None))
        self.remove_transaction_btn.setText(QCoreApplication.translate("MainWindow", u"Remove Transaction", None))
        self.transaction_table_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Transactio using Transaction_ID", None))
        self.label_70.setText("")
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Welcome you at Dashboard", None))
        self.show_books_btn.setText(QCoreApplication.translate("MainWindow", u" Show Books", None))
        self.how_returned_btn.setText(QCoreApplication.translate("MainWindow", u" Show Returned", None))
        self.show_borrowed_btn.setText(QCoreApplication.translate("MainWindow", u"Show Borrowed", None))
        self.show_fines_btn.setText(QCoreApplication.translate("MainWindow", u"Show Fines", None))
        self.show_transaction_btn.setText(QCoreApplication.translate("MainWindow", u"Show Transactions", None))
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Books", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Welcome you at Books Page", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Add a New Book", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Book_Name:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Book_ID:", None))
        self.books_line_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"100001 etc.", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Book_Type:", None))
        self.books_line_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Fiction, Poetry etc.", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Author:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Publisher:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Copies:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Price:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Remarks:", None))
        self.add_book_btn.setText(QCoreApplication.translate("MainWindow", u"Add Book", None))
        self.View_books_btn.setText(QCoreApplication.translate("MainWindow", u"View Books", None))
        self.remove_book_btn.setText(QCoreApplication.translate("MainWindow", u"Remove Book", None))
        self.books_table_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Book using Book_ID", None))
        self.label_21.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Returned Books", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Welcome you at Books Returning Page", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Add a New Book Rerurn Record", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Return_ID:", None))
        self.return_line_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"10001 etc.", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Book_Name:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Book_Type:", None))
        self.return_line_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Fiction, Noval etc", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Student_Name:", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Student_ID:", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Book_ID:", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Received By:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Borrow_Date:", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Return_Date:", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Remarks:", None))
        self.add_record_btn.setText(QCoreApplication.translate("MainWindow", u"Add Record", None))
        self.view_returns_btn.setText(QCoreApplication.translate("MainWindow", u"View Returns", None))
        self.remove_record_btn.setText(QCoreApplication.translate("MainWindow", u"Remove Record", None))
        self.return_table_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search returns using Return_ID", None))
        self.label_35.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Borrowed Books", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Welcome you at Books Borrowing Page", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Add a New Book Borrow Record", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Borrow_ID:", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Student_Name:", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Student_ID:", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Book_Name:", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Remarks:", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Borrow_Date:", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Return_Date:", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Book_Type:", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Book_ID:", None))
        self.add_borrow_record_btn.setText(QCoreApplication.translate("MainWindow", u"Add Record", None))
        self.view_borrows_btn.setText(QCoreApplication.translate("MainWindow", u"View Borrows", None))
        self.remove_borrow_record_btn.setText(QCoreApplication.translate("MainWindow", u"Remove Record", None))
        self.borrow_table_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Borrow record using Borrow_ID", None))
    # retranslateUi

