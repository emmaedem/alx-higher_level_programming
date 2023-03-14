#!/usr/bin/python3
#a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

for c in range(ord('a'), ord('z') + 1):
     print("{:c}".format(c), end="")
