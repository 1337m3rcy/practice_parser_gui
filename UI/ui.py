# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QTableView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(653, 710)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(180, 20, 271, 21))
        self.pushButton.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 4px rgba(255, 255, 255, 40);\n"
"border-raduis: 7px;\n"
"color: rgb(255, 255, 255);")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setEnabled(True)
        self.tableView.setGeometry(QRect(40, 140, 541, 371))
        self.tableView.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 4px rgba(255, 255, 255, 40);\n"
"border-raduis: 7px;\n"
"color: rgb(0, 0, 0);")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(140, 100, 341, 24))
        self.pushButton_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 4px rgba(255, 255, 255, 40);\n"
"border-raduis: 7px;\n"
"color: rgb(255, 255, 255);")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(80, 50, 471, 41))
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 4px rgba(255, 255, 255, 40);\n"
"border-raduis: 7px;\n"
"color: rgb(255, 255, 255);")
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 4px rgba(255, 255, 255, 40);\n"
"border-raduis: 7px;\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 4px rgba(255, 255, 255, 40);\n"
"border-raduis: 7px;\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.comboBox)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(40, 530, 221, 24))
        self.pushButton_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 4px rgba(255, 255, 255, 40);\n"
"border-raduis: 7px;\n"
"color: rgb(255, 255, 255);")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(360, 530, 221, 24))
        self.pushButton_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 4px rgba(255, 255, 255, 40);\n"
"border-raduis: 7px;\n"
"color: rgb(255, 255, 255);")
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(260, 570, 101, 24))
        self.pushButton_5.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 4px rgba(255, 255, 255, 40);\n"
"border-raduis: 7px;\n"
"color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"parser App", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u043e\u0435\u0434\u0438\u043d\u0438\u0435 \u0441 \u0441\u0430\u0439\u0442\u043e\u043c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Parser", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u0442\u0440\u0430\u043d\u0443 \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430 \u043f\u0440\u043e\u043a\u0441\u0438:", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0432 JSON", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043a\u0430\u0440\u0442\u0443 IP", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043a\u0430\u0440\u0442\u0443", None))
    # retranslateUi

