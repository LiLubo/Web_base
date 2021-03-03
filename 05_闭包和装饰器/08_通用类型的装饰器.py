# 李禄波
# 2021/2/10 10:30

# 结论1：login = fun_out(login)
#       调用被装饰的函数就相当于调用闭包中的内存函数
# 结论2：外层函数的参数就是原始的login

def fun_out(func):
    def fun_in(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return fun_in




