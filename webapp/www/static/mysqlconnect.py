import mysql.connector
# 打开数据库连接
# db = mysql.connect("localhost", "root", "season", "db1")
db = mysql.connector.connect(user='root',password='season',datanase='db1')
#使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute()  方法执行 SQL 查询
cursor.execute('SELECT VERSION()')
# 使用 fetchone() 方法获取单条数据
data = cursor.fetchone()
print("Database version: %s" % data)
cursor.close()
db.close()
