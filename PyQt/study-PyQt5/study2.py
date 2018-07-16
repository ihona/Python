# coding=utf-8
# 设置程序图标
import sys
from PyQt5 import QtWidgets, QtGui


# 我们创建了一个名为Icon的新类，该类继承QtWidgets.QWidget类。
# 因此我们必须调用两个构造函数——Icon的构造函数和继承类QtGui.QWidget类的构造函数。
class Icon(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        # setGeometry()方法完成两个功能——设置窗口在屏幕上的位置和设置窗口本身的大小。
        # 它的前两个参数是窗口在屏幕上的x和y坐标。后两个参数是窗口本身的宽和高。
        # setWindowIcon()方法用来设置程序图标，它需要一个QIcon类型的对象作为参数。
        # 调用QIcon构造函数时，我们需要提供要显示的图标的路径（相对或绝对路径）。
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("图标")
        self.setWindowIcon(QtGui.QIcon('D:/python/PyQt/study-PyQt5/g16.ico'))


app = QtWidgets.QApplication(sys.argv)
icon = Icon()
icon.show()
sys.exit(app.exec_())
