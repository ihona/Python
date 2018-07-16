# coding=utf-8
import pymysql

db = pymysql.connect(host='120.78.176.45', port=3306, user='root', passwd='199583ismy', db='insect', charset='utf8')
# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
# sql = "insert into insect(name,img1,img2) VALUES (%s,%s,%s)", ('test1', pymysql.BINARY(img1), pymysql.BINARY(img2))
# 执行sql语句
# cursor.execute("insert into insect(name,img1,img2) VALUES (%s,%s,%s)", ('test1', pymysql.BINARY(img1), pymysql.BINARY(img2)))
for i in range(1, 151):
    sql_id = '%s%d' % ('select IdentityMale from Cicadellinae大叶蝉 where 序号ID =', i)
    cursor.execute(sql_id)
    data = cursor.fetchall()
    data_re = str(data).replace("(('", '').replace("',),)", '')
    print(i)
    print(data_re)

