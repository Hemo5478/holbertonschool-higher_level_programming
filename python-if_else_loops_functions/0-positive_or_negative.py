#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(random, ' is positive')
elif number < 0:
    print(random, ' is negative')
elif number == 0:
    print(random, 'is zero')
