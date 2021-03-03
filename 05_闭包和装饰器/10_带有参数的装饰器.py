# 李禄波
# 2021/2/10 11:36


# 传入参数
def func_out_out(flag):      # flag == "+"

    def func_out(func):

        def func_in(num1, num2):
            if flag == "+":
                print("--正在努力加法计算--")
            elif flag == "-":
                print("--正在努力减法计算--")
            r = func(num1, num2)
            return r

        return func_in

    return func_out


# 使用装饰器装饰函数
@func_out_out('+')      # 1.logging("+") 2.@func_out 3.add = func_out(add)
def add(a, b):
    r = a + b
    return r


result = add(1, 2)
print(result)
