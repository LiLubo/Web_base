# 李禄波
# 2021/2/10 11:06

def func_out01(func01):
    print("this is func_out01")

    def func_in01():
        print("this is func_in01")
        func01()

    return func_in01


def func_out02(func02):
    print("this is func_out02")

    def func_in02():
        print("this is func_in02")
        func02()

    return func_in02


# 就近原则：哪个装饰器距离login函数近就先执行哪个
@func_out02     # login = func_out02(login)
@func_out01     # login = func_out01(login)
def login():
    print("login")


login()

