# 李禄波
# 2021/2/9 18:34

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
select_name = input("请输入要查询的物品名称")

sql_select = 'select * from goods where name = %s'
# 传参要在execute函数里进行传参
cur.execute(sql_select, [select_name])

# 4.获取数据
# data是元组类型，元组中的每一个元素都是数据库的一个数据
while True:
    data = cur.fetchone()

    if data is None:
        break

    print(data)


# 5.关闭
cur.close()
conn.close()
