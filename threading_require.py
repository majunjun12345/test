# -*- coding:utf-8 -*-

import threading
import time
from threading import Thread, Lock

lock = threading.Lock()
l = []

# def worker1(i):
#     result = lock.acquire(False)
#     if result:
#         time.sleep(1)
#         print(i)
#         l.append(i)
#         lock.release()
#     else:
#         print("no lock 1")
#
# def worker2(i):
#     result = lock.acquire(False)
#     if result:
#         time.sleep(1)
#         print(i)
#         l.append(i)
#         lock.release()
#     else:
#         print("no lock 2")
#
#
#
# t1 = threading.Thread(target=worker1, args=(1,))
# t2 = threading.Thread(target=worker1, args=(2,))
# t3 = threading.Thread(target=worker1, args=(3,))
# t4 = threading.Thread(target=worker2, args=(4,))
# t5 = threading.Thread(target=worker2, args=(5,))
#
#
# t1.start()
# t1.join()
# t2.start()
# t2.join()
# t3.start()
# t3.join()
# t4.start()
# t4.join()
# t5.start()
# t5.join()
#
# print(l)

num = 0
mutex = Lock()

def fun1():
    global num
    for i in range(1, 10000001):
        while True:
            # result =mutex.acquire(False)
            # result =mutex.acquire()
            # if result:
                # print "i: %s \n" % i
                # print "t1 拿到锁"
            num += 1
                # mutex.release()
                # break
            # else:
            #     print("线程1 虽然没有拿到锁，但是可以唱歌")
            #     time.sleep(0.1)
def fun2():
    global num
    # print "num:%s \n" % num
    for i in range(1, 10000001):
        while True:
            # result = mutex.acquire(False)
            # result = mutex.acquire()
            # if result:
                # print "t:", i
                # print "t2 拿到锁"
            num += 1
                # mutex.release()
                # break
            # else:
            #     print("线程2 虽然没有拿到锁，但是可以跳舞")
            #     time.sleep(0.1)

t_1 = time.time()
t1 = Thread(target=fun1)
t2 = Thread(target=fun2)
t1.start()
t2.start()
t2.join()

t1.join()
print(num)
t_2 = time.time()
print(t_2 - t_1)