# coding=utf-8
# 一个综合的例子
import sys
from PyQt5 import QtWidgets, QtGui

class MainWidow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWidow,self).__init__()

        self.resize(350,250)
        self.setWindowTitle("我的程序")
        # 创建一个文本编辑器
        text_edit = QtWidgets.QTextEdit()
        # 将文本编辑器设置为QMainWindow的中心部件
        # 中心部件将占据所有的窗口剩余空间
        self.setCentralWidget(text_edit)

        exit_action = QtWidgets.QAction("退出", self)
        exit_action.setStatusTip("退出程序")
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(QtWidgets.qApp.quit)

        self.statusBar()

        self.menu_bar = self.menuBar()
        file = self.menu_bar.addMenu("文件")
        file.addAction(exit_action)

        self.toolbar = self.addToolBar("退出")
        self.toolbar.addAction(exit_action)

app = QtWidgets.QApplication(sys.argv)
main_window = MainWidow()
main_window.show()
sys.exit(app.exec_())

