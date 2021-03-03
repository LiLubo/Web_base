import pymysql
import time
import json

# 函数列表
# {"/index.html":index, "/center.html":center}
func_list = {}


# 路由装饰器
def route(path):  # path = "/index.html"
    def func_out(func):  # func = index
        func_list[path] = func

        def func_in():
            func()

        return func_in

    return func_out


# 一个函数控制以页面(切面化编程)
@route("/index.html")  # 1 route() 2 @func_out ==> index = func_out(index)
def index():
    with open("./template/index.html", encoding="utf8") as f:
        content = f.read()

    # 1 创建链接
    conn = pymysql.connect(host="localhost",
                           port=3306,
                           user="root",
                           password="123456789",
                           database="stock_db",
                           charset="utf8")

    # 2 创建游标
    cur = conn.cursor()

    # 3 执行sql
    sql = "select * from info;"
    cur.execute(sql)

    # 4 获取数据(元组类型的)
    stock_data = cur.fetchall()

    cur.close()
    conn.close()

    temp = """
                <tr>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <th><input type="button" value="添加"></input></th>
                </tr>
            """
    html = ""
    # 元组形式的股票数据
    # ((1, '000007', '全新好', '10.01%', '4.40%', Decimal('16.05'), Decimal('14.60'), datetime.date(2017, 7, 18),)
    for i in stock_data:
        html += temp % (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])

    content = content.replace("{%content%}", html)
    return content


@route("/center.html")
def center():
    with open("./template/center.html", encoding="utf8") as f:
        content = f.read()
    return content


@route("/ajax.html")
def ajax():
    with open("./template/ajax.html", encoding="utf8") as f:
        content = f.read()

    # content = content.replace("nihao", str(time.time()))
    return content


@route("/ajax_data.html")
def ajax():
    content = [{"time": str(time.time())}]
    content = json.dumps(content)
    return content


# 接口函数(不能随便修改的)
#               /index.html
def application(request_path):
    try:
        #   func_list["/index.html"]
        func = func_list[request_path]
        #   func = index
        #   func() = index()
        return func()
    except Exception as e:
        print(e)
        return "not found"
