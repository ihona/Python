# coding=utf-8
# 信号槽示例
import sys
from PyQt5 import QtWidgets, QtCore

# 创建了一个LCD显示器和一个滑块。
# 通过拖动滑块我们可改变LCD显示器的数字。

class SignalSlot(QtWidgets.QWidget):
    def __init__(self):
        super(SignalSlot, self).__init__()

        self.setWindowTitle('信号槽演示程序')
        lcd = QtWidgets.QLCDNumber(self)
        slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(lcd)
        v_box.addWidget(slider)

        self.setLayout(v_box)
        # 这里我们将滑块的 valueChanged信号连接到 LCD 显示器的 display槽函数上。
        # 下面介绍connect 的用法，如果信号发送者对象为emit（这里是 slider 对象），
        # 要发射的信号是signal（这里是valueChanged 信号），
        # 信号的接收者对象accept（这里是 lcd 对象），对信号做出响应的槽函数slot（这里是 display 方法）
        # 那么连接信号和槽的方法为:
        # emit.signal.connect(accept.slot)
        slider.valueChanged.connect(lcd.display)
        self.resize(250, 150)


app = QtWidgets.QApplication(sys.argv)
qb = SignalSlot()
qb.show()
sys.exit(app.exec_())
