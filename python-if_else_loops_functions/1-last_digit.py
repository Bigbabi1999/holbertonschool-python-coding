#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

res = abs(number) % 10

if number < 0:
    res = -res
print(f"Last digit of {number} is {res} and ", end="")
if res > 5:
    print(f"is greater than 5")
elif res == 0:
    print(f"is 0")

else:
    print(f"is less than 6 and not 0")
