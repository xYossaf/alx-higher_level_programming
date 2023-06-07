#!/usr/bin/python3
import random
number = random.randint(-10, 10)
text = ""
if number > 0:
    text = "positive"
elif number == 0:
    text = "zero"
else:
    text = "negative"
print(f"{number} is {text}")
