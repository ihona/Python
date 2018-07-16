# coding=utf-8
import sys
from PyQt5 import QtWidgets, QtCore
import pymysql


class InputDialog(QtWidgets.QWidget):
    def __init__(self):
        super(InputDialog, self).__init__()

        self.setWindowTitle('大叶蝉检索系统')
        self.setGeometry(500, 500, 500, 300)
        self.button = QtWidgets.QPushButton('检索', self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button.move(20, 20)
        self.button.clicked.connect(self.show_dialog)
        self.setFocus()
        self.label = QtWidgets.QTextEdit(self)
        self.label.move(130, 22)



    def show_dialog(self):
        text, ok = QtWidgets.QInputDialog.getText(self, '检索', '请输入关键字：')
        if ok:
            te = '%'+text+'%'
            db = pymysql.connect(host='120.78.176.45', port=3306, user='root', passwd='199583ismy', db='insect',
                                      charset='utf8')
            cursor = db.cursor()
            sql = "select * from Cicadellinae大叶蝉 where 学名Name LIKE '%s'" % (te)
            cursor.execute(sql)
            data = cursor.fetchall()
            self.label.setText(str(data))

app = QtWidgets.QApplication(sys.argv)
input_dialog = InputDialog()
input_dialog.show()
sys.exit(app.exec_())
