#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):

            print(my_list[i], end=' ')

    except IndexError:

        pass  # just ignore the index error if x is greater than the list length
    print()  # print a new line after the elements

    return min(x, len(my_list))  # return the actual number of printed elements
