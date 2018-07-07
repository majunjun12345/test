import sys
import os
import traceback

    
def check_exit():
    try:
        os.mknod("exec.txt")
    except:
        print traceback.format_exc()

if __name__ == "__main__":
    check_exit()