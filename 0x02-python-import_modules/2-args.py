#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    number = len(sys.argv) - 1
    if number == 0:
        print("{:d} 0-arguments.".format(number))
    elif number == 1:
        print("{:d} 1-argument:".format(number))
    else:
        print("{:d} arguments:".format(number))
    for i in range(number):
        print("{:d}: {}".format(i + 1, sys.argv[i + 1]))
