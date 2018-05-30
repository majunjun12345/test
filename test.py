import os


def cdir():
    print os.getcwd()


def write():
    path = os.path.join(os.getcwd(), "tt.txt")
    print path
    fd = os.open(path, os.O_CREAT|os.O_APPEND|os.O_WRONLY)
    os.write(fd, "hello world\n")
    os.close(fd)
    a = 1
    b = 2
    c = 0
    if not a or b:
        print "not"
    else:
        print "yes"


if __name__ == "__main__":
    write()