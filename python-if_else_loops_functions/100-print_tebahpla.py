#!/usr/bin/python3
for c in range(122, 96, -1):
    print("{}".format(chr(c - (c % 2) * 32)), end="")
