# coding=utf-8
# 状态栏
import sys
from PyQt5 import QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        # 所有的类在创建时都会先调用构造函数(python中就是__init__())将实例按照构造函数的操作先进行初始化，
        # 继承了其它类的类，在构造函数中，先要构造他的父类，
        # 在之前的程序中，我们都是直接调用父类的__init__()方法来完成父类的构造，
        # 但是有一种更安全的方法就是用关键字super来完成。
        # super(MainWindow, self).__init__()我们可以这样理解：
        # super(MainWindow, self)首先找到MainWindow的父类（就是QtWidgets.QMainWindow），
        # 然后把类MainWindow的对象self转换为类QtWidgets.QMainWindow的对象，
        # 然后“被转换”的类A对象调用自己的__init__函数。考虑到super中只有指明子类的机制，
        # 因此，在多继承的类定义中，通常我们保留使用之前代码中的方法。
        super(MainWindow, self).__init__()
        self.resize(400, 300)
        self.setWindowTitle("状态栏程序示例")
        self.statusBar().showMessage("就绪")


app = QtWidgets.QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())
