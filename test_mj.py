import os


def cdir():
    print os.getcwd()


def rite():
    path = os.path.join(os.getcwd(), "tt.txt")
    print path
    fd = os.open(path, os.O_CREAT|os.O_APPEND|os.O_WRONLY)
    os.write(fd, "hello world\n")
    os.close(fd)


num = 6

def a():
    global num
    print num
    num = 4

def b():
    global num
    print num
    num = 3
    print num


if __name__ == "__main__":
    # rite()
    a()
    b()