#!/usr/bin/python3
for i in range(97, 123):
    if i not in [113, 101]:
        print("{:s}".format(chr(i)), end="")
