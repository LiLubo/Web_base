# 李禄波
# 2021/2/15 11:59

# 函数列表
# {'/index.html': index, '/center.html': center}
func_list = {}


# 一个函数控制一个变量（切面化编程）
def index():
    with open("./template/index.html") as f:
        connect = f.read()
        return connect


def center():
    with open("./template/center.html") as f:
        return f.read()


func_list["/index.html"] = index
func_list["/center.html"] = center


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