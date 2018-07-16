# coding=utf-8
# 第一个程序
from PyQt5 import QtWidgets
import sys
# 每一个PyQt5程序都需要有一个application对象。
# sys.argv参数是一个命令行参数列表。Python脚本可以从shell中执行，参数可以让我们选择启动脚本的方式。
# sys.argv[]是用来获取命令行参数的，sys.argv[0]表示代码本身文件路径
app = QtWidgets.QApplication(sys.argv)

# QWidget部件是PyQt5中所有用户界面类的父类。
# 这里我们使用没有参数的默认构造函数，它没有继承其它类。我们称没有父类的first_window为一个window。
frist_window = QtWidgets.QWidget()

# resize()方法可以改变窗口部件的大小，在这里我们将其设置为250像素宽，150像素高。
frist_window.resize(250,150)

# 这句用来设置窗口部件的标题，该标题将在标题栏中显示
frist_window.setWindowTitle("第一个程序")

# show()方法将窗口部件显示在屏幕上
frist_window.show()

# 最后我们进入该程序的主循环。事件处理从本行语句开始。主循环接受事件消息并将其分发给程序的各个部件。
# 如果调用exit()或主部件被销毁，主循环就会结束。
# 使用sys.exit()方法退出可以确保程序可以完整的结束，这种情况下系统的环境变量会记录程序是如何退出的。
# 也许你会疑惑，为什么exec_()方法会有一个下划线。这是因为exec是Python的关键字，
# 为避免冲突，PyQt使用exec_()替代。
sys.exit(app.exec_())
