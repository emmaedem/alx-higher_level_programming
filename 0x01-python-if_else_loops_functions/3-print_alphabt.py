#!/usr/bin/python3
# a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
# Print all the letters except q and e.

for alphabet in range(97, 123):
    if alphabet != 101 and alphabet != 113:
        print(chr(alphabet), end="")
