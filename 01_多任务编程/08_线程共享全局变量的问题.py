# 李禄波
# 2021/2/6 12:15

import threading
import time

g_num = 0


def sum_num1():

    global g_num

    for i in range(1000000):
        g_num += 1

    print("sum_num1:", g_num)


def sum_num2():
    global g_num

    for i in range(1000000):
        g_num += 1

    print("sum_num2:", g_num)


if __name__ == '__main__':

    my_sum_num1 = threading.Thread(target=sum_num1)
    my_sum_num2 = threading.Thread(target=sum_num2)

    # 出错原因，线程竞争CPU的使用权，获取全局变量时有时间差
    my_sum_num1.start()
    my_sum_num2.start()

