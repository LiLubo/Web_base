# 李禄波
# 2021/2/5 20:15

import threading
import time


def dance(count):

    for i in range(count):
        time.sleep(1)
        print("dance", i)


def sing(count):

    for i in range(count):
        time.sleep(1)
        print("sing", i)


if __name__ == '__main__':
    # 一个进程 三个线程

    # 创建子线程
    # args：元组传参
    my_dance = threading.Thread(target=dance, args=(5,))

    # kwargs：字典传参(字典的key必须和函数的参数名相同)
    my_sing = threading.Thread(target=sing, kwargs={'count': 5})

    # 开启子线程
    my_dance.start()
    my_sing.start()

