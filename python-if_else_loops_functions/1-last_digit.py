#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = str(number)
length = len(a)
b = a[length-1:length]
last_digit = int(b)
message = ''
if last_digit > 5:
    message = 'and is greater than 5'
elif last_digit < 6 and last_digit != 0:
    message = 'and is less than 6 and not 0'
else:
    message = 'and is 0'
print('Last digit of', number, 'is', last_digit, message)