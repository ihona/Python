import pymysql

def my_Sql(statement):
    # 连接数据库
    db = pymysql.connect(host='120.78.176.45', port=3306, user='root', passwd='199583ismy', db='movie',
                         charset='utf8')
    # 设置一个游标
    cursor = db.cursor()
    # 执行SQL语句
    cursor.execute(statement)
    # 获得返回结果
    data = cursor.fetchall()
    return str(data)


te = '2010'
na = 'year'
sql = '%s%s%s%s%s' % ('select name, rating_num from res5_utf8 where ', str(na), ' like ', str(te), ' limit 10;')
print(sql)

res = my_Sql(sql).replace("(", "").replace(")", "").replace("'", "")
print(res)
ctx = []
ctx = res.split(',')
ctx1 = []
ctx2 = []

for i in range(0, 9, 2):
    ctx1.append(ctx[i])
for i in range(1, 10, 2):
    ctx2.append(ctx[i])
print(ctx1)
print(ctx2)


sql_2 = '%s%s%s%s%s%s' % (
            "select count(*) from res5_utf8 where genre like ", "'%动作%'", " and director like ", "'%", str(te), "%' ")

res_2 = (my_Sql(sql_2).replace("(", "").replace(")", "").replace("'", "")).replace(",", "")

print(res_2)




sql_ba_genre = '%s%s%s%s%s%s%s' % ("select name, rating_num from res5_utf8 where ", str(na), " like '%", str(te), "%' ", " order by rating_num DESC ", 'limit 15;')
res_ba = (my_Sql(sql_ba_genre).replace("(", "").replace(")", ""))


