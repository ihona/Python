# coding=utf-8
# 将窗口放在屏幕中心
import sys
from PyQt5 import QtWidgets


class Center(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowTitle("窗口置中程序")
        # 该语句用来设置 QWidget 窗口的大小为 250 像素宽，150 像素高。
        self.resize(250, 150)
        self.center()

    def center(self):
        # 该语句用来计算出显示器的分辨率（screen.width, screen.height）。
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        # 该语句用来获取 QWidget 窗口的大小（size.width,size.height）。
        size = self.geometry()
        # 该语句将窗口移动到屏幕的中间位置。
        # 这里move语句是将窗口的左上角移动到((screen.width()- size.width())/2, (screen.height() - size.height())/2)这个位置
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)


app = QtWidgets.QApplication(sys.argv)
center = Center()
center.show()
sys.exit(app.exec_())
