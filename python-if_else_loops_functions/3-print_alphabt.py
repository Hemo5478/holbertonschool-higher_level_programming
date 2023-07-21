#!/usr/bin/python3
i = 97
for i in range(97, 123):
    if i in [101, 113]:
        continue
    print("{}".format(chr(i)), end='')
