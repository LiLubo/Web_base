# 李禄波
# 2021/2/6 12:06

# 线程间共享全局变量

import threading
import time

g_num = []


def my_write():

    global g_num

    for i in range(5):
        g_num.append(i)

    print("write:", g_num)


def my_read():

    global g_num

    print("read:", g_num)


if __name__ == '__main__':

    sub_write = threading.Thread(target=my_write)
    sub_read = threading.Thread(target=my_read)

    sub_write.start()
    time.sleep(1)
    sub_read.start()
