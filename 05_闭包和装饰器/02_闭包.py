# 李禄波
# 2021/2/10 9:00

# 在函数嵌套（函数里面再定义函数）的前提下
# 内部函数使用了外部函数（还包括外部函数的参数）
# 外部函数返回了内部函数名


def fun_out(data):
    def fun_in():
        print(data)

    return fun_in


func = fun_out(10)
func()
# 结论: func() 等价于 fun_in()
