# coding=utf-8
# 输入对话框示例
import sys
from PyQt5 import QtWidgets, QtCore


class InputDialog(QtWidgets.QWidget):
    def __init__(self):
        super(InputDialog, self).__init__()

        self.setWindowTitle("输入对话框演示程序")
        self.setGeometry(500, 500, 500, 300)
        self.button = QtWidgets.QPushButton('对话框', self)
        # 将按钮的焦点策略设定为NoFocus，
        # 关于焦点，简单介绍一下，在应用程序中，都会有一个当前窗口，
        # 即当前获得焦点事件的窗口，这个窗口可以接受键盘的输入。
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button.move(20, 20)
        self.button.clicked.connect(self.show_dialog)
        # 将当前窗口设为焦点窗口，即设为选中状态
        self.setFocus()

        self.label = QtWidgets.QTextEdit(self)
        self.label.move(130, 22)

    def show_dialog(self):
        # 该语句用来显示一个输入对话框。
        # 第一个参数"输入对话框"是对话框的标题。
        # 第二个参数"请输入你的名字："将作为提示信息显示在对话框内。
        # 该对话框将返回用户输入的内容和一个布尔值，如果用户单击OK按钮确认输入，则返回的布尔值为true，否则返回的布尔值为false。
        text, ok = QtWidgets.QInputDialog.getText(self, '输入对话框', '请输入你的名字：')
        if ok:
            self.label.setText(text)


app = QtWidgets.QApplication(sys.argv)
input_dialog = InputDialog()
input_dialog.show()
sys.exit(app.exec_())
