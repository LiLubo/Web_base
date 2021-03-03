# 李禄波
# 2021/2/4 下午4:34

import time
import multiprocessing
import os


def dance():
    # 获取子进程id
    print("子进程 my_dance id:", os.getpid())
    # 获取父进程id
    print("dance父进程：", os.getppid())
    # 获取进程名
    print("dance的进程名是：", multiprocessing.current_process())
    for i in range(5):

        time.sleep(1)
        print("dance", i)


def sing():
    # 获取子进程id
    print("子进程 my_sing id:", os.getpid())
    # 获取父进程id
    print("sing父进程：", os.getppid())
    # 获取进程名
    print("sing的进程名是：", multiprocessing.current_process())
    for i in range(5):

        time.sleep(1)
        print("sing", i)


if __name__ == "__main__":
    # 单进程 需要十秒钟完成
    # 最少有一个进程 该进程中最少有一个线程
    # dance()
    # sing()

    # 获取主进程id
    print("主进程id：", os.getpid())

    # 多进程 需要五秒完成
    # 三个进程： 1个主进程 两个子进程
    # 三个线程： 三个线程 一个进程里有一个线程
    # 创建子进程
    # Process:
    # target:指定执行的任务名（函数名）
    # name:子进程的名字
    my_dance = multiprocessing.Process(target=dance, name="dance")
    my_sing = multiprocessing.Process(target=sing)

    # 开启子进程（不开启子进程不会执行）
    my_dance.start()
    my_sing.start()
