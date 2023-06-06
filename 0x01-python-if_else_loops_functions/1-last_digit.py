#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = (number * -1) % 10
    neg_last_digit = last_digit * -1
    print(f"Last digit of {number:d} is {neg_last_digit:d}", end=" ")
else:
    last_digit = number % 10
    print(f"Last digit of {number:d} is {last_digit:d}", end=" ")
if number < 0:
    last_digit = last_digit * -1
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
elif last_digit < 6 and not 0:
    print("and is less than 6 and not 0")
