
# 李禄波
# 2021/2/6 12:34

import threading
import time

g_num = 0

# 互斥锁
# 1.创建锁
mutex = threading.Lock()


def sum_num1():

    global g_num

    # 2.上锁
    mutex.acquire()

    for i in range(1000000):
        g_num += 1

    # 3.解锁(如果不解锁，会产生死锁问题)
    mutex.release()

    print("sum_num1:", g_num)


def sum_num2():
    global g_num

    # 2.上锁（同一把锁必须先解锁才能再上锁，如果还未解锁则会阻塞）
    mutex.acquire()

    for i in range(1000000):
        g_num += 1

    # 3.解锁(如果不解锁，会产生死锁问题)
    mutex.release()

    print("sum_num2:", g_num)


if __name__ == '__main__':

    my_sum_num1 = threading.Thread(target=sum_num1)
    my_sum_num2 = threading.Thread(target=sum_num2)

    # 出错原因，线程竞争CPU的使用权，获取全局变量时有时间差
    # 解决方法1：线程等待 join
    # 解决方法2：互斥锁
    my_sum_num1.start()

    # join：线程等待，让主线程等待已有线程结束以后再继续向下执行
    # my_sum_num1.join()

    my_sum_num2.start()
