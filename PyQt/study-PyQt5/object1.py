# coding=utf-8
# 文件对话框示例
import sys
import cv2
from PyQt5 import QtWidgets, QtCore, QtGui


class OpenFileDialog(QtWidgets.QMainWindow):
    def __init__(self):
        super(OpenFileDialog, self).__init__()

        self.setWindowTitle('文件对话框演示程序')
        self.setGeometry(300, 300, 400, 300)

        self.text_edit = QtWidgets.QTextEdit()
        self.setCentralWidget(self.text_edit)
        self.statusBar()
        self.setFocus()

        self.file_item = QtWidgets.QAction('打开', self)
        self.file_item.setShortcut("Ctrl+O")
        self.file_item.setStatusTip('打开新文件')
        self.file_item.triggered.connect(self.show_dialog)

        self.file = self.menuBar().addMenu('文件')
        self.file.addAction(self.file_item)

    def show_dialog(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName(self, '打开文件', 'D:/')

        img = cv2.imread(file_name[0])
        data = img.shape
        self.text_edit.setText('文件：'+file_name[0]+'\n'+'文件信息：'+str(data))
        # try:
        #     file = open(file_name[0], 'r')
        #     data = file.read()
        # except UnicodeDecodeError:
        #     data = '不是合法的文件'
        # except FileNotFoundError:
        #     data = ''
        # self.text_edit.setText(data)


app = QtWidgets.QApplication(sys.argv)
file_d = OpenFileDialog()
file_d.show()
sys.exit(app.exec_())
