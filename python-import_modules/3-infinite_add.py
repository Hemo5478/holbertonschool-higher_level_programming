#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    args = argv[1:]
    add_arg = sum(map(int, args))
    print(add_arg)
