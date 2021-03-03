# 李禄波
# 2021/2/9 18:19

import pymysql

# 1.建立连接
conn = pymysql.connect(host='localhost',
                       port=3306,
                       database='jing_dong',
                       user='root',
                       password='llb2001',
                       charset='utf8')

# 2.创建游标对象
# 游标可以记录获取数据的个数
cur = conn.cursor()

# 3.执行SQL语句
sql = "select * from goods;"
cur.execute(sql)

# 4.获取数据
# data是元组类型，元组中的每一个元素都是数据库的一个数据
while True:
    data = cur.fetchone()
    print(data)
    if data is None:
        break

# 5.关闭
cur.close()
conn.close()
