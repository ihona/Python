# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '主界面.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys,time
from PyQt5.QtWidgets import QMessageBox
from PyQt.obzjm import Ui_Form



class Ui_Form1(object):

    def __init__(self):
        super(Ui_Form1, self).__init__()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(595, 424)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 20, 411, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(20, 110, 221, 31))
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.SizeFDiagCursor))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(290, 110, 291, 171))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 350, 221, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 350, 221, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.pushButton_2.clicked.connect(self.output)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "     大叶蝉文字检索系统"))
        self.comboBox.setItemText(0, _translate("Form", "第一个标签"))
        self.comboBox.setItemText(1, _translate("Form", "第二个标签"))
        self.comboBox.setItemText(2, _translate("Form", "第三个标签"))
        self.comboBox.setItemText(3, _translate("Form", "第四个标签"))
        self.pushButton.setText(_translate("Form", "开始搜索"))
        self.pushButton_2.setText(_translate("Form", "关闭程序"))


    # def __init__(self):
    #     # super(mySigmalSlot,self).__init__()
    #     self.setupUi(self)
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.pushButton_2.clicked.connect(self.output)

    def on_pushButton_clicked(self):
        self.form.hide()
        Form1 = QtGui.QDialog()
        self.ui = Ui_Form()
        self.ui.setupUi(Form1)
        Form1.show()
        Form1.exec_()
        self.form.show()



    def output(self):
        # ok = QMessageBox.information(self,("即将退出"),("""谢谢使用"""),
        #     QMessageBox.StandardButtons(QMessageBox.Yes |QMessageBox.No))
        # self.form.close()
        exit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    pass