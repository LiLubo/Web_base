# 李禄波
# 2021/2/10 11:53

class Func:
    def __init__(self, fn):
        # fn 用来保存被装饰的函数的原始地址
        self.__fn = fn

    # 让对象加上小括号就可以直接调用该方法
    def __call__(self, *args, **kwargs):

        print("验证")
        # 执行被装饰的函数
        self.__fn()


@Func   # my_test = Func(my_test)
def my_test():
    print("登录")


# 此时my_test相当于一个对象，而对象加()可以调用内置的__call__()方法
my_test()