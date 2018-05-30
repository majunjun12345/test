import os


def cdir():
    print os.getcwd()


def rite():
    path = os.path.join(os.getcwd(), "tt.txt")
    print path
    fd = os.open(path, os.O_CREAT|os.O_APPEND|os.O_WRONLY)
    os.write(fd, "hello world\n")
    os.close(fd)



if __name__ == "__main__":
    rite()