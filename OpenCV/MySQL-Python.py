# coding=utf-8
import pymysql

db = pymysql.connect(host='120.78.176.45', port=3306, user='root', passwd='199583ismy', db='insect', charset='utf8')
# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = """select 序号ID from Cicadellinae大叶蝉 where 学名Name like '%红%'"""

# 执行sql语句
cursor.execute(sql)
# 提交到数据库执行
# db.commit()
data = cursor.fetchall()
data_1 = str(data).replace("((",'').replace(",)", '').replace("))", '').replace(")", '').replace(" (", '')
content = []
list = []
list = data_1.split(",")
for i in range(1, len(list)):
    data_int = int(list[i-1])
    print(data_int)
    sql_str = '%s%d' % ('select 学名Name from Cicadellinae大叶蝉 where 序号ID =', data_int)
    cursor.execute(sql_str)
    res = cursor.fetchall()
    content.append(res)
    print(content)
content_str = str(content).replace("(('", '').replace("',),", '').replace("',),)]", '').replace("[", '').replace("), ", '\n').replace("]", '')
print(content_str)


