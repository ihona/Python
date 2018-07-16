# coding=utf-8
import pymysql

def my_Sql(statement):
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

sql = my_Sql('select Q1 from Cicadellinae大叶蝉 where 序号ID = 17 ').replace("(('", "").replace("',),)", "")
val = 'et'
ctx = []
print(sql)
ctx = sql.split('et')
print(ctx)

