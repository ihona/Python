# coding=utf-8
# 绝对定位方式
import sys
from PyQt5 import QtWidgets, QtGui


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("绝对定位演示程序")
        self.resize(250, 150)
        # 在该示例中，我们简单是使用 move()方法来设置部件的位置。
        # 我们通过 x 和 y 坐标来指定 QLabel 部件的位置.
        # 坐标起点为左上角的顶点。x 坐标从左向右增长，y 坐标从上向下增长。
        QtWidgets.QLabel('Couldn\'t', self).move(15, 10)
        QtWidgets.QLabel('care', self).move(35, 40)
        QtWidgets.QLabel('less', self).move(55, 65)
        QtWidgets.QLabel('and', self).move(115, 65)
        QtWidgets.QLabel('then', self).move(135, 45)
        QtWidgets.QLabel('you', self).move(115, 25)
        QtWidgets.QLabel('kiss', self).move(145, 10)
        QtWidgets.QLabel('me', self).move(215, 10)

app = QtWidgets.QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())