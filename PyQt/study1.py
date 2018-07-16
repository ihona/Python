# coding=utf-8
# 从pyQt库导入QtWidget通用窗口类
from PyQt5 import QtWidgets


# 自己建一个mywindows类，以class开头，mywindows是自己的类名，
# （QtWidgets.QWidget）是继承QtWidgets.QWidget类方法，
class mywindow(QtWidgets.QWidget):
    def __init__(self):
        super(mywindow, self).__init__()


import sys

app = QtWidgets.QApplication(sys.argv)
windows = mywindow()
# 在窗口中绑定label
label = QtWidgets.QLabel(windows)
label.setText("hello world!")

windows.show()
sys.exit(app.exec_())
