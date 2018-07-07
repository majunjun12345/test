


def per(x, y):
    # if y == 0:
    #     raise ValueError("err")
    # else:
    #     print(x/y)
    # print("majun")
    # return



    try:
        a = x/y
    except BaseException as e:
        print(e)
    finally:
        print("这句话始终会被执行")


def ThrowErr():
    raise Exception("抛出一个异常")


import traceback

def _per(x, y):
    try:
        a = x / y
    except Exception as e:
        return traceback.format_exc()
    return


if __name__ == "__main__":
    # print(_per(1, 0))
    ThrowErr()
