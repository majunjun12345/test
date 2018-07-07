from collections import OrderedDict
from time import time
from random import randint
import traceback


def p():
    a = 0
    b = 3
    s = b/1
    if a == 0:
        raise Exception("error")
    else:
        print(s)
    print("ok")


def order():
    # d = OrderedDict()
    # for i in "abcdef":
    #     start = time()
    #     input()
    #     end = time()
    #     dt = end - start
    #     d[i] = dt
    # return d
    a = input()
    return a


if __name__ == "__main__":
    # order()
    p()