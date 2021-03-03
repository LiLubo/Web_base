# 李禄波
# 2021/2/15 11:59

# 函数列表
# {'/index.html', '/center.html'}
func_list = {}


# 一个函数控制一个变量（切面化编程）
def index():
    return 'index'


def center():
    return 'center'


func_list['/index.html'] = index
func_list['/center.html'] = center


# 接口函数（不能随便修改）
def application(request_path):

    # if request_path == '/index.html':
    #     response_body = index()
    #
    # elif request_path == '/center.html':
    #     response_body = center()
    # else:
    #     response_body = "not found"
    #
    # return response_body

    # func_list['index.html']
    func = func_list[request_path]
    # func = index
    # func() = index()
    return func()