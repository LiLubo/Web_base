
# 李禄波
# 2021/2/6 12:53

import threading
import time

# 1.创建锁
mutex = threading.Lock()


def sum_num1():

    num = 1

    # 2.上锁
    mutex.acquire()

    if num == 1:
        # 解锁
        mutex.release()
        return

    # 3.解锁(如果不解锁，会产生死锁问题)
    mutex.release()


def sum_num2():

    # 2.上锁（同一把锁必须先解锁才能再上锁，如果还未解锁则会阻塞）
    mutex.acquire()

    # 3.解锁(如果不解锁，会产生死锁问题)
    mutex.release()

    print("sum_num2:")


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
