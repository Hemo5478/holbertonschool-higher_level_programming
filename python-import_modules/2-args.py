#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    num_args = len(argv) - 1
    print("{:d} argument{}".format(num_args, "" if num_args == 1 else "s"), end="")
    print("{}".format("." if num_args == 0 else ":"))
    if num_args > 0:
        for i in range(1, num_args + 1):
            print("{:d}: {}".format(i, argv[i]))
