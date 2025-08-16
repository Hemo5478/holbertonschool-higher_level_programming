#!/usr/bin/python3
"""Read and display a text file"""


def read_file(filename=""):
    """
    Open a UTF-8 text file and print its contents
    straight to the screen.
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
