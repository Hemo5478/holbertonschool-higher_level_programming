#!/usr/bin/python3
for i in range(97, 123):
    if i in [101, 113]:
        i += 1
    print("{0}".format(chr(i)), end='')
