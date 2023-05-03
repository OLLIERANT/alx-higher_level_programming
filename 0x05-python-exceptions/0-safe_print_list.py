#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """writes a function that prints 'x' elements of a list."""
    index = 0
    while True:
        try:
            if index < x:
                print(my_list[index], end='')
                index += 1
            else:
                print()
                return index
        except IndexError:
            print()
            return index
