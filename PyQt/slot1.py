# coding=utf-8
from PyQt5 import QtWidgets
from PyQt.objectui1 import Ui_MainWindow


class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.myPrint)

    def myPrint(self):
        print("hello world")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())
