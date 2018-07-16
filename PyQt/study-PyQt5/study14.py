# coding=utf-8
# 发射信号示例
import sys
from PyQt5 import QtWidgets, QtCore


class EmitSignal(QtWidgets.QWidget):

    # 我们创建一个叫做closeEmitApp()的新的信号。这个信号在鼠标按下时产生。
    closeEmitApp = QtCore.pyqtSignal()

    def __init__(self):
        super(EmitSignal, self).__init__()

        self.setWindowTitle('发射信号演示程序')
        self.resize(250, 150)

        # 把自定义的closeEmitApp()信号与槽函数close()连接起来。
        self.closeEmitApp.connect(self.close)

    # 通过信号变量的emit()方法来发射一个信号。
    def mousePressEvent(self, QMouseEvent):
        self.closeEmitApp.emit()


app = QtWidgets.QApplication(sys.argv)
es = EmitSignal()
es.show()
sys.exit(app.exec_())
