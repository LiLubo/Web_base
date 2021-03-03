# 李禄波
# 2021/2/16 11:06

# 特点：生成器可以记录代码的执行状态
# 效果：节省空间资源

def func():
    for i in range(5):
        print("start")
        # 如果函数中包含yield，则该函数是一个生成器
        yield i
        print("end")


# 通过func创建生成器a
a = func()

# next可以执行生成器
# next执行完毕之后，会把yield后的数值返回（和return很相似）
# 即该函数的出口在yield处，下次再调用next()会接着上次执行到的位置继续执行
# 执行next()当超出范围之后，会出现异常（可以进行异常处理）
ret = next(a)
print(ret)

# for 循环也可以使用生成器,此时,即使超出范围也不会报异常
for x in a:
    print(a)