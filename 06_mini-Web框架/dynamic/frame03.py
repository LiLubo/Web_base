# 李禄波
# 2021/2/15 11:59

# 函数列表
# {'/index.html': index, '/center.html': center}
func_list = {}


# 路由装饰器
def route(path):  # path = 'index.html'

    def func_out(func):

        func_list[path] = func

        def func_in():
            func()
        return func_in

    return func_out


# 一个函数控制一个变量（切面化编程）
@route('/index.html')      # 1.route() 2.@func_out() ==> index = func_out(index)
def index():
    with open("./template/index.html") as f:
        connect = f.read()
        return connect


@route('/center.html')
def center():
    with open("./template/center.html") as f:
        return f.read()


# 接口函数（不能随便修改）
def application(request_path):

    try:
        # func_list['index.html']
        func = func_list[request_path]
        # func = index
        # func() = index()
        return func()
    except Exception as e:
        print(e)
        return "NOT FOUND"