# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(328, 273)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.price_box = QtWidgets.QLineEdit(self.centralwidget)
        self.price_box.setObjectName("price_box")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.price_box)
        self.tax_rate = QtWidgets.QSpinBox(self.centralwidget)
        self.tax_rate.setProperty("value", 20)
        self.tax_rate.setObjectName("tax_rate")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.tax_rate)
        self.calc_tax_button = QtWidgets.QPushButton(self.centralwidget)
        self.calc_tax_button.setObjectName("calc_tax_button")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.calc_tax_button)
        self.results_output = QtWidgets.QLabel(self.centralwidget)
        self.results_output.setText("")
        self.results_output.setObjectName("results_output")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.results_output)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(-100, -100, 328, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Sales Tax Calculator"))
        self.label.setText(_translate("MainWindow", "Price"))
        self.calc_tax_button.setText(_translate("MainWindow", "Calculate Tax"))
        self.label_2.setText(_translate("MainWindow", "Tax Rate %"))