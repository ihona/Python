# coding=utf-8
# coding=utf-8
import sys
from PyQt5 import QtWidgets
import pymysql
from PIL import Image
import cv2
import numpy


class Insect(QtWidgets.QMainWindow):
    def __init__(self):
        super(Insect, self).__init__()

        # 设置窗口标题
        self.setWindowTitle("大叶蝉检索系统")
        # 设置窗口大小
        self.setGeometry(500, 300, 1000, 600)

        # 添加一个文本框
        self.text_edit = QtWidgets.QTextEdit(self)
        # 设置字体大小
        self.text_edit.setFontPointSize(16)
        # 设为中心
        self.setCentralWidget(self.text_edit)
        self.statusBar()
        self.setFocus()

        # 添加选择图片动作
        self.file_item = QtWidgets.QAction('打开', self)
        self.file_item.setShortcut("Ctrl+O")
        self.file_item.setStatusTip('选择图片')
        self.file_item.triggered.connect(self.pic_search)

        # 添加文字检索动作
        self.text_search = QtWidgets.QAction('名称检索', self)
        self.text_search.setShortcut("Ctrl+N")
        self.text_search.setStatusTip('文字检索')
        self.text_search.triggered.connect(self.name_search)

        # 将动作添加到菜单
        self.file = self.menuBar().addMenu('图片检索')

        self.file.addAction(self.file_item)
        self.file = self.menuBar().addMenu('名称检索')
        self.file.addAction(self.text_search)


        # self.path = 'D:/'


        # self.button = QtWidgets.QPushButton('选择图片', self)
        # self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        # self.button.move(100, 100)
        # self.button.clicked.connect(self.show_dialog)
        # self.setFocus()

    def pic_search(self):
        # 打开文件选择窗口
        file_name = QtWidgets.QFileDialog.getOpenFileName(self, '选择图片', 'D:/', 'Image files (*.png *.jpg)')
        if file_name[0]:
            # 通过函数得到图片信息
            self.cutimg(file_name[0])
            img1 = self.get_ImgHash('D:/cutimg.jpg')
            # 查找表有多少记录（多少行）
            count = int(
                self.my_Sql("select count(*) from largeleafhopper").replace('(', '').replace(')', '').replace(',', ''))
            db = pymysql.connect(host='120.78.176.45', port=3306, user='root', passwd='199583ismy', db='insect',
                                 charset='utf8')
            # 设置一个游标
            cursor = db.cursor()
            # 获得返回结果
            for i in range(1, count + 1):
                sql_img1 = '%s%d' % ('select IdentityMale from Cicadellinae大叶蝉 where 序号ID =', i)
                cursor.execute(sql_img1)
                fet1 = cursor.fetchall()
                fet1_str = str(fet1).replace('(', '').replace(')', '').replace(',', '').replace("'", '')
                if (img1 == fet1) :
                    # 设置文本框显示内容
                    self.text_edit.setText(self.sql_search(i))
                    # 读取图片
                    img = cv2.imread('D:/insect.jpg')
                    # 设置一个窗口用来显示图片
                    cv2.namedWindow('img1', 0)
                    # 设置窗口位置
                    cv2.moveWindow('img1', 50, 50)
                    # 设置窗口大小
                    cv2.resizeWindow('img1', 600, 200)
                    # 显示图片
                    cv2.imshow('img1', img)

                    # 找第二张图
                    sql_img2 = '%s%d' % ('select img2 from largeleafhopper where id =', i)
                    # 执行SQL语句
                    cursor.execute(sql_img2)
                    # 获取返回值
                    fet2 = cursor.fetchone()[0]
                    if fet2:
                        file2 = open('D:/img2.jpg', 'wb')
                        file2.write(fet2)
                        img2 = cv2.imread('D:/img2.jpg')
                        cv2.namedWindow('img2', 0)
                        cv2.resizeWindow('img2', 700, 500)
                        cv2.moveWindow('img2', 50, 300)
                        cv2.imshow('img2', img2)

                    # 找第三张图
                    sql_img3 = '%s%d' % ('select img3 from largeleafhopper where id =', i)
                    # 执行SQL语句
                    cursor.execute(sql_img3)
                    # 获取返回值
                    fet3 = cursor.fetchone()[0]
                    if fet3:
                        file3 = open('D:/img3.jpg', 'wb')
                        file3.write(fet3)
                        img3 = cv2.imread('D:/img3.jpg')
                        cv2.namedWindow('img3', 0)
                        cv2.resizeWindow('img3', 600, 200)
                        cv2.moveWindow('img3', 1000, 50)
                        cv2.imshow('img3', img3)



                    break
                else:
                    self.text_edit.setText("抱歉，数据库未能匹配到所选图片......." + "请重新选择图片")

    def sql_search(self, x):
        sql_Name = '%s%d' % ('select 学名Name from Cicadellinae大叶蝉 where 序号ID =', x)
        sql_Species = '%s%d' % ('select Species种属 from Cicadellinae大叶蝉 where 序号ID =', x)
        sql_Quote = '%s%d' % ('select 引证Quote from Cicadellinae大叶蝉 where 序号ID =', x)
        sql_Alias = '%s%d' % ('select 别名Alias from Cicadellinae大叶蝉 where 序号ID =', x)
        sql_TypeLocality = '%s%d' % ('select 模式标本产地TypeLocality from Cicadellinae大叶蝉 where 序号ID =', x)
        sql_TrunkToMeasure = '%s%d' % ('select 提取量度TrunkToMeasure from Cicadellinae大叶蝉 where 序号ID =', x)
        sql_TheColorPattern = '%s%d' % ('select 体色斑纹TheColorPattern from Cicadellinae大叶蝉 where 序号ID =', x)
        sql_TrunkCharacteristics = '%s%d' % (
            'select 体躯特征TrunkCharacteristics from Cicadellinae大叶蝉 where 序号ID =', x)
        sql_Host = '%s%d' % ('select 寄主Host from Cicadellinae大叶蝉 where 序号ID =', x)
        sql_MaleFemaleSexualGenitals = '%s%d' % (
            'select 雄雌性外生殖器MaleFemaleSexualGenitals from Cicadellinae大叶蝉 where 序号ID =', x)
        sql_InsectSamples = '%s%d' % ('select 馆藏标本InsectSamples from Cicadellinae大叶蝉 where 序号ID =', x)
        sql_GeographicalDistribution = '%s%d' % (
            'select 地理分布GeographicalDistribution from Cicadellinae大叶蝉 where 序号ID =', x)
        sql_KeyReference = '%s%d' % ('select 主要文献KeyReference from Cicadellinae大叶蝉 where 序号ID =', x)

        sql_Name_str = self.my_Sql(sql_Name).replace("(('",'').replace("',),",'').replace("('",'')
        sql_Species_str = self.my_Sql(sql_Species).replace('(', '').replace(')', '').replace(',', '').replace(
            "'", '')
        sql_Quote_str = self.my_Sql(sql_Quote).replace('(', '').replace(')', '').replace(',', '').replace("'",
                                                                                                          '')
        sql_Alias_str = self.my_Sql(sql_Alias).replace('(', '').replace(')', '').replace(',', '').replace("'",
                                                                                                          '')
        sql_TypeLocality_str = self.my_Sql(sql_TypeLocality).replace('(', '').replace(')', '').replace(',',
                                                                                                       '').replace(
            "'", '')
        sql_TrunkToMeasure_str = self.my_Sql(sql_TrunkToMeasure).replace('(', '').replace(')', '').replace(',',
                                                                                                           '').replace(
            "'", '')
        sql_TheColorPattern_str = self.my_Sql(sql_TheColorPattern).replace('(', '').replace(')', '').replace(
            ',', '').replace("'", '')
        sql_TrunkCharacteristics_str = self.my_Sql(sql_TrunkCharacteristics).replace('(', '').replace(')',
                                                                                                      '').replace(
            ',', '').replace("'", '')
        sql_Host_str = self.my_Sql(sql_Host).replace('(', '').replace(')', '').replace(',', '').replace("'", '')
        sql_MaleFemaleSexualGenitals_str = self.my_Sql(sql_MaleFemaleSexualGenitals).replace('(', '').replace(
            ')', '').replace(',', '').replace("'", '')
        sql_InsectSamples_str = self.my_Sql(sql_InsectSamples).replace('(', '').replace(')', '').replace(',',
                                                                                                         '').replace(
            "'", '')
        sql_GeographicalDistribution_str = self.my_Sql(sql_GeographicalDistribution).replace('(', '').replace(
            ')', '').replace(',', '').replace("'", '')
        sql_KeyReference_str = self.my_Sql(sql_KeyReference).replace('(', '').replace(')', '').replace(',',
                                                                                                       '').replace(
            "'", '')
        result = '学名：' + sql_Name_str + '\n' + '\n' + '种属：' + sql_Species_str + '\n' + '\n' + '引证：' + sql_Quote_str + '\n' + '\n' + '别名：' + sql_Alias_str + '\n' + '\n' + '模式标本产地：' + sql_TypeLocality_str + '\n' + '\n' + '提取量度：' + sql_TrunkToMeasure_str + '\n' + '\n' + '体色斑纹：' + sql_TheColorPattern_str + '\n' + '\n' + '体躯特征：' + sql_TrunkCharacteristics_str + '\n' + '\n' + '寄主' + sql_Host_str + '\n' + '\n' + '雄雌性外生殖器：' + sql_MaleFemaleSexualGenitals_str + '\n' + '\n' + '馆藏标本：' + sql_InsectSamples_str + '\n' + '\n' + '地理分布：' + sql_GeographicalDistribution_str + '\n' + '\n' + '主要文献：' + sql_KeyReference_str
        return result

    def name_search(self):
        db_text = pymysql.connect(host='120.78.176.45', port=3306, user='root', passwd='199583ismy', db='insect',
                                  charset='utf8')
        cursor = db_text.cursor()
        text, ok = QtWidgets.QInputDialog.getText(self, '名称检索', '请输入关键字：')
        if ok:
            te = '%' + text + '%'
            sql = "select 序号ID from Cicadellinae大叶蝉 where 学名Name LIKE '%s'" % te
            id = int(self.my_Sql(sql).replace('(', '').replace(')', '').replace(',', ''))
            print(id)
            self.text_edit.setText(self.sql_search(id))


            # 第一张图
            sql_img1_str = '%s%d' % ('select img1 from largeleafhopper where id = ', id)
            cursor.execute(sql_img1_str)
            fet_text = cursor.fetchone()[0]
            file_text = open('D:/img1_text.jpg', 'wb')
            file_text.write(fet_text)
            img1_text = cv2.imread('D:/img1_text.jpg')
            cv2.namedWindow('img1_text', 0)
            cv2.moveWindow('img1_text', 50, 50)
            cv2.resizeWindow('img1_text', 600, 200)
            cv2.imshow('img1_text', img1_text)


            # 第二张图
            sql_img2_str = '%s%d' % ('select img2 from largeleafhopper where id = ', id)
            cursor.execute(sql_img2_str)
            fet_text2 = cursor.fetchone()[0]
            if fet_text2:
                file_text2 = open('D:/img2_text.jpg', 'wb')
                file_text2.write(fet_text2)
                img2_text = cv2.imread('D:/img2_text.jpg')
                cv2.namedWindow('img2_text', 0)
                cv2.moveWindow('img2_text', 50, 300)
                cv2.resizeWindow('img2_text', 700, 500)
                cv2.imshow('img2_text', img2_text)

            # 第三张图
            sql_img3_str = '%s%d' % ('select img3 from largeleafhopper where id = ', id)
            cursor.execute(sql_img3_str)
            fet_text3 = cursor.fetchone()[0]
            if fet_text3:
                file_text3 = open('D:/img3_text.jpg', 'wb')
                file_text3.write(fet_text3)
                img3_text = cv2.imread('D:/img3_text.jpg')
                cv2.namedWindow('img3_text', 0)
                cv2.moveWindow('img3_text', 1000, 50)
                cv2.resizeWindow('img3_text', 600, 200)
                cv2.imshow('img3_text', img3_text)


    def my_Sql(self, statement):
        # 连接数据库
        db = pymysql.connect(host='120.78.176.45', port=3306, user='root', passwd='199583ismy', db='insect',
                             charset='utf8')
        # 设置一个游标
        cursor = db.cursor()
        # 执行SQL语句
        cursor.execute(statement)
        # 获得返回结果
        data = cursor.fetchall()
        return str(data)

    def get_Gray(self, image_file):
        tmpls = []
        for h in range(0, image_file.size[1]):
            for w in range(0, image_file.size[0]):
                tmpls.append(image_file.getpixel((w, h)))
        return tmpls

    # 获取平均灰度值
    def get_Avg(self, ls):
        return sum(ls) / len(ls)

    # 比较100个字符有几个字符相同
    def get_MH(self, a, b):
        dist = 0
        for i in range(0, len(a)):
            if a[i] == b[i]:
                dist = dist + 1
        return dist

    def get_ImgHash(self, fne):
        # 打开图片
        image_file = Image.open(fne)
        # 重置图片大小为12px X 12px
        image_file = image_file.resize((12, 12))
        # 转256灰度图
        image_file = image_file.convert("L")
        # 灰度集合
        Gravls = self.get_Gray(image_file)
        # 灰度平均值
        avg = self.get_Avg(Gravls)
        # 接收获取0或1
        bitls = ''
        for h in range(1, image_file.size[1] - 1):
            for w in range(1, image_file.size[0] - 1):
                # 像素的值比较平均值，大于记为1，小于记为0
                if image_file.getpixel((w, h)) >= avg:
                    bitls = bitls + '1'
                else:
                    bitls = bitls + '0'
        return bitls


    def cutimg(self, image):
        img = cv2.imread(image)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
        gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=-1)

        # subtract the y-gradient from the x-gradient
        gradient = cv2.subtract(gradX, gradY)
        gradient = cv2.convertScaleAbs(gradient)
        blurred = cv2.blur(gradient, (9, 9))
        (_, thresh) = cv2.threshold(blurred, 90, 255, cv2.THRESH_BINARY)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))
        closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
        closed = cv2.erode(closed, None, iterations=30)
        closed = cv2.dilate(closed, None, iterations=30)
        (_, cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]

        # compute the rotated bounding box of the largest contour
        rect = cv2.minAreaRect(c)
        box = numpy.int0(cv2.boxPoints(rect))
        # draw a bounding box arounded the detected barcode and display the image
        cv2.drawContours(img, [box], -1, (0, 255, 0), 3)
        # cv2.imshow("img", img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        Xs = [i[0] for i in box]
        Ys = [i[1] for i in box]
        x1 = min(Xs)
        x2 = max(Xs)
        y1 = min(Ys)
        y2 = max(Ys)
        hight = y2 - y1
        width = x2 - x1
        cropImg = img[y1:y1 + hight, x1:x1 + width]
        cv2.imwrite('D:/cutimg.jpg', cropImg)


app = QtWidgets.QApplication(sys.argv)
Ui = Insect()
Ui.show()
sys.exit(app.exec_())
