# 李禄波
# 2021/2/6 11:

import threading
import time


def fun_c():

    for i in range(5):
        time.sleep(0.2)
        print("fun_c")


if __name__ == '__main__':
    # 让子线程随主线程的结束而结束
    # 1.threading.Thread(target=show_info,deamon=True)
    # 2.线程对象.setDeamon(True)

    # 第一种方法
    # my_fun_c = threading.Thread(target=fun_c, daemon=True)

    my_fun_c = threading.Thread(target=fun_c)

    # 第二种方法
    my_fun_c.setDaemon(True)

    my_fun_c.start()

    time.sleep(0.5)

    print("主线程over")
    exit()

