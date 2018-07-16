# coding=utf-8
import pymysql

db = pymysql.connect(host='120.78.176.45', port=3306, user='root', passwd='199583ismy', db='insect',
                                 charset='utf8')

cursor = db.cursor()
sql_img1 = '%s%d' % ('select IdentityMale from Cicadellinae大叶蝉 where 序号ID =', 1)
cursor.execute(sql_img1)
fet1 = cursor.fetchall()
fet1_str = str(fet1).replace('(', '').replace(')', '').replace(',', '').replace("'", '')
print(fet1_str)