# coding=utf-8
# 消息窗口
import sys
from PyQt5 import QtWidgets, QtGui, QtCore


class MessageBox(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("消息窗口演示程序")

    # 如果我们关闭QWidget窗口，QCloseEvent事件就会被触发。
    # 要改变原有的wdiget行为阻止查窗口的关闭，我们就需要重新实现closeEvent()方法。
    def closeEvent(self, event):

        # 第一个字符串参数'确认退出'在消息窗口的标题栏显示。
        # 第二个字符串参数'你确定要退出么？'以对话的形式显示在消息窗口中。返回的结果被保存在reply变量中。
        reply = QtWidgets.QMessageBox.question(self, '确认退出', '你确定要退出么？',
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)

        # 我们使用下面的if语句来判断用户选择的结果。
        # 如果用户选择了Yes按钮，那么关闭widget窗口并终止应用程序的动作会被允许执行。
        # 否则，关闭窗口的动作会被忽略
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

app = QtWidgets.QApplication(sys.argv)
qb = MessageBox()
qb.show()
sys.exit(app.exec_())