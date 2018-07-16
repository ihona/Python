# coding=utf-8
import sys
from PyQt5 import QtWidgets, QtCore
import pymysql

class InputDialog(QtWidgets.QMainWindow):
    def __init__(self):
        super(InputDialog, self).__init__()

        self.setWindowTitle('大叶蝉检索系统')
        main_ground = QtWidgets.QWidget()
        self.setCentralWidget(main_ground)

        grid = QtWidgets.QGridLayout()
        grid.setSpacing(20)


