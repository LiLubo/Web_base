# 李禄波
# 2021/2/10 9:00

# 在函数嵌套（函数里面再定义函数）的前提下
# 内部函数使用了外部函数（还包括外部函数的参数）
# 外部函数返回了内部函数名


def fun_out(data):
    num1 = 100  # 属于 fun_out
    print('fun_out', num1)

    def fun_in():
        # num1 = 1000     # 属于 fun_in,并没有修改外层函数的变量（就近原则）

        # 声明使用外层函数的变量
        nonlocal num1
        num1 = 1000

        print('fun_in', num1)

    fun_in()
    print("修改后的num1:", num1)

    return fun_in


func = fun_out(10)
func()

# 结论: func() 等价于 fun_in()
