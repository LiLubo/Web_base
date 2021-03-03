# 李禄波
# 2021/2/5 14:36

# 子进程随主进程结束而结束的两种方式
# 1.设置守护进程
# 2.手动结束子进程

import multiprocessing
import time


def fun_c():

    for i in range(5):
        time.sleep(0.2)
        print("fun_c", i)


if __name__ == '__main__':
    # 注意！！！程序一旦运行就会默认创建主进程
    # 默认：主进程会等待子进程结束之后再结束
    # 将子进程设置为守护进程之后，主进程结束则子进程也会随之结束

    # 主进程创建子进程
    my_fun_c = multiprocessing.Process(target=fun_c)

    # 方式1：设置守护进程(需要在开启子进程之前设置)
    # my_fun_c.daemon = True

    # 主进程开启了子进程
    my_fun_c.start()

    time.sleep(0.5)

    # 方式2：手动结束子进程
    my_fun_c.terminate()

    print("主进程over")
    exit()
