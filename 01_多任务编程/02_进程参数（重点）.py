# 李禄波
# 2021/2/5 14:06

# 导包
import multiprocessing


# 带参函数
def dance(count):
    for i in range(count):

        print("dance", i)


if __name__ == '__main__':
    # 创建子进程
    # 给带参函数传参

    # args：元组(定义单个元素的元组元素后加,号)
    # my_dance = multiprocessing.Process(target=dance, args=(5,))

    # kwargs:字典(key要和函数中的形参名相同)
    my_dance = multiprocessing.Process(target=dance, kwargs={"count": 5})

    # 开启子进程
    my_dance.start()
