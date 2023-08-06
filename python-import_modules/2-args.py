#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    num = len(argv) - 1
    if num == 0:
        print("No arguments.")
    elif num == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num))
    for i in range(1, num + 1):
        arg = argv[i]
        print("{:d}: {}".format(i, arg))
