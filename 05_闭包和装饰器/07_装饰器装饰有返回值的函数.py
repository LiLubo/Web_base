# 李禄波
# 2021/2/10 10:30

# 结论1：login = fun_out(login)
#       调用被装饰的函数就相当于调用闭包中的内存函数
# 结论2：外层函数的参数就是原始的login

def fun_out(func):
    def fun_in():
        # 如果函数中没有return则函数没有返回值
        # 因此当获取被修饰函数中的返回值，要在闭包的内层函数中要将执行被修饰函数返回的值再进行返回
        return func()

    return fun_in


@fun_out
def my_test():
    return 100


a = my_test()
print(a)


