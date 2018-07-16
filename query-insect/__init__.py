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


count = int(my_Sql("select count(*) from largeleafhopper").replace('(', '').replace(')', '').replace(',', ''))
print(count)
for i in range(1, 2):
    sql = '%s%d' % ('select name from largeleafhopper where id =', i)
    img2 = my_Sql(sql).replace('(', '').replace(')', '').replace(',', '')
    print(img2)
