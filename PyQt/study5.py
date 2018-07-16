# coding=utf-8
# Qt Designer自定义信号emit及传参

from PyQt5 import QtWidgets, QtCore
from PyQt.untitled import Ui_Form
import time

class MyWindow(QtWidgets.QWidget,Ui_Form):
    # 自定义信号，定义参数为str类型
    _singal = QtCore.pyqtSignal(str)
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.myPrint)
        # 将信号连接到函数mySignal
        self._singal.connect(self.mySignal)

    def myPrint(self):
        self.tb.setText("")
        self.tb.append("正在打印，请稍候")
        self._singal.emit("打印结束了吗？快回答！")
    def mySignal(self,string):
        print(string)
        self.tb.append("打印结束")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())