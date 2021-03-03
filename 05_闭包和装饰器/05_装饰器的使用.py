# 李禄波
# 2021/2/10 10:30

# 获取函数执行时间
import time


def fun_out(func):
    def fun_in():
        start = time.time()
        func()
        end = time.time()

        take_time = end - start
        print("函数执行时间", take_time)

    return fun_in


# 被装饰的函数
@fun_out
def my_test():

    for i in range(100000):
        print(i)


my_test()


