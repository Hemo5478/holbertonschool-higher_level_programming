#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    compt = 0
    for i in range(0, x):
        try:
            print(f"{my_list[i]}", end="")
            compt += 1
        except IndexError:
            pass
    print()
    return (compt)
