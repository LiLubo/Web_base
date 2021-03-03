# 李禄波
# 2021/2/10 8:53

def fun_c():
    print("fun_c")


# 函数名存放的是函数所在空间的地址
# print(fun_c)

# 函数名() 去函数所在的空间执行对应的代码
# fun_c()

def test(func):
    func()


# 在python中参数传递的都是引用
test(fun_c)

