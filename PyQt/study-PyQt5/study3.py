# coding=utf-8
# 悬停提示信息
from PyQt5 import QtWidgets, QtGui, QtCore
import sys


class Tooltip(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setGeometry(835, 465, 250, 150)
        self.setWindowTitle("提示信息")

        self.setToolTip("This is a<b>Qwidget</b>widght")
        QtWidgets.QToolTip.setFont(QtGui.QFont("Times", 10))


app = QtWidgets.QApplication(sys.argv)
tooltip = Tooltip()
tooltip.show()
sys.exit(app.exec_())
