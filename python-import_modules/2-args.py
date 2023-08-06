#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    nb_arg = len(argv) - 1
    print("{:d} argument{}".format(nb_arg, "" if nb_arg == 1 else "s"), end="")
    print("{}".format("." if nb_arg == 0 else ":"))
    if nb_arg > 0:
        for i in range(1, nb_arg + 1):
            print("{:d}: {}".format(i, argv[i]))
