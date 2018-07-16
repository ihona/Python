# coding=utf-8
import pymysql
import cv2

db = pymysql.connect(host='120.78.176.45', port=3306, user='root', passwd='199583ismy', db='insect',
                                 charset='utf8')

cursor = db.cursor()

sql_img1 = '%s%d' % ('select img1 from largeleafhopper where id =', 2)
cursor.execute(sql_img1)
fet_text = cursor.fetchone()[0]
file_text = open('D:/img_text.jpg', 'wb')
file_text.write(fet_text)

img = cv2.imread('D:/img_text.jpg')
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.displayOverlay()