# 李禄波
# 2021/2/10 9:49

# 装饰器：在不修改原有函数的前提下，给函数增加新的功能
def fun_out(func):
    def fun_in():
        print("验证")
        func()

    return fun_in


@fun_out   # login = fun_out(login)
def login():
    print("登录")


login()
# 结论1：login = fun_out(login)
#       调用被装饰的函数就相当于调用闭包中的内存函数
# 结论2：外层函数的参数就是原始的login