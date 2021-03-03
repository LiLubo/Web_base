# 李禄波
# 2021/2/5 14:16

import multiprocessing
import time

# 全局变量列表
g_num = []


def my_write():

    """向全局变量g_num中写入数据"""
    global g_num

    for i in range(5):
        g_num.append(i)

    print("my_write:", g_num)


def my_read():

    """读取全局变量g_num的值"""
    global g_num

    print("my_read:", g_num)


if __name__ == '__main__':
    # 创建子进程
    write = multiprocessing.Process(target=my_write)
    read = multiprocessing.Process(target=my_read)

    # 开启子进程
    write.start()

    # 保证数据写入g_num中
    time.sleep(1)

    read.start()
