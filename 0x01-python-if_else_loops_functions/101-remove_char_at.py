
# a program that prints the ASCII alphabet, in reverse order, 
# alternating lowercase and uppercase (z in lowercase and Y in uppercase),
# not followed by a new line.

for c in range(122, 96, -1):

    if c % 2 != 0:

        c = c - 32

    print("{}".format(chr(c)), end='')
