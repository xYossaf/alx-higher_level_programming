#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastdigit = ((number * -1) % 10) * -1
else:
    lastdigit = number % 10
lasttext = ""
if lastdigit > 5:
    lasttext = "and is greater than 5"
elif lastdigit == 0:
    lasttext = "and is 0"
else:
    lasttext = "and is less than 6 and not 0"
print(f"Last digit of {number} is {lastdigit} {lasttext}")
