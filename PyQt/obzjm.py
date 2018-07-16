# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '第二界面.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 426)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(5, 11, 591, 281))
        self.textBrowser.setObjectName("textBrowser")
        self.out_pushButton = QtWidgets.QPushButton(Form)
        self.out_pushButton.setGeometry(QtCore.QRect(170, 350, 261, 28))
        self.out_pushButton.setObjectName("pushButton")
        self.liulan = QtWidgets.QScrollBar(Form)
        self.liulan.setGeometry(QtCore.QRect(570, 20, 20, 271))
        self.liulan.setOrientation(QtCore.Qt.Vertical)
        self.liulan.setObjectName("liulan")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.out_pushButton.clicked.connect(self.on_dialog1_pushButton_clicked)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.out_pushButton.setText(_translate("Form", "返回"))

    def on_dialog1_pushButton_clicked(self):
            self.form.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())