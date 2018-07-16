# coding=utf-8
import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='199583ismy', db='testdb')

cursor = db.cursor()

sql = 'select * from table1'

cursor.execute(sql)

print(cursor.fetchall())