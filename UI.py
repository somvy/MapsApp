# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\xenon\PycharmProjects\Yandex\API\FullMapApp\UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(957, 516)
        MainWindow.setIconSize(QtCore.QSize(20, 20))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEditSearch = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSearch.setGeometry(QtCore.QRect(400, 0, 371, 31))
        self.lineEditSearch.setObjectName("lineEditSearch")
        self.pushButton_Search = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Search.setGeometry(QtCore.QRect(780, 0, 31, 31))
        self.pushButton_Search.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/normal/icons8-search-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Search.setIcon(icon)
        self.pushButton_Search.setIconSize(QtCore.QSize(31, 31))
        self.pushButton_Search.setFlat(True)
        self.pushButton_Search.setObjectName("pushButton_Search")
        self.pushButton_Plus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Plus.setGeometry(QtCore.QRect(900, 170, 41, 41))
        self.pushButton_Plus.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/normal/icons8-plus-math-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Plus.setIcon(icon1)
        self.pushButton_Plus.setIconSize(QtCore.QSize(31, 31))
        self.pushButton_Plus.setFlat(True)
        self.pushButton_Plus.setObjectName("pushButton_Plus")
        self.pushButton_Minus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Minus.setGeometry(QtCore.QRect(900, 220, 41, 41))
        self.pushButton_Minus.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/normal/icons8-subtract-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Minus.setIcon(icon2)
        self.pushButton_Minus.setIconSize(QtCore.QSize(31, 31))
        self.pushButton_Minus.setFlat(True)
        self.pushButton_Minus.setObjectName("pushButton_Minus")
        self.pushButton_Back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Back.setGeometry(QtCore.QRect(360, 0, 41, 31))
        self.pushButton_Back.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/normal/icons8-back-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Back.setIcon(icon3)
        self.pushButton_Back.setIconSize(QtCore.QSize(31, 31))
        self.pushButton_Back.setFlat(True)
        self.pushButton_Back.setObjectName("pushButton_Back")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 50, 650, 450))
        self.label.setTabletTracking(True)
        self.label.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setText("")
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard)
        self.label.setObjectName("label")
        self.pushButton_Change = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Change.setGeometry(QtCore.QRect(900, 460, 41, 41))
        self.pushButton_Change.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/normal/icons8-transfer-64 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Change.setIcon(icon4)
        self.pushButton_Change.setIconSize(QtCore.QSize(31, 31))
        self.pushButton_Change.setFlat(True)
        self.pushButton_Change.setObjectName("pushButton_Change")
        self.label_adress = QtWidgets.QLabel(self.centralwidget)
        self.label_adress.setGeometry(QtCore.QRect(30, 50, 191, 431))
        self.label_adress.setText("")
        self.label_adress.setObjectName("label_adress")
        self.checkBox_index = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_index.setGeometry(QtCore.QRect(30, 10, 121, 17))
        self.checkBox_index.setObjectName("checkBox_index")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox_index.setText(_translate("MainWindow", "Показывать индекс"))

import ForMaps_rc
