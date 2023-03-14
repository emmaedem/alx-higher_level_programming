#!/usr/bin/python3
# a program that prints the ASCII alphabet, in lowercase,
# not followed by a new line.
# Print all the letters except q and e.

for c in range(ord('a'), ord('z') + 1):

    if c != ord('e') and c != ord('q'):

        print("{:c}".format(c), end="")
