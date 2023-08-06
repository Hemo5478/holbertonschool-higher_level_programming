#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    args = argv[1:]
    add_arg = 0
    for arg in args:
        add_arg += int(arg)
    print(add_arg)
